import sys
from datetime import datetime
import os
import csv
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

date = datetime.now().strftime("%Y-%m-%d")

fieldnames = ('Product', 'Quantity', 'Price')


class SalesRecorder:
    def __init__(self, filename='guitar_sales_data.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.create_csv()

    def create_csv(self):
        # Create a new CSV file with headers if it doesn't exist
        with open(self.filename, mode='a') as file:
            csv_writer = csv.writer(file, delimiter=';')
            csv_writer.writerow(['Date', 'Product', 'Spent' 'Sold', 'Net profit'])

    def add_sale(self, product, spent, sold):
        net_profit = int(sold) - int(spent)
        new_sale = [date, product, spent, sold, net_profit]

        with open(self.filename, mode='a',  newline='', encoding='cp1251') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            csv_writer.writerow(new_sale)


def make_widgets(recorder):
    window = Tk()
    window.title('Sales Tracker')
    window.geometry("400x300")
    font = ("Times New Roman", 12)

    label = Label(window, text="Enter product's name: ", font=font)
    label.pack(side=TOP)

    product = Entry(window, width=40, font=font)
    product.pack(side=TOP)

    label = Label(window, text="How many money was spend: ", font=font)
    label.pack(side=TOP)

    spent_field = Entry(window, width=40, font=font)
    spent_field.pack(side=TOP)

    label = Label(window, text="Sold: ", font=font)
    label.pack(side=TOP)

    sold_field = Entry(window, width=40, font=font)
    sold_field.pack(side=TOP)

    def add_to_database():
        product_value = product.get()
        spent_value = spent_field.get()
        sold_value = sold_field.get()

        if product_value and spent_value and sold_value:
            if spent_value.isdigit() and sold_value.isdigit():
                recorder.add_sale(product.get(), spent_field.get(), sold_field.get())
                showinfo(title="Success", message="Sale added to database!")
                clear_fields()
            else:
                showerror(title="Error", message="Spend and Sold fields must be digits")

        else:
            showerror(title="Error", message="All fields must be filled")

    def clear_fields():
        product.delete(0, END)
        spent_field.delete(0, END)
        sold_field.delete(0, END)

    btn = Button(window, text="Add to database", command=add_to_database, font=font)

    btn.pack()
    return window


def main():
    recorder = SalesRecorder()
    #recorder.create_csv()

    #recorder.add_sale('Guitar', 1, 2000)
    print(f"Sales data recorded in {recorder.filename}")

    window = make_widgets(recorder)
    window.mainloop()


if __name__ == "__main__":
    main()

