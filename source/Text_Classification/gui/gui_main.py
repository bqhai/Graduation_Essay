import os
import logging
from datetime import datetime
import validators
from tkinter import *
from tkinter import ttk, messagebox
from bll.text_classification import predict, convert_label_to_text
from bll.preprocessor import text_preprocess
from bll.crawler import crawl, count_crawled_post


def time_now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Tool thu thập, phân loại tin tức")
        self.pack(fill=BOTH, expand=1)
        tab_control = ttk.Notebook(self)
        tab_control.pack(fill=BOTH, expand=1)
        frm_crawler = ttk.Frame(tab_control)
        frm_word_tokenizer = ttk.Frame(tab_control)
        frm_text_classification = ttk.Frame(tab_control)
        frm_guild = ttk.Frame(tab_control)
        tab_control.add(frm_crawler, text='   Thu thập dữ liệu   ')
        tab_control.add(frm_word_tokenizer, text='   Công cụ tách từ   ')
        tab_control.add(frm_text_classification, text='   Phân loại văn bản   ')
        tab_control.add(frm_guild, text='   Hướng dẫn   ')

        # Facebook Crawler area
        select_type = IntVar()

        frm_top_cr = ttk.Frame(frm_crawler)
        frm_top_cr.pack(fill=BOTH, padx=15, pady=15)
        lbl_url_cr = Label(frm_top_cr, text='Facebook URL: ')
        lbl_url_cr.grid(column=0, row=0)
        ent_url_cr = ttk.Entry(frm_top_cr, width=70)
        ent_url_cr.grid(column=1, row=0)
        btn_black_list_cr = ttk.Button(frm_top_cr, text='...', width=5)  # button to open blacklist
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

        def write_log(message):
            txt_log_cr.config(state=NORMAL)
            txt_log_cr.insert(END, time_now() + '   ' + message + '\n')
            txt_log_cr.config(state=DISABLED)

        def start_crawl():
            url = ent_url_cr.get()
            if len(url) <= 0:
                write_log('Warning: Link FB không được để trống!')
                return

            # check valid url
            if validators.url(url):
                pass
            else:
                write_log('Error: Link FB không hợp lệ!')
                return
            # check valid scroll down
            try:
                scroll_down = int(spn_numpage_cr.get())
            except:
                write_log('Error: Số lần cuộn trang không hợp lệ.')
                return
            selection = int(select_type.get())
            try:
                status = crawl(url, scroll_down, selection)
                if status == 0:
                    write_log('Success: Tổng số bài viết thu thập: ' + str(count_crawled_post()))
                elif status == -1:
                    write_log('Error: Link FB không tồn tại!')
                else:
                    write_log('Error: Kết nối server thất bại!')
            except:
                write_log('Error: Thực thi thất bại!')

        def clear_log():
            txt_log_cr.config(state=NORMAL)
            txt_log_cr.delete('1.0', END)
            txt_log_cr.config(state=DISABLED)

        btn_crawl_cr = ttk.Button(frm_top_cr, text='Thu thập', command=start_crawl)
        btn_crawl_cr.grid(column=1, row=2, sticky='w', pady=(10, 0))
        btn_clear_log_cr = ttk.Button(frm_top_cr, text='Xóa log', command=clear_log)
        btn_clear_log_cr.grid(column=1, row=2, sticky='w', padx=(100, 0), pady=(10, 0))

        prg_cr = ttk.Progressbar(frm_crawler, length=200)
        prg_cr.pack(fill=BOTH)
        frm_term_cr = ttk.Frame(frm_crawler)
        frm_term_cr.pack(fill=BOTH)
        txt_log_cr = Text(frm_term_cr, wrap=WORD, state=DISABLED)
        txt_log_cr.pack(fill=BOTH, expand=True)

        # Word Tokenize area
        frm_input_wt = ttk.Frame(frm_word_tokenizer)
        frm_input_wt.grid(column=0, row=0)
        lbl_input_wt = Label(frm_input_wt, text='Dữ liệu đầu vào')
        lbl_input_wt.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_input_wt = Text(frm_input_wt, width=51, height=23, wrap=WORD)
        txt_input_wt.pack(expand=True, padx=5, pady=5)
        frm_output_wt = ttk.Frame(frm_word_tokenizer)
        frm_output_wt.grid(column=1, row=0)
        lbl_output_wt = Label(frm_output_wt, text='Kết quả')
        lbl_output_wt.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_output_wt = Text(frm_output_wt, width=51, height=23, wrap=WORD)
        txt_output_wt.pack(expand=True, padx=5, pady=5)
        frm_bottom_wt = ttk.Frame(frm_word_tokenizer)
        frm_bottom_wt.grid(column=0, row=1, columnspan=2)

        def get_preprocessor_text():
            txt_output_wt.delete('1.0', END)
            txt_output_wt.insert('1.0', text_preprocess(txt_input_wt.get('1.0', END)))

        btn_wt = ttk.Button(frm_bottom_wt, text='Tách từ', command=get_preprocessor_text)
        btn_wt.pack(side=RIGHT, padx=5, pady=5)
        btn_clear_wt = ttk.Button(frm_bottom_wt, text='Xóa text')
        btn_clear_wt.pack(side=RIGHT, padx=5, pady=5)

        # Text Classification area
        frm_input_tc = ttk.Frame(frm_text_classification)
        frm_input_tc.pack(fill=BOTH, expand=True)
        lbl_input_tc = Label(frm_input_tc, text='Dữ liệu đầu vào')
        lbl_input_tc.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_input_tc = Text(frm_input_tc, height=18, wrap=WORD)
        txt_input_tc.pack(fill=BOTH, padx=5, pady=5, expand=True)
        frm_output_tc = ttk.Frame(frm_text_classification)
        frm_output_tc.pack(fill=BOTH, expand=True)
        lbl_output_tc = Label(frm_output_tc, text='Kết quả:')
        lbl_output_tc.pack(side=LEFT, anchor=N, padx=5, pady=5)
        lbl_result_tc = Label(frm_output_tc, fg='red')
        lbl_result_tc.pack(side=LEFT, anchor=N, padx=5, pady=5)

        def get_label():
            if len(txt_input_tc.get('1.0', END)) <= 0:
                messagebox.showwarning('Thông báo', 'Nội dung trống!')
            else:
                lbl_result_tc["text"] = convert_label_to_text(predict(txt_input_tc.get('1.0', END)))
                messagebox.showwarning('Thông báo', 'Xong!')

        def clear_text():
            txt_input_tc.delete('1.0', END)
            lbl_result_tc["text"] = ''

        btn_tc = ttk.Button(frm_output_tc, text='Phân loại', command=get_label)
        btn_tc.pack(side=RIGHT, padx=5, pady=5)
        btn_clear_tc = ttk.Button(frm_output_tc, text='Xóa text', command=clear_text)
        btn_clear_tc.pack(side=RIGHT, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    # Gets the requested values of the height and widht.
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    # Gets both half the screen width/height and window width/height
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry("850x480".format(position_right, position_down))
    root.resizable(False, False)
    app = MainWindow(root)
    app.mainloop()
