__author__ = 'Hai Bui'

from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
from bll.text_classification import predict, convert_label_to_text
from bll.preprocessor import text_preprocess
from bll.crawler import crawl, count_crawled_post
from bll.call_api import get_all_black_list
import subprocess
import validators
import bll.config_log
import logging


def time_now():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def on_closing():
    if messagebox.askokcancel('Thoát', 'Bạn muốn thoát chứ?'):
        logging.info('Exit')
        root.destroy()


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Tool thu thập, phân loại tin tức")
        self.pack(fill=BOTH, expand=1)
        tab_control_m = ttk.Notebook(self)
        tab_control_m.pack(fill=BOTH, expand=1)
        frm_crawler = ttk.Frame(tab_control_m)
        frm_word_tokenizer = ttk.Frame(tab_control_m)
        frm_text_classification = ttk.Frame(tab_control_m)
        frm_guild = ttk.Frame(tab_control_m)
        tab_control_m.add(frm_crawler, text='   Thu thập dữ liệu   ')
        tab_control_m.add(frm_word_tokenizer, text='   Công cụ tách từ   ')
        tab_control_m.add(frm_text_classification, text='   Phân loại văn bản   ')
        tab_control_m.add(frm_guild, text='   Hướng dẫn   ')

        # Facebook Crawler area
        def write_error_info(message):
            txt_info_cr.config(state=NORMAL)
            txt_info_cr.insert(END, time_now() + '   ' + 'Error: ' + message + '\n', 'error')
            txt_info_cr.config(state=DISABLED)

        def write_warning_info(message):
            txt_info_cr.config(state=NORMAL)
            txt_info_cr.insert(END, time_now() + '   ' + 'Warning: ' + message + '\n', 'warning')
            txt_info_cr.config(state=DISABLED)

        def write_success_info(message):
            txt_info_cr.config(state=NORMAL)
            txt_info_cr.insert(END, time_now() + '   ' + 'Success: ' + message + '\n', 'success')
            txt_info_cr.config(state=DISABLED)

        def clear_info():
            txt_info_cr.config(state=NORMAL)
            txt_info_cr.delete('1.0', END)
            txt_info_cr.config(state=DISABLED)

        def open_black_list():
            black_list = get_all_black_list()
            if black_list == -2:
                write_error_info('Kết nối server thất bại!')
                root.config(cursor='')
                return
            win_black_list = Toplevel(self)
            win_black_list.title('Danh sách đen')
            win_black_list.geometry('854x480')
            win_black_list.resizable(False, False)
            win_black_list.grab_set()
            tab_control_bl = ttk.Notebook(win_black_list)
            tab_control_bl.pack(fill=BOTH, expand=1)
            frm_page_bl = Frame(tab_control_bl)
            frm_group_bl = Frame(tab_control_bl)
            frm_user_bl = Frame(tab_control_bl)
            tab_control_bl.add(frm_page_bl, text='  Page  ')
            tab_control_bl.add(frm_group_bl, text='  Group  ')
            tab_control_bl.add(frm_user_bl, text='  User  ')

            txt_page_bl = Text(frm_page_bl, wrap=WORD, state=DISABLED)
            txt_page_bl.pack(fill=BOTH, expand=True)
            txt_page_bl.tag_config('header', foreground='red', background='yellow')
            # global black_list
            # if len(black_list) <= 0:
            #     black_list = get_all_black_list()
            txt_page_bl.config(state=NORMAL)
            txt_page_bl.insert(END, '{:<35} \t {:<12}'.format('Tên trang', 'URL') + '\n', 'header')
            for i in black_list:
                txt_page_bl.insert(END, '{:<35} \t {:<12}'.format(i['FacebookName'], i['FacebookUrl']) + '\n')
            txt_page_bl.config(state=DISABLED)

        def open_log():
            subprocess.call(['notepad.exe', '../log/run_time.log'])

        def start_crawl():
            url = ent_url_cr.get()
            if len(url) <= 0:
                write_warning_info('Link FB không được để trống!')
                return
            # check valid url
            if validators.url(url):
                pass
            else:
                write_error_info('Link FB không hợp lệ!')
                return
            # check valid scroll down
            try:
                scroll_down = int(spn_numpage_cr.get())
                if scroll_down > 20:
                    write_warning_info('Tối đa 20 lần cuộn trang')
                    return
            except:
                write_error_info('Số lần cuộn trang không hợp lệ.')
                return
            selection = int(select_type.get())
            try:
                status = crawl(url, scroll_down, selection)
                if status == 0:
                    write_success_info('Tổng số bài viết thu thập: ' + str(count_crawled_post()))
                elif status == -1:
                    write_error_info('Link FB không tồn tại!')
                else:
                    write_error_info('Kết nối server thất bại!')
            except:
                write_error_info('Thực thi thất bại!')

        select_type = IntVar()

        frm_top_cr = ttk.Frame(frm_crawler)
        frm_top_cr.pack(fill=BOTH, padx=15, pady=15)
        lbl_url_cr = Label(frm_top_cr, text='Facebook URL: ')
        lbl_url_cr.grid(column=0, row=0)
        ent_url_cr = ttk.Entry(frm_top_cr, width=120)
        ent_url_cr.grid(column=1, row=0)
        # button to open blacklist
        btn_black_list_cr = ttk.Button(frm_top_cr, text='...', width=5, cursor='hand2', command=open_black_list)
        btn_black_list_cr.grid(column=2, row=0, padx=(10, 0))
        lbl_numpage_cr = Label(frm_top_cr, text='Số lần cuộn trang: ')
        lbl_numpage_cr.grid(column=3, row=0, padx=(20, 0))
        spn_numpage_cr = ttk.Spinbox(frm_top_cr, from_=1, to=20, width=5)
        spn_numpage_cr.grid(column=4, row=0)
        spn_numpage_cr.insert(1, 1)
        frm_fbtype_cr = ttk.Frame(frm_top_cr)
        frm_fbtype_cr.grid(column=1, row=1, sticky='w', pady=(10, 0))
        rad_page_cr = ttk.Radiobutton(frm_fbtype_cr, text='Page', variable=select_type, value=1)
        rad_page_cr.grid(column=0, row=0, padx=(0, 15))
        select_type.set(1)
        rad_group_cr = ttk.Radiobutton(frm_fbtype_cr, text='Group', variable=select_type, value=2)
        rad_group_cr.grid(column=1, row=0, padx=(0, 15))
        rad_user_cr = ttk.Radiobutton(frm_fbtype_cr, text='User', variable=select_type, value=3)
        rad_user_cr.grid(column=2, row=0, padx=(0, 15))

        btn_crawl_cr = ttk.Button(frm_top_cr, text='Thu thập', cursor='hand2', command=start_crawl)
        btn_crawl_cr.grid(column=1, row=2, sticky='w', pady=(10, 0))
        btn_show_log_cr = ttk.Button(frm_top_cr, text='Xem log', cursor='hand2', command=open_log)
        btn_show_log_cr.grid(column=1, row=2, sticky='w', padx=(100, 0), pady=(10, 0))
        btn_clear_info_cr = ttk.Button(frm_top_cr, text='Xóa thông báo', cursor='hand2', command=clear_info)
        btn_clear_info_cr.grid(column=1, row=2, sticky='w', padx=(200, 0), pady=(10, 0))

        prg_cr = ttk.Progressbar(frm_crawler, length=200)
        prg_cr.pack(fill=BOTH)
        frm_term_cr = ttk.Frame(frm_crawler)
        frm_term_cr.pack(fill=BOTH)
        txt_info_cr = Text(frm_term_cr, height=35, wrap=WORD, bg='black', state=DISABLED)
        txt_info_cr.pack(fill=BOTH, expand=True)
        # add tag to change color at log
        txt_info_cr.tag_config('error', foreground='red')
        txt_info_cr.tag_config('warning', foreground='yellow')
        txt_info_cr.tag_config('success', foreground='#22ff00')

        # Word Tokenize area
        def get_preprocessor_text():
            txt_output_wt.config(state=NORMAL)
            txt_output_wt.delete('1.0', END)
            txt_output_wt.insert('1.0', text_preprocess(txt_input_wt.get('1.0', END)))
            txt_output_wt.config(state=DISABLED)

        frm_input_wt = ttk.Frame(frm_word_tokenizer)
        frm_input_wt.grid(column=0, row=0)
        lbl_input_wt = Label(frm_input_wt, text='Dữ liệu đầu vào')
        lbl_input_wt.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_input_wt = Text(frm_input_wt, width=78, height=38, wrap=WORD)
        txt_input_wt.pack(expand=True, padx=(5, 3), pady=5)
        frm_output_wt = ttk.Frame(frm_word_tokenizer)
        frm_output_wt.grid(column=1, row=0)
        lbl_output_wt = Label(frm_output_wt, text='Kết quả')
        lbl_output_wt.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_output_wt = Text(frm_output_wt, width=78, height=38, wrap=WORD, state=DISABLED)
        txt_output_wt.pack(expand=True, padx=5, pady=5)
        frm_bottom_wt = ttk.Frame(frm_word_tokenizer)
        frm_bottom_wt.grid(column=0, row=1, columnspan=2)

        btn_wt = ttk.Button(frm_bottom_wt, text='Tách từ', cursor='hand2', command=get_preprocessor_text)
        btn_wt.pack(side=RIGHT, padx=5, pady=5)
        btn_clear_wt = ttk.Button(frm_bottom_wt, text='Xóa text', cursor='hand2')
        btn_clear_wt.pack(side=RIGHT, padx=5, pady=5)

        # Text Classification area
        def get_label():
            if len(txt_input_tc.get('1.0', END)) <= 0:
                messagebox.showwarning('Thông báo', 'Nội dung trống!')
            else:
                lbl_result_tc["text"] = convert_label_to_text(predict(txt_input_tc.get('1.0', END)))
                messagebox.showinfo('Thông báo', 'Xong!')

        def clear_text():
            txt_input_tc.delete('1.0', END)
            lbl_result_tc["text"] = ''

        frm_input_tc = ttk.Frame(frm_text_classification)
        frm_input_tc.pack(fill=BOTH, expand=True)
        lbl_input_tc = Label(frm_input_tc, text='Dữ liệu đầu vào')
        lbl_input_tc.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_input_tc = Text(frm_input_tc, height=35, wrap=WORD)
        txt_input_tc.pack(fill=BOTH, padx=5, pady=5, expand=True)
        frm_output_tc = ttk.Frame(frm_text_classification)
        frm_output_tc.pack(fill=BOTH, expand=True)
        lbl_output_tc = Label(frm_output_tc, text='Kết quả:')
        lbl_output_tc.pack(side=LEFT, anchor=N, padx=5, pady=5)
        lbl_result_tc = Label(frm_output_tc, fg='red')
        lbl_result_tc.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btn_tc = ttk.Button(frm_output_tc, text='Phân loại', cursor='hand2', command=get_label)
        btn_tc.pack(side=RIGHT, padx=5, pady=5)
        btn_clear_tc = ttk.Button(frm_output_tc, text='Xóa text', cursor='hand2', command=clear_text)
        btn_clear_tc.pack(side=RIGHT, padx=5, pady=5)


if __name__ == "__main__":
    logging.info('Start up')
    root = Tk()
    # Gets the requested values of the height and widht.
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry("1280x720".format(position_right, position_down))
    root.resizable(False, False)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    app = MainWindow(root)
    app.mainloop()
