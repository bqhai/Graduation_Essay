from tkinter import *
from tkinter import ttk

from bll.preprocessor import text_preprocess
from bll.bll_text_classification import predict


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
        tab_control.add(frm_crawler, text='Cào dữ liệu')
        tab_control.add(frm_word_tokenizer, text='Tách từ')
        tab_control.add(frm_text_classification, text='Phân loại văn bản')
        tab_control.add(frm_guild, text='Hướng dẫn')

        # Facebook Crawler area

        # Word Tokenize area

        frm_input_wt = ttk.Frame(frm_word_tokenizer)
        frm_input_wt.grid(column=0, row=0)
        lbl_input_wt = Label(frm_input_wt, text='Dữ liệu đầu vào')
        lbl_input_wt.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_input_wt = Text(frm_input_wt, width=50, height=23, wrap=WORD)
        txt_input_wt.pack(expand=True, padx=5, pady=5)
        frm_output_wt = ttk.Frame(frm_word_tokenizer)
        frm_output_wt.grid(column=1, row=0)
        lbl_output_wt = Label(frm_output_wt, text='Kết quả')
        lbl_output_wt.pack(side=TOP, anchor=N, padx=5, pady=5)
        txt_output_wt = Text(frm_output_wt, width=50, height=23, wrap=WORD)
        txt_output_wt.pack(expand=True, padx=5, pady=5)
        frm_bottom_wt = ttk.Frame(frm_word_tokenizer)
        frm_bottom_wt.grid(column=0, row=1)

        def get_preprocessor_text():
            txt_output_wt.delete('1.0', END)
            txt_output_wt.insert('1.0', text_preprocess(txt_input_wt.get('1.0', END)))

        btn_wt = ttk.Button(frm_bottom_wt, text='Tách từ', command=get_preprocessor_text)
        btn_wt.pack(side=RIGHT, padx=5, pady=5)

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
            lbl_result_tc["text"] = predict(txt_input_tc.get('1.0', END))

        def clear_text():
            txt_input_tc.delete('1.0', END)
            lbl_result_tc["text"] = ''

        btn_tc = ttk.Button(frm_output_tc, text='Phân loại', command=get_label)
        btn_tc.pack(side=RIGHT, padx=5, pady=5)
        btn_clear_tc = ttk.Button(frm_output_tc, text='Xóa text', command=clear_text)
        btn_clear_tc.pack(side=RIGHT, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    root.geometry("840x480")
    root.resizable(False, False)
    app = MainWindow(root)
    root.mainloop()
