import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        sd = StringVar()
        ck = StringVar()
        sandwich = Label(window, text = "샌드위치 (5000원)").grid(row = 0, column = 0)
        sd_entry = Entry(window, width=7, textvariable = sd).grid(row = 0, column = 1)
        cake = Label(window, text = "케이크 (20000원)").grid(row=1, column = 0)
        ck_entry = Entry(window, width=7, textvariable = ck).grid(row = 1, column = 1)

        button = Button(window, text = "주문하기", command = lambda:self.send_order(sd.get(), ck.get()))
        button.grid(row=2, column = 0)

    def send_order(self, x1, x2):
        order_text = "{}: ".format(self.name)

        if x1.isdigit() and int(x1) > 0:
                order_text += "샌드위치 (5000원) {}개, ".format(x1)
        if x2.isdigit() and int(x2) > 0:
                order_text += "케이크 (20000원) {}개".format(x2)

        if order_text == "{}: ".format(self.name):
            pass
        else:
            self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
