try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry


# def example1():
#     def print_sel():
#         print(cal.selection_get())
#
#     top = tk.Toplevel(root)
#
#     cal = Calendar(top,
#                    font="Arial 14", selectmode='day',
#                    cursor="hand1", year=2018, month=2, day=5)
#     cal.pack(fill="both", expand=True)
#     ttk.Button(top, text="ok", command=print_sel).pack()
#
#
# def example2():
#     top = tk.Toplevel(root)
#
#     ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
#
#     cal = DateEntry(top, width=12, background='darkblue',
#                     foreground='white', borderwidth=2)
#     cal.pack(padx=10, pady=10)
#
#
# root = tk.Tk()
# s = ttk.Style(root)
# s.theme_use('clam')
#
# ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
# ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)
#
# root.mainloop()
class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
        self.minstr=tk.StringVar(self,'30')

        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2)    # ,state="readonly"
        self.secstr=tk.StringVar(self,'00')
        self.sec = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.secstr,width=2)

        self.last_valueSec = ""
        self.last_value = ""
        self.minstr.trace("w",self.trace_var)
        self.secstr.trace("w",self.trace_varsec)

        self.hour.grid()
        self.min.grid(row=0,column=1)
        self.sec.grid(row=0,column=2)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.minstr.get()

    def trace_varsec(self,*args):
        if self.last_valueSec == "59" and self.secstr.get() == "0":
            self.minstr.set(int(self.minstr.get())+1 if self.minstr.get() !="59" else 0)
            if self.last_value == "59":
                self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_valueSec = self.secstr.get()

root = tk.Tk()
App(root).pack()
root.mainloop()