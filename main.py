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
    def __init__(self, filename='sales_data.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.create_csv()

    def create_csv(self):
        # Create a new CSV file with headers if it doesn't exist
        with open(self.filename, mode='a') as file:
            csv_writer = csv.writer(file, delimiter=';')
            csv_writer.writerow(['Date', 'Product', 'Quantity', 'Price', 'Total'])

    def add_sale(self, product, quantity, price):
        total = quantity * price
        new_sale = [date, product, quantity, price, total]

        with open(self.filename, mode='a') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            csv_writer.writerow(new_sale)


def main():
    recorder = SalesRecorder()
    #recorder.create_csv()

    #recorder.add_sale('Guitar', 1, 2000)
    print(f"Sales data recorded in {recorder.filename}")

    def reply(name):
        showinfo(title="Reply", message="Hello % s!" % name)

    window = Tk()
    window.title('Sales Tracker')

    label = Label(window, text="Enter product's name: ")
    label.pack(side=TOP)

    product = Entry(window)
    product.pack(side=TOP)

    quantity = Entry(window)
    quantity.pack(side=TOP)

    price = Entry(window)
    price.pack(side=TOP)
   # recorder.add_sale(item, quantity, price)
    btn = Button(window, text="Add to database", command=(lambda: reply(product.get())))
    btn.pack(side=LEFT)

    window.mainloop()


# Example usage
if __name__ == "__main__":
    main()

