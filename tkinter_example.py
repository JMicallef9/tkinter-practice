import tkinter as tk
from tkinter import ttk

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Test App")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.entry.bind("<Return>", self.add_to_list)

        self.entry_btn = ttk.Button(self, text="Add", command=self.add_to_list)
        self.entry_btn.grid(row=0, column=1)
    
    def add_to_list(self, event=None):
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)


if __name__() == "__main__":
    main()


# def add_to_list(entry, listbox):
#     text = entry.get()
#     if text:
#         listbox.insert(tk.END, text)
#         entry.delete(0, tk.END)







# frame2 = tk.Frame(root)
# frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# frame2.columnconfigure(0, weight=1)
# frame2.rowconfigure(1, weight=1)

# entry2 = tk.Entry(frame2)
# entry2.grid(row=0, column=0, sticky="ew")

# text_list2 = tk.Listbox(frame2)
# text_list2.grid(row=1, column=0, columnspan=2, sticky="nsew")

# entry2.bind("<Return>", lambda event: add_to_list(entry2, text_list2))

# entry_btn2 = tk.Button(frame2, text="Add", command=lambda: add_to_list(entry2, text_list2))
# entry_btn2.grid(row=0, column=1)

# root.mainloop()
