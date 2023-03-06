from tkinter import *
import os


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "Выбран уровень: "
        self.lbl = Label(text=self.formula, font=("Bahnschrift SemiBold", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "Уровень 1", "Уровень 2", "Уровень 3", 
            "О_О"
        ]

        x = 10
        y = 130
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Bahnschrift SemiBold", 15),
                   command=com).place(x=x, y=y,
                                      width=150,
                                      height=79)
            x += 160
            if x > 400:
                x = 170
                y += 100

    def logicalc(self, operation):
        if operation == "Уровень 1":
            self.formula = "Выбран уровень: Уровень 1"
            os.system('python pygame_zero_game.py')
        elif operation == "Уровень 2":
            self.formula = "Выбран уровень: Уровень 2"
        elif operation == "Уровень 3":
            self.formula = "Выбран уровень: Уровень 3"
        elif operation == "О_О":
            self.formula = "Ты бессмертный что ли?"
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x320+200+200")
    root.title("")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()