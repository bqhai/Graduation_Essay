__author__ = 'Hai Bui'

from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import babel.numbers
from bll.text_classification import predict, convert_label_to_text
from bll.preprocessor import text_preprocess
from bll.crawler import crawl, count_crawled_post, set_stop_flag
from bll.call_api import *
from threading import Thread
import threading
import subprocess
import validators
import time
import bll.config_log
import logging

# ---Global variable---
list_page_url = []
list_group_url = []
list_user_url = []

username = ''
password = ''


def time_now():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def on_closing():
    if messagebox.askokcancel('Thoát', 'Bạn muốn thoát chứ?'):
        logging.info('Exit')
        root.destroy()


def check_valid_time(minute, hour):
    if not minute.isdigit() or not hour.isdigit():
        return False
    if int(minute) < 0 or int(minute) > 59 or int(hour) < 0 or int(hour) > 24:
        return False
    return True


def check_valid_post_url(url):
    if validators.url(url) and 'facebook.com' in url:
        if 'posts' in url:
            return True
        elif 'groups' in url and 'permalink' in url:
            return True
        else:
            return False
    else:
        return False


def keypress_only_number(c):
    if c.isdigit():
        # print(c)
        return True
    elif c is '':
        # print(c)
        return True
    else:
        # print(c)
        return False


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
        self.parent.title('Công cụ thu thập, phân loại tin tức')
        self.pack(fill=BOTH, expand=1)
        tab_control_m = ttk.Notebook(self)
        tab_control_m.pack(fill=BOTH, expand=1)
        frm_crawler = ttk.Frame(tab_control_m)
        frm_word_tokenizer = ttk.Frame(tab_control_m)
        frm_text_classification = ttk.Frame(tab_control_m)
        tab_control_m.add(frm_crawler, text='   Thu thập dữ liệu   ')
        tab_control_m.add(frm_word_tokenizer, text='   Công cụ tách từ   ')
        tab_control_m.add(frm_text_classification, text='   Phân loại văn bản   ')

        # tab_control_m.add(frm_guild, text='   Hướng dẫn   ')

        # Facebook Crawler area
        def write_runtime_info(message):
            txt_info_cr.config(state=NORMAL)
            txt_info_cr.insert(END, time_now() + '   ' + message + '\n', 'runtime')
            txt_info_cr.config(state=DISABLED)

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

        def login():
            if login_option.get():
                def login_ok():
                    global username
                    global password
                    username = ent_username_lg.get()
                    password = ent_password_lg.get()
                    if len(username) <= 0 or len(password) <= 0:
                        messagebox.showwarning('Thông báo', 'Thông tin đăng nhập không được để trống')
                        return
                    login_option.set(True)
                    win_login.destroy()

                def login_cancel():
                    login_option.set(False)
                    win_login.destroy()

                win_login = Toplevel(self)
                win_login.title('Đăng nhập')
                center_window(win_login, 390, 130)
                win_login.resizable(False, False)
                win_login.grab_set()
                lbl_username_lg = Label(win_login, text='Email hoặc SĐT: ')
                lbl_username_lg.grid(column=0, row=0, sticky='w', padx=15, pady=(15, 0))
                lbl_password_lg = Label(win_login, text='Mật khẩu: ')
                lbl_password_lg.grid(column=0, row=1, sticky='w', padx=15, pady=(15, 0))
                ent_username_lg = ttk.Entry(win_login, width=40)
                ent_username_lg.grid(column=1, row=0, pady=(15, 0))
                ent_password_lg = ttk.Entry(win_login, width=40)
                ent_password_lg.grid(column=1, row=1, pady=(15, 0))
                btn_login_lg = ttk.Button(win_login, text='OK', cursor='hand2', command=login_ok)
                btn_login_lg.grid(column=1, row=2, sticky='w', pady=(15, 0))
                btn_cancel_lg = ttk.Button(win_login, text='Hủy', cursor='hand2', command=login_cancel)
                btn_cancel_lg.grid(column=1, row=2, sticky='w', padx=(80, 0), pady=(15, 0))
                login_option.set(False)
            else:
                global username
                global password
                username = ''
                password = ''
                login_option.set(False)

        def open_watch_list():
            watch_list = get_all_watch_list()
            if watch_list == -2:
                write_error_info('Kết nối server thất bại!')
                root.config(cursor='')
                return
            win_watch_list = Toplevel(self)
            win_watch_list.title('Danh sách theo dõi')
            center_window(win_watch_list, 1200, 480)
            win_watch_list.resizable(False, False)
            win_watch_list.grab_set()
            tab_control_wl = ttk.Notebook(win_watch_list, height=480, width=1200)
            tab_control_wl.pack(expand=1)
            # frm_bottom_wl = Frame(win_watch_list, height=60, width=1200)
            # frm_bottom_wl.pack()
            frm_page_wl = Frame(tab_control_wl)
            frm_group_wl = Frame(tab_control_wl)
            frm_user_wl = Frame(tab_control_wl)
            tab_control_wl.add(frm_page_wl, text='  Page  ')
            tab_control_wl.add(frm_group_wl, text='  Group  ')
            tab_control_wl.add(frm_user_wl, text='  User  ')

            txt_page_wl = Text(frm_page_wl, wrap=WORD)
            txt_page_wl.pack(fill=BOTH, expand=True)
            txt_page_wl.tag_config('pageheader', foreground='red', background='yellow')
            txt_page_wl.insert(END, '{:<50} \t {:<89}'.format('Tên trang', 'URL') + 'Chọn' + '\n', 'pageheader')

            txt_group_wl = Text(frm_group_wl, wrap=WORD)
            txt_group_wl.pack(fill=BOTH, expand=True)
            txt_group_wl.tag_config('groupheader', foreground='red', background='yellow')
            txt_group_wl.insert(END, '{:<50} \t {:89}'.format('Tên nhóm', 'URL') + 'Chọn' + '\n', 'groupheader')

            txt_user_wl = Text(frm_user_wl, wrap=WORD)
            txt_user_wl.pack(fill=BOTH, expand=True)
            txt_user_wl.tag_config('userheader', foreground='red', background='yellow')
            txt_user_wl.insert(END, '{:<50} \t {:<89}'.format('Tên facebook cá nhân', 'URL') + 'Chọn' + '\n', 'userheader')

            def choose_url(url):
                ent_url_cr.delete(0, END)
                ent_url_cr.insert(0, url)
                win_watch_list.destroy()

            def select_page_url(url):
                global list_page_url
                if url not in list_page_url:
                    list_page_url.append(url)
                else:
                    list_page_url.remove(url)
                print(list_page_url)

            def select_group_url(url):
                global list_group_url
                if url not in list_group_url:
                    list_group_url.append(url)
                else:
                    list_group_url.remove(url)
                print(list_group_url)

            def select_user_url(url):
                global list_user_url
                if url not in list_user_url:
                    list_user_url.append(url)
                else:
                    list_user_url.remove(url)
                print(list_user_url)

            for i in watch_list:
                if not i['Status']:
                    pass
                else:
                    if i['FacebookTypeID'] == 'PAGE':
                        txt_page_wl.config(state=NORMAL)
                        txt_page_wl.insert(END, '{:<50} \t {:<89}'.format(i['FacebookName'], i['FacebookUrl']))
                        chk_select_page_wl = Checkbutton(txt_page_wl, cursor='hand2', variable=i['FacebookUrl'], command=lambda url=i['FacebookUrl']: select_page_url(url))
                        btn_choose_url = ttk.Button(txt_page_wl, text='⮜', width=2, cursor='hand2', command=lambda url=i['FacebookUrl']: choose_url(url))
                        txt_page_wl.window_create(txt_page_wl.index('end'), window=chk_select_page_wl)
                        txt_page_wl.window_create(txt_page_wl.index('end'), window=btn_choose_url)
                        txt_page_wl.insert(END, '\n')
                        txt_page_wl.config(state=DISABLED)
                    elif i['FacebookTypeID'] == 'GR':
                        txt_group_wl.config(state=NORMAL)
                        txt_group_wl.insert(END, '{:<50} \t {:<89}'.format(i['FacebookName'], i['FacebookUrl']))
                        chk_select_gr_wl = Checkbutton(txt_group_wl, cursor='hand2', variable=i['FacebookUrl'], command=lambda url=i['FacebookUrl']: select_group_url(url))
                        btn_choose_url = ttk.Button(txt_group_wl, text='⮜', width=2, cursor='hand2', command=lambda url=i['FacebookUrl']: choose_url(url))
                        txt_group_wl.window_create(txt_group_wl.index('end'), window=chk_select_gr_wl)
                        txt_group_wl.window_create(txt_group_wl.index('end'), window=btn_choose_url)
                        txt_group_wl.insert(END, '\n')
                        txt_group_wl.config(state=DISABLED)
                    else:
                        txt_user_wl.config(state=NORMAL)
                        txt_user_wl.insert(END, '{:<50} \t {:<89}'.format(i['FacebookName'], i['FacebookUrl']))
                        chk_select_user_wl = Checkbutton(txt_user_wl, cursor='hand2', variable=i['FacebookUrl'], command=lambda url=i['FacebookUrl']: select_user_url(url))
                        btn_choose_url = ttk.Button(txt_user_wl, text='⮜', width=2, cursor='hand2', command=lambda url=i['FacebookUrl']: choose_url(url))
                        txt_user_wl.window_create(txt_user_wl.index('end'), window=chk_select_user_wl)
                        txt_user_wl.window_create(txt_user_wl.index('end'), window=btn_choose_url)
                        txt_user_wl.insert(END, '\n')
                        txt_user_wl.config(state=DISABLED)

        def open_log():
            subprocess.call(['notepad.exe', 'log/run_time.log'])

        def open_add_to_watch_list(facebook_id, url):
            def cancel_awl():
                write_warning_info('Đã hủy thao tác thu thập dữ liệu')
                win_add_watch_list.destroy()

            def ok_awl():
                facebook_name = ent_facebook_name_awl.get()
                if facebook_type.get() == 'Trang':
                    fb_type = 'PAGE'
                elif facebook_type.get() == 'Nhóm':
                    fb_type = 'GR'
                else:
                    fb_type = 'USER'

                if len(facebook_name) <= 0:
                    messagebox.showwarning('Lỗi', 'Tên không được để trống')
                    return
                watch_list_item = {
                    'FacebookID': facebook_id,
                    'FacebookUrl': url,
                    'FacebookName': facebook_name,
                    'FacebookTypeID': fb_type
                }
                status = add_to_watch_list(watch_list_item)
                if status == 0:
                    win_add_watch_list.destroy()
                    write_success_info('Đã thêm ' + facebook_name + ' vào danh sách theo dõi')
                elif status == -2:
                    messagebox.showerror('Lỗi', 'Kết nối server thất bại')
                    return
                elif status == -4:
                    messagebox.showerror('Lỗi', 'Có lỗi xảy ra phía server')
                    return

            # ---create ui add to watch list ---
            win_add_watch_list = Toplevel(self)
            win_add_watch_list.title('Thêm đối tượng vào danh sách theo dõi')
            center_window(win_add_watch_list, 480, 200)
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

            facebook_type = StringVar(win_add_watch_list)
            choices = ['Trang', 'Nhóm', 'Cá nhân']
            facebook_type.set('Trang')
            ent_facebook_id_awl = ttk.Entry(win_add_watch_list, width=65)
            ent_facebook_id_awl.grid(column=1, row=0, pady=(15, 0))
            ent_facebook_id_awl.insert(0, facebook_id)
            ent_facebook_id_awl.config(state='disabled')
            ent_facebook_url_awl = ttk.Entry(win_add_watch_list, width=65)
            ent_facebook_url_awl.grid(column=1, row=1, pady=(15, 0))
            ent_facebook_url_awl.insert(0, url)
            ent_facebook_url_awl.config(state='disabled')
            ent_facebook_name_awl = ttk.Entry(win_add_watch_list, width=65)
            ent_facebook_name_awl.grid(column=1, row=2, pady=(15, 0))
            ent_facebook_name_awl.insert(0, facebook_id)
            opm_facebook_type_awl = ttk.OptionMenu(win_add_watch_list, facebook_type, choices[0], *choices)
            opm_facebook_type_awl.grid(column=1, row=3, sticky='w', pady=(15, 0))

            btn_add_awl = ttk.Button(win_add_watch_list, text='OK', cursor='hand2', command=ok_awl)
            btn_add_awl.grid(column=1, row=4, sticky='w', pady=(15, 0))
            btn_cancel_awl = ttk.Button(win_add_watch_list, text='Hủy', cursor='hand2', command=cancel_awl)
            btn_cancel_awl.grid(column=1, row=4, sticky='w', padx=(80, 0), pady=(15, 0))

        def thread_start_crawl():
            t = threading.Thread(target=start_crawl)
            t.start()

        def start_crawl():
            url = ent_url_cr.get()
            if len(url) <= 0:
                write_warning_info('Link Facebook trống')
                return
            write_runtime_info('Kiểm tra thông tin url...')
            # check valid url
            if validators.url(url) and 'facebook.com' in url:
                pass
            else:
                write_error_info('Link Facebook không hợp lệ')
                return
            # check valid scroll down
            try:
                scroll_down = int(spn_numpage_cr.get())
                if scroll_down > 20:
                    write_warning_info('Tối đa 20 lần cuộn trang')
                    return
            except EXCEPTION:
                write_error_info('Số lần cuộn trang không hợp lệ')
                return
            selection = int(select_type.get())

            # check exit facebook id in watchlist
            if url.split('/')[-1] == '':
                facebook_id = url.split('/')[-2]
            else:
                facebook_id = url.split('/')[-1]
            status = check_exist_in_watch_list(facebook_id)
            if status:
                pass
            elif status == -2:
                messagebox.showerror('Lỗi', 'Kiểm tra thông tin thất bại, server không phản hồi')
                return
            else:
                msg_box = messagebox.askquestion('Thông báo', 'Url này chưa có trong danh sách theo dõi. Chọn Yes để thêm')
                if msg_box == 'yes':
                    open_add_to_watch_list(facebook_id, url)
                    return
                else:
                    write_warning_info('Đã hủy thao tác thu thập dữ liệu')
                    return
            # check login if selection = 3 (crawl user)
            global username, password
            if selection == 3:
                if not username or not password:
                    write_warning_info('Yêu cầu đăng nhập...')
                    return
            # start crawl data
            btn_crawl_cr['state'] = 'disabled'
            btn_crawl_list_cr['state'] = 'disabled'
            btn_stop_crawl_cr['state'] = 'enable'
            set_stop_flag(False)  # set flag to false -> continue crawl
            write_runtime_info('Đang tiến hành thu thập...')
            try:
                status = crawl(url, scroll_down, selection, username, password)
                if status == 0:
                    write_success_info('Tổng số bài viết thu thập: ' + str(count_crawled_post()))
                elif status == -1:
                    write_error_info('Link Facebook không hợp lệ')
                elif status == -3:
                    write_warning_info('Chức năng này hiện đang trong giai đoạn phát triển')
                elif status == -4:
                    write_error_info('Có lỗi xảy ra ở server')
                elif status == -5:
                    write_warning_info('Hủy')
                else:
                    write_error_info('Kết nối server thất bại')
            except EXCEPTION:
                write_error_info('Thực thi thất bại')
            # status = crawl(url, scroll_down, selection)
            btn_crawl_cr['state'] = 'enable'
            btn_crawl_list_cr['state'] = 'enable'
            btn_stop_crawl_cr['state'] = 'disabled'

        def thread_start_crawl_list():
            t = threading.Thread(target=start_crawl_list)
            t.start()

        def start_crawl_list():
            global list_page_url
            global list_group_url
            global list_user_url
            global username, password
            selection = int(select_type.get())
            if selection == 1:
                list_url = list_page_url
            elif selection == 2:
                list_url = list_group_url
            else:
                if not username or not password:
                    write_warning_info('Yêu cầu đăng nhập...')
                    return
                list_url = list_user_url
            if not list_url:
                write_warning_info('Danh sách thu thập trống')
                return
            try:
                scroll_down = int(spn_numpage_cr.get())
                if scroll_down > 20:
                    write_warning_info('Tối đa 20 lần cuộn trang')
                    return
            except EXCEPTION:
                write_error_info('Số lần cuộn trang không hợp lệ')
                return
            btn_crawl_cr['state'] = 'disabled'
            btn_crawl_list_cr['state'] = 'disabled'
            btn_stop_crawl_cr['state'] = 'enable'
            set_stop_flag(False)  # set flag to false -> continue crawl
            count = 1
            for i in list_url:
                write_runtime_info('Đang thu thập ' + '(' + str(count) + '/' + str(len(list_url)) + ')' + ' URL: ' + i + ' ...')
                try:
                    status = crawl(i, scroll_down, selection, username, password)
                    # show status
                    if status == 0:
                        write_success_info('Tổng số bài viết thu thập: ' + str(count_crawled_post()))
                    elif status == -1:
                        write_warning_info('Link Facebook không hợp lệ')
                    elif status == -4:
                        write_error_info('Có lỗi xảy ra ở server')
                    elif status == -5:
                        write_warning_info('Hủy')
                    else:
                        write_error_info('Kết nối server thất bại')
                except EXCEPTION:
                    write_error_info('Kết nối server thất bại')
                count += 1
            write_success_info('Xong')
            btn_crawl_cr['state'] = 'enable'
            btn_crawl_list_cr['state'] = 'enable'
            btn_stop_crawl_cr['state'] = 'disabled'

        def stop_crawl():
            set_stop_flag(True)  # set flag to true -> stop crawl
            write_runtime_info('Đang hủy tiến trình thu thập dữ liệu...')

        select_type = IntVar()
        login_option = BooleanVar()

        frm_top_cr = ttk.Frame(frm_crawler)
        frm_top_cr.pack(fill=BOTH, padx=15, pady=15)
        lbl_url_cr = Label(frm_top_cr, text='Facebook URL: ')
        lbl_url_cr.grid(column=0, row=0, sticky='e')
        lbl_function_cr = Label(frm_top_cr, text='Chức năng: ')
        lbl_function_cr.grid(column=0, row=3, sticky='e')
        ent_url_cr = ttk.Entry(frm_top_cr, width=120)
        ent_url_cr.grid(column=1, row=0)
        # button to open blacklist
        btn_black_list_cr = ttk.Button(frm_top_cr, text='...', width=5, cursor='hand2', command=open_watch_list)
        btn_black_list_cr.grid(column=2, row=0, padx=(10, 0))
        lbl_numpage_cr = Label(frm_top_cr, text='Số lần cuộn trang: ')
        lbl_numpage_cr.grid(column=3, row=0, padx=(20, 0))
        spn_numpage_cr = ttk.Spinbox(frm_top_cr, from_=1, to=20, width=3)
        spn_numpage_cr.grid(column=4, row=0)
        spn_numpage_cr.insert(1, 1)
        frm_fbtype_cr = ttk.Frame(frm_top_cr)
        frm_fbtype_cr.grid(column=1, row=1, sticky='w', pady=(10, 0))
        rad_page_cr = ttk.Radiobutton(frm_fbtype_cr, text='Page', cursor='hand2', variable=select_type, value=1)
        rad_page_cr.grid(column=0, row=0, padx=(0, 15))
        select_type.set(1)
        rad_group_cr = ttk.Radiobutton(frm_fbtype_cr, text='Group', cursor='hand2', variable=select_type, value=2)
        rad_group_cr.grid(column=1, row=0, padx=(0, 15))
        rad_user_cr = ttk.Radiobutton(frm_fbtype_cr, text='User', cursor='hand2', variable=select_type, value=3)
        rad_user_cr.grid(column=2, row=0, padx=(0, 15))

        chk_login_cr = ttk.Checkbutton(frm_top_cr, text='Đăng nhập (Dùng cho chức năng thu thập từ cá nhân)', variable=login_option, onvalue=True,
                                       offvalue=False, command=login)
        chk_login_cr.grid(column=1, row=2, sticky='w', pady=(10, 0))

        btn_show_log_cr = ttk.Button(frm_top_cr, text='Xem log', cursor='hand2', width=17, command=open_log)
        btn_show_log_cr.grid(column=1, row=3, sticky='w', pady=(10, 0))
        btn_clear_info_cr = ttk.Button(frm_top_cr, text='Xóa thông báo', cursor='hand2', width=17, command=clear_info)
        btn_clear_info_cr.grid(column=1, row=3, sticky='w', padx=(125, 0), pady=(10, 0))
        btn_crawl_cr = ttk.Button(frm_top_cr, text='Thu thập 1 URL', cursor='hand2', width=17, command=thread_start_crawl)
        btn_crawl_cr.grid(column=1, row=4, sticky='w', pady=(10, 0))
        btn_crawl_list_cr = ttk.Button(frm_top_cr, text='Thu thập List URL', cursor='hand2', width=17, command=thread_start_crawl_list)
        btn_crawl_list_cr.grid(column=1, row=4, sticky='w', padx=(125, 0), pady=(10, 0))
        btn_stop_crawl_cr = ttk.Button(frm_top_cr, text='Hủy thu thập', cursor='hand2', width=17, command=stop_crawl)
        btn_stop_crawl_cr.grid(column=1, row=4, sticky='w', padx=(250, 0), pady=(10, 0))
        btn_stop_crawl_cr['state'] = 'disabled'

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
        txt_info_cr.tag_config('runtime', foreground='white')

        # Word Tokenize area
        def get_preprocessor_text():
            txt_output_wt.config(state=NORMAL)
            txt_output_wt.delete('1.0', END)
            txt_output_wt.insert('1.0', text_preprocess(txt_input_wt.get('1.0', END)))
            txt_output_wt.config(state=DISABLED)

        def clear_text_wt():
            txt_input_wt.delete('1.0', END)
            txt_output_wt.config(state=NORMAL)
            txt_output_wt.delete('1.0', END)
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
        btn_clear_wt = ttk.Button(frm_bottom_wt, text='Xóa text', cursor='hand2', command=clear_text_wt)
        btn_clear_wt.pack(side=RIGHT, padx=5, pady=5)

        # Text Classification area
        def save_post():
            def save_post_cancel():
                win_save_post.destroy()

            def save_post_ok():
                post_url = ent_post_url_sp.get()
                user_url = ent_user_url_sp.get()
                post_content = txt_input_tc.get('1.0', END)
                minute = spn_minute_sp.get()
                hour = spn_hour_sp.get()
                like = ent_like_sp.get()
                comment = ent_comment_sp.get()
                share = ent_share_sp.get()
                news_label_id = convert_label_to_text(predict(text_preprocess(post_content)))[0]
                sentiment_label_id = convert_label_to_text(predict(text_preprocess(post_content)))[2]
                # --- check url is null
                if not post_url or not user_url:
                    messagebox.showwarning('Thông báo', 'Hãy nhập đầy đủ thông tin')
                    return
                # check valid post url
                if check_valid_post_url(post_url):
                    pass
                else:
                    messagebox.showwarning('Thông báo', 'Link bài viết không hợp lệ!')
                    return

                if validators.url(user_url) and 'facebook.com' in user_url and 'groups' not in user_url:
                    pass
                else:
                    messagebox.showwarning('Thông báo', 'Link người đăng không hợp lệ!')
                    return
                if not check_valid_time(minute, hour):
                    messagebox.showwarning('Thông báo', 'Thời gian không hợp lệ')
                    return
                facebook_id = user_url.split('/')[3]
                post = {
                    'PostUrl': post_url,
                    'UserUrl': user_url,
                    'PostContent': post_content,
                    'UploadTime': str(cal_date_sp.get_date()) + ' ' + hour + ':' + minute + ':00',
                    'CrawledTime': (datetime.now()).strftime("%Y/%m/%d %H:%M:%S"),
                    'TotalLikes': like,
                    'TotalComment': comment,
                    'TotalShare': share,
                    'FacebookID': facebook_id,
                    'NewsLabelID': news_label_id,
                    'SentimentLabelID': sentiment_label_id
                }
                post_url_check = {
                    'PostUrl': post_url  # to check post url exits in database or not
                }
                status = check_exist_post(post_url_check)
                if status:
                    msg_box = messagebox.askquestion('Thông báo', 'Bài viết này đã được lưu trước đó, bạn muốn cập nhật chứ?')
                    if msg_box == 'yes':
                        if update_json_post(post) == 0:
                            messagebox.showinfo('Thông báo', 'Cập nhật thành công!')
                            win_save_post.destroy()
                        else:
                            messagebox.showerror('Thông báo', 'Cập nhật thất bại')
                            return
                elif status == -2:
                    messagebox.showerror('Lỗi', 'Kiểm tra thông tin thất bại, server không phản hồi!')
                    return
                else:
                    # --- check user exits in watch list ---
                    status = check_exist_in_watch_list(facebook_id)
                    if status:
                        pass
                    elif status == -2:
                        messagebox.showerror('Lỗi', 'Kiểm tra thông tin thất bại, server không phản hồi!')
                        return
                    else:
                        msg_box = messagebox.askquestion('Thông báo', 'Url này chưa có trong danh sách theo dõi. Chọn Yes để thêm!')
                        if msg_box == 'yes':
                            open_add_to_watch_list(facebook_id, user_url)
                            return
                        else:
                            return

                    if add_json_post(post) == 0:
                        messagebox.showinfo('Thông báo', 'Đã thêm bài viết!')
                        win_save_post.destroy()
                    else:
                        messagebox.showerror('Thông báo', 'Thêm bài viết thất bại')
                        return

            if len(txt_input_tc.get('1.0', 'end-1c')) == 0:
                messagebox.showwarning('Thông báo', 'Nội dung trống!')
                return
            if lbl_result1_tc['text'] == '' or lbl_result2_tc['text'] == '':
                messagebox.showwarning('Thông báo', 'Bài viết chưa được phân loại!')
                return
            # --- create ui save post ---
            win_save_post = Toplevel(self)
            win_save_post.title('Lưu bài viết')
            center_window(win_save_post, 854, 230)
            win_save_post.resizable(False, False)
            win_save_post.grab_set()
            reg = win_save_post.register(keypress_only_number)
            # --- left ---
            lbl_post_url_sp = Label(win_save_post, text='URL bài viết: ')
            lbl_post_url_sp.grid(column=0, row=0, sticky='w', padx=15, pady=(15, 0))
            lbl_user_url_sp = Label(win_save_post, text='URL người đăng: ')
            lbl_user_url_sp.grid(column=0, row=1, sticky='w', padx=15, pady=(15, 0))
            lbl_post_time_sp = Label(win_save_post, text='Thời gian đăng: ')
            lbl_post_time_sp.grid(column=0, row=2, sticky='w', padx=15, pady=(15, 0))
            lbl_post_interactive_sp = Label(win_save_post, text='Tương tác: ')
            lbl_post_interactive_sp.grid(column=0, row=3, sticky='w', padx=15, pady=(15, 0))
            # --- right ---
            ent_post_url_sp = ttk.Entry(win_save_post, width=115)
            ent_post_url_sp.grid(column=1, row=0, pady=(15, 0))
            ent_user_url_sp = ttk.Entry(win_save_post, width=115)
            ent_user_url_sp.grid(column=1, row=1, pady=(15, 0))
            # --- upload time ---
            spn_hour_sp = ttk.Spinbox(win_save_post, from_=00, to=23, width=3, validate='key', validatecommand=(reg, '%P'))
            spn_hour_sp.grid(column=1, row=2, sticky='w', pady=(15, 0))
            spn_hour_sp.insert(1, 0)
            lbl_hour_sp = Label(win_save_post, text='giờ')
            lbl_hour_sp.grid(column=1, row=2, sticky='w', padx=(40, 0), pady=(15, 0))
            spn_minute_sp = ttk.Spinbox(win_save_post, from_=00, to=59, width=3, validate='key', validatecommand=(reg, '%P'))
            spn_minute_sp.grid(column=1, row=2, sticky='w', padx=(70, 0), pady=(15, 0))
            spn_minute_sp.insert(1, 0)
            lbl_minute_sp = Label(win_save_post, text='phút')
            lbl_minute_sp.grid(column=1, row=2, sticky='w', padx=(110, 0), pady=(15, 0))
            lbl_date_sp = Label(win_save_post, text='Ngày: ')
            lbl_date_sp.grid(column=1, row=2, sticky='w', padx=(150, 0), pady=(15, 0))
            cal_date_sp = DateEntry(win_save_post, width=12, foreground='white', borderwidth=2)
            cal_date_sp.grid(column=1, row=2, sticky='w', padx=(200, 0), pady=(15, 0))
            # --- interaction ---
            lbl_like_sp = Label(win_save_post, text='Like: ')
            lbl_like_sp.grid(column=1, row=3, sticky='w', pady=(15, 0))
            ent_like_sp = ttk.Entry(win_save_post, width=5, validate='key', validatecommand=(reg, '%P'))
            ent_like_sp.grid(column=1, row=3, sticky='w', padx=(35, 0), pady=(15, 0))
            lbl_comment_sp = Label(win_save_post, text='Comment: ')
            lbl_comment_sp.grid(column=1, row=3, sticky='w', padx=(80, 0), pady=(15, 0))
            ent_comment_sp = ttk.Entry(win_save_post, width=5, validate='key', validatecommand=(reg, '%P'))
            ent_comment_sp.grid(column=1, row=3, sticky='w', padx=(150, 0), pady=(15, 0))
            lbl_share_sp = Label(win_save_post, text='Share: ')
            lbl_share_sp.grid(column=1, row=3, sticky='w', padx=(195, 0), pady=(15, 0))
            ent_share_sp = ttk.Entry(win_save_post, width=5, validate='key', validatecommand=(reg, '%P'))
            ent_share_sp.grid(column=1, row=3, sticky='w', padx=(240, 0), pady=(15, 0))
            # --- ok/cancel button ---
            btn_ok_sp = ttk.Button(win_save_post, text='OK', cursor='hand2', command=save_post_ok)
            btn_ok_sp.grid(column=1, row=4, sticky='w', pady=(15, 0))
            btn_cancel_sp = ttk.Button(win_save_post, text='Hủy', cursor='hand2', command=save_post_cancel)
            btn_cancel_sp.grid(column=1, row=4, sticky='w', padx=(80, 0), pady=(15, 0))

        def get_label():
            if len(txt_input_tc.get('1.0', 'end-1c')) == 0:
                messagebox.showwarning('Thông báo', 'Nội dung trống!')
            else:
                lbl_result1_tc['text'] = convert_label_to_text(predict(txt_input_tc.get('1.0', END)))[1]
                lbl_result2_tc['text'] = convert_label_to_text(predict(txt_input_tc.get('1.0', END)))[3]
                messagebox.showinfo('Thông báo', 'Xong!')

        def clear_text_tc():
            txt_input_tc.delete('1.0', END)
            lbl_result1_tc['text'] = ''
            lbl_result2_tc['text'] = ''

        frm_input_tc = ttk.Frame(frm_text_classification)
        frm_input_tc.pack(fill=BOTH, expand=True)
        lbl_input_tc = Label(frm_input_tc, text='Dữ liệu đầu vào')
        lbl_input_tc.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_input_tc = Text(frm_input_tc, height=35, wrap=WORD)
        txt_input_tc.pack(fill=BOTH, padx=5, pady=5, expand=True)
        frm_output_tc = ttk.Frame(frm_text_classification)
        frm_output_tc.pack(fill=BOTH, expand=True)
        lbl_output1_tc = Label(frm_output_tc, text='Chủ đề:')
        lbl_output1_tc.grid(column=0, row=0, padx=5, pady=5)
        lbl_output2_tc = Label(frm_output_tc, text='Mức độ:')
        lbl_output2_tc.grid(column=0, row=1, padx=5, pady=5)
        lbl_result1_tc = Label(frm_output_tc, fg='red', width=134, justify=LEFT, anchor='w')
        lbl_result1_tc.grid(column=1, row=0, sticky='w', padx=5, pady=5)
        lbl_result2_tc = Label(frm_output_tc, fg='red', width=134, justify=LEFT, anchor='w')
        lbl_result2_tc.grid(column=1, row=1, sticky='w', padx=5, pady=5)

        btn_save_post_tc = ttk.Button(frm_output_tc, text='Lưu', cursor='hand2', command=save_post)
        btn_save_post_tc.grid(column=2, row=1, padx=5, pady=5)
        btn_classification_tc = ttk.Button(frm_output_tc, text='Phân loại', cursor='hand2', command=get_label)
        btn_classification_tc.grid(column=3, row=1, padx=5, pady=5)
        btn_clear_tc = ttk.Button(frm_output_tc, text='Xóa text', cursor='hand2', command=clear_text_tc)
        btn_clear_tc.grid(column=4, row=1, padx=5, pady=5)


if __name__ == '__main__':
    logging.info('Start up')
    root = Tk()
    center_window(root, 1280, 720)
    root.resizable(False, False)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    app = MainWindow(root)
    app.mainloop()
