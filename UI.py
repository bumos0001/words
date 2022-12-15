import tkinter
import Word_manage
bgc = "#3D7878"


class UI:
    def __init__(self, word: Word_manage):
        self.word = word
        self.window = tkinter.Tk()
        self.window.title("背單字v3")
        self.window.config(bg=bgc)
        #   畫布
        self.canvas = tkinter.Canvas(bg="white", width=300, height=250)
        self.canvas.grid(padx=20, pady=20, row=0, column=0, columnspan=3)
        self.Eng_text = self.canvas.create_text(150, 75, width=300, text="123", fill=bgc, font=("Arial", 20, "italic"))
        self.Che_text = self.canvas.create_text(150, 200, width=300, text="", fill="black",
                                                font=("Arial", 18, "italic"))
        # 按鈕 勾
        photo = tkinter.PhotoImage(file="images/true.png")
        self.good = tkinter.Button(text="會了", width=70, height=70, image=photo, command=self.yes)
        self.good.grid(padx=20, pady=15, row=1, column=2)
        # 按鈕 看中文
        self.look_che = tkinter.Button(text="看中文", width=8, height=4, command=self.look)
        self.look_che.grid(padx=20, pady=15, row=1, column=1)
        # 按鈕 叉
        photo2 = tkinter.PhotoImage(file="images/false.png")
        self.bad = tkinter.Button(text="不會", width=70, height=70, image=photo2, command=self.no)
        self.bad.grid(padx=20, pady=15, row=1, column=0)
        self.word.next_word()
        self.canvas.itemconfig(self.Eng_text, text=self.word.Eng)

        self.window.mainloop()

    def yes(self):
        self.word.word_book.pop(self.word.Eng)
        if self.word.next_word():
            self.canvas.itemconfig(self.Eng_text, text=self.word.Eng)
            self.canvas.itemconfig(self.Che_text, text="")
        else:
            self.canvas.itemconfig(self.Eng_text, text="End! No word~~~~ Automatically shuts off after 1 second")
            self.window.after(1000, self.end)

    def no(self):
        self.word.word_book.pop(self.word.Eng)
        self.word.Wrong_word_book[self.word.Eng] = self.word.Che
        self.word.next_word()
        self.canvas.itemconfig(self.Eng_text, text=self.word.Eng)
        self.canvas.itemconfig(self.Che_text, text="")

    def look(self):
        self.canvas.itemconfig(self.Che_text, text=self.word.Che)

    def end(self):
        self.window.destroy()
