__author__ = 'Hai Bui'

from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from bll.text_classification import predict, convert_label_to_text
from bll.preprocessor import text_preprocess
from bll.crawler import crawl, count_crawled_post
from bll.call_api import *
import subprocess
import validators
import bll.config_log
import logging


# ---Global variable---
# username = ''
# password = ''


def time_now():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def on_closing():
    if messagebox.askokcancel('Thoát', 'Bạn muốn thoát chứ?'):
        logging.info('Exit')
        root.destroy()


def center_window(window, w=300, h=200):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title('Tool thu thập, phân loại tin tức')
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

        # def login():
        #     if login_option.get():
        #         def login_ok():
        #             global username
        #             global password
        #             username = ent_username_lg.get()
        #             password = ent_password_lg.get()
        #             if len(username) <= 0 or len(password) <= 0:
        #                 messagebox.showwarning('Thông báo', 'Thông tin đăng nhập không được để trống')
        #                 return
        #             login_option.set(True)
        #             win_login.destroy()
        #
        #         def login_cancel():
        #             login_option.set(False)
        #             win_login.destroy()
        #
        #         win_login = Toplevel(self)
        #         win_login.title('Đăng nhập')
        #         win_login.geometry('390x150')
        #         win_login.resizable(False, False)
        #         win_login.grab_set()
        #         lbl_username_lg = Label(win_login, text='Email hoặc SĐT: ')
        #         lbl_username_lg.grid(column=0, row=0, sticky='w', padx=15, pady=(15, 0))
        #         lbl_password_lg = Label(win_login, text='Mật khẩu: ')
        #         lbl_password_lg.grid(column=0, row=1, sticky='w', padx=15, pady=(15, 0))
        #         ent_username_lg = ttk.Entry(win_login, width=40)
        #         ent_username_lg.grid(column=1, row=0, pady=(15, 0))
        #         ent_password_lg = ttk.Entry(win_login, width=40)
        #         ent_password_lg.grid(column=1, row=1, pady=(15, 0))
        #         btn_login_lg = ttk.Button(win_login, text='OK', cursor='hand2', command=login_ok)
        #         btn_login_lg.grid(column=1, row=2, sticky='w', pady=(15, 0))
        #         btn_cancel_lg = ttk.Button(win_login, text='Hủy', cursor='hand2', command=login_cancel)
        #         btn_cancel_lg.grid(column=1, row=2, sticky='w', padx=(80, 0), pady=(15, 0))
        #         login_option.set(False)
        #     else:
        #         global username
        #         global password
        #         username = ''
        #         password = ''
        #         login_option.set(False)

        def open_watch_list():
            black_list = get_all_black_list()
            if black_list == -2:
                write_error_info('Kết nối server thất bại!')
                root.config(cursor='')
                return
            win_watch_list = Toplevel(self)
            win_watch_list.title('Danh sách theo dõi')
            win_watch_list.geometry('854x480')
            win_watch_list.resizable(False, False)
            win_watch_list.grab_set()
            tab_control_wl = ttk.Notebook(win_watch_list)
            tab_control_wl.pack(fill=BOTH, expand=1)
            frm_page_wl = Frame(tab_control_wl)
            frm_group_wl = Frame(tab_control_wl)
            frm_user_wl = Frame(tab_control_wl)
            tab_control_wl.add(frm_page_wl, text='  Page  ')
            tab_control_wl.add(frm_group_wl, text='  Group  ')
            tab_control_wl.add(frm_user_wl, text='  User  ')

            txt_page_wl = Text(frm_page_wl, wrap=WORD, state=DISABLED)
            txt_page_wl.pack(fill=BOTH, expand=True)
            txt_page_wl.tag_config('header', foreground='red', background='yellow')
            # global black_list
            # if len(black_list) <= 0:
            #     black_list = get_all_black_list()
            txt_page_wl.config(state=NORMAL)
            txt_page_wl.insert(END, '{:<35} \t {:<12}'.format('Tên trang', 'URL') + '\n', 'header')
            for i in black_list:
                txt_page_wl.insert(END, '{:<35} \t {:<12}'.format(i['FacebookName'], i['FacebookUrl']) + '\n')
            txt_page_wl.config(state=DISABLED)

        def open_log():
            subprocess.call(['notepad.exe', '../log/run_time.log'])

        def open_add_to_watch_list(facebook_id, url):
            win_add_watch_list = Toplevel(self)
            win_add_watch_list.title('Thêm đối tượng vào danh sach theo dõi')
            win_add_watch_list.geometry('480x200')
            win_add_watch_list.resizable(False, False)
            win_add_watch_list.grab_set()
            lbl_facebook_id_awl = Label(win_add_watch_list, text='ID: ')
            lbl_facebook_id_awl.grid(column=0, row=0, sticky='w', padx=15, pady=(15, 0))
            lbl_facebook_url_awl = Label(win_add_watch_list, text='Url: ')
            lbl_facebook_url_awl.grid(column=0, row=1, sticky='w', padx=15, pady=(15, 0))
            lbl_facebook_name_awl = Label(win_add_watch_list, text='Tên: ')
            lbl_facebook_name_awl.grid(column=0, row=2, sticky='w', padx=15, pady=(15, 0))
            lbl_facebook_type_awl = Label(win_add_watch_list, text='Loại: ')
            lbl_facebook_type_awl.grid(column=0, row=3, sticky='w', padx=15, pady=(15, 0))

            ent_facebook_id_awl = ttk.Entry(win_add_watch_list, width=55)
            ent_facebook_id_awl.grid(column=1, row=0, pady=(15, 0))
            ent_facebook_id_awl.insert(0, facebook_id)
            ent_facebook_id_awl.config(state='disabled')
            ent_facebook_url_awl = ttk.Entry(win_add_watch_list, width=55)
            ent_facebook_url_awl.grid(column=1, row=1, pady=(15, 0))
            ent_facebook_url_awl.insert(0, url)
            ent_facebook_url_awl.config(state='disabled')
            ent_facebook_name_awl = ttk.Entry(win_add_watch_list, width=55)
            ent_facebook_name_awl.grid(column=1, row=2, pady=(15, 0))

        def start_crawl():
            url = ent_url_cr.get()
            if len(url) <= 0:
                write_warning_info('Link FB không được để trống!')
                return
            # check valid url
            if validators.url(url) and 'facebook.com' in url:
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

            # check exit facebook id in watchlist
            facebook_id = url.split('/')[-2]
            status = check_exist_facebook_id(facebook_id)
            if status:
                pass
            elif status == -2:
                messagebox.showerror('Lỗi', 'Kiểm tra thông tin thất bại, server không phản hồi!')
                return
            else:
                open_add_to_watch_list(facebook_id, url)
                return

            # start crawl data
            try:
                status = crawl(url, scroll_down, selection)
                if status == 0:
                    write_success_info('Tổng số bài viết thu thập: ' + str(count_crawled_post()))
                elif status == -1:
                    write_error_info('Link FB không tồn tại!')
                elif status == -3:
                    write_warning_info('Chức năng này hiện đang trong giai đoạn phát triển!')
                elif status == -4:
                    write_error_info('Có lỗi xảy ra ở server!')
                else:
                    write_error_info('Kết nối server thất bại!')
            except:
                write_error_info('Thực thi thất bại!')
            # status = crawl(url, scroll_down, selection)

        select_type = IntVar()
        # login_option = BooleanVar()

        frm_top_cr = ttk.Frame(frm_crawler)
        frm_top_cr.pack(fill=BOTH, padx=15, pady=15)
        lbl_url_cr = Label(frm_top_cr, text='Facebook URL: ')
        lbl_url_cr.grid(column=0, row=0)
        ent_url_cr = ttk.Entry(frm_top_cr, width=120)
        ent_url_cr.grid(column=1, row=0)
        # button to open blacklist
        btn_black_list_cr = ttk.Button(frm_top_cr, text='...', width=5, cursor='hand2', command=open_watch_list)
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

        # chk_login_cr = ttk.Checkbutton(frm_top_cr, text='Đăng nhập', variable=login_option, onvalue=True,
        #                                offvalue=False, command=login)
        # chk_login_cr.grid(column=1, row=2, sticky='w', pady=(10, 0))

        btn_crawl_cr = ttk.Button(frm_top_cr, text='Thu thập', cursor='hand2', command=start_crawl)
        btn_crawl_cr.grid(column=1, row=3, sticky='w', pady=(10, 0))
        btn_show_log_cr = ttk.Button(frm_top_cr, text='Xem log', cursor='hand2', command=open_log)
        btn_show_log_cr.grid(column=1, row=3, sticky='w', padx=(100, 0), pady=(10, 0))
        btn_clear_info_cr = ttk.Button(frm_top_cr, text='Xóa thông báo', cursor='hand2', command=clear_info)
        btn_clear_info_cr.grid(column=1, row=3, sticky='w', padx=(200, 0), pady=(10, 0))

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
        def save_post():
            def save_post_cancel():
                win_save_post.destroy()

            if len(txt_input_tc.get('1.0', 'end-1c')) == 0:
                messagebox.showwarning('Thông báo', 'Nội dung trống!')
                return
            if lbl_result_tc['text'] == '':
                messagebox.showwarning('Thông báo', 'Bài viết chưa được phân loại!')
                return
            win_save_post = Toplevel(self)
            win_save_post.title('Lưu bài viết')
            center_window(win_save_post, 854, 230)
            win_save_post.resizable(False, False)
            win_save_post.grab_set()
            lbl_post_url_sp = Label(win_save_post, text='URL bài viết: ')
            lbl_post_url_sp.grid(column=0, row=0, sticky='w', padx=15, pady=(15, 0))
            lbl_user_url_sp = Label(win_save_post, text='URL người đăng: ')
            lbl_user_url_sp.grid(column=0, row=1, sticky='w', padx=15, pady=(15, 0))
            lbl_profile_name_sp = Label(win_save_post, text='Tên người đăng: ')
            lbl_profile_name_sp.grid(column=0, row=2, sticky='w', padx=15, pady=(15, 0))
            lbl_post_time_sp = Label(win_save_post, text='Thời gian đăng: ')
            lbl_post_time_sp.grid(column=0, row=3, sticky='w', padx=15, pady=(15, 0))

            ent_post_url_sp = ttk.Entry(win_save_post, width=110)
            ent_post_url_sp.grid(column=1, row=0, pady=(15, 0))
            ent_user_url_sp = ttk.Entry(win_save_post, width=110)
            ent_user_url_sp.grid(column=1, row=1, pady=(15, 0))
            ent_profile_name_sp = ttk.Entry(win_save_post, width=110)
            ent_profile_name_sp.grid(column=1, row=2, pady=(15, 0))
            spn_hour_sp = ttk.Spinbox(win_save_post, from_=00, to=23, width=3)
            spn_hour_sp.grid(column=1, row=3, sticky='w', pady=(15, 0))
            spn_hour_sp.insert(1, 0)
            lbl_hour_sp = Label(win_save_post, text='giờ')
            lbl_hour_sp.grid(column=1, row=3, sticky='w', padx=(40, 0), pady=(15, 0))
            spn_minute_sp = ttk.Spinbox(win_save_post, from_=00, to=59, width=3)
            spn_minute_sp.grid(column=1, row=3, sticky='w', padx=(70, 0), pady=(15, 0))
            spn_minute_sp.insert(1, 0)
            lbl_minute_sp = Label(win_save_post, text='phút')
            lbl_minute_sp.grid(column=1, row=3, sticky='w', padx=(110, 0), pady=(15, 0))
            lbl_date_sp = Label(win_save_post, text='Ngày: ')
            lbl_date_sp.grid(column=1, row=3, sticky='w', padx=(150, 0), pady=(15, 0))
            cal_date_sp = DateEntry(win_save_post, width=12, foreground='white', borderwidth=2)
            cal_date_sp.grid(column=1, row=3, sticky='w', padx=(200, 0), pady=(15, 0))
            btn_ok_sp = ttk.Button(win_save_post, text='OK', cursor='hand2')
            btn_ok_sp.grid(column=1, row=4, sticky='w', pady=(15, 0))
            btn_cancel_sp = ttk.Button(win_save_post, text='Hủy', cursor='hand2', command=save_post_cancel)
            btn_cancel_sp.grid(column=1, row=4, sticky='w', padx=(80, 0), pady=(15, 0))

        def get_label():
            if len(txt_input_tc.get('1.0', 'end-1c')) == 0:
                messagebox.showwarning('Thông báo', 'Nội dung trống!')
            else:
                lbl_result_tc['text'] = convert_label_to_text(predict(txt_input_tc.get('1.0', END)))
                messagebox.showinfo('Thông báo', 'Xong!')

        def clear_text():
            txt_input_tc.delete('1.0', END)
            lbl_result_tc['text'] = ''

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

        btn_save_post_tc = ttk.Button(frm_output_tc, text='Lưu', cursor='hand2', command=save_post)
        btn_save_post_tc.pack(side=RIGHT, padx=5, pady=5)
        btn_classification_tc = ttk.Button(frm_output_tc, text='Phân loại', cursor='hand2', command=get_label)
        btn_classification_tc.pack(side=RIGHT, padx=5, pady=5)
        btn_clear_tc = ttk.Button(frm_output_tc, text='Xóa text', cursor='hand2', command=clear_text)
        btn_clear_tc.pack(side=RIGHT, padx=5, pady=5)


if __name__ == '__main__':
    logging.info('Start up')
    root = Tk()
    center_window(root, 1280, 720)
    root.resizable(False, False)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    app = MainWindow(root)
    app.mainloop()
