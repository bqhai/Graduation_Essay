from tkinter import *
import gui_word_tokenizer
import gui_text_classification


def open_word_tokenizer():
    win_1 = Toplevel(root)
    gui_word_tokenizer.WordTokenizer(win_1)
    return


def open_text_classification():
    win_2 = Toplevel(root)
    gui_text_classification.TextClassification(win_2)
    return


if __name__ == "__main__":
    root = Tk()
    root.title("Main")
    root.minsize(100, 100)
    root.geometry("300x200+600+50")
    btn_word_tokenizer = Button(root, text="Open Tokenizer", command=open_word_tokenizer)
    btn_word_tokenizer.pack(side=LEFT, padx=5, pady=5)
    btn_text_classification = Button(root, text="Open Classification", command=open_text_classification)
    btn_text_classification.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
