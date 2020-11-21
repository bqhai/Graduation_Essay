from tkinter import *
from preprocessor import text_preprocess


class WordTokenizer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Word Tokenizer")
        self.pack(fill=BOTH, expand=1)

        frame_input = Frame(self)
        frame_input.pack(fill=BOTH, expand=True)

        lbl_input = Label(frame_input, text="Text:", width=6)
        lbl_input.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt_input = Text(frame_input)
        txt_input.pack(fill=BOTH, padx=5, pady=5, expand=True)

        frame_output = Frame(self)
        frame_output.pack(fill=BOTH, expand=True)

        lbl_output = Label(frame_output, text="Result:", width=6)
        lbl_output.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt_output = Text(frame_output)
        txt_output.pack(fill=BOTH, padx=5, pady=5, expand=True)

        def get_preprocessor_text():
            txt_output.delete("1.0", END)
            txt_output.insert("1.0", text_preprocess(txt_input.get("1.0", END)))
        analysis_button = Button(self, text="Word Tokenizer", command=get_preprocessor_text)
        analysis_button.pack(side=RIGHT, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    root.geometry("680x950+600+50")
    app = WordTokenizer(root)
    root.mainloop()
