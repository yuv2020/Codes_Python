from tkinter import *
root = Tk()
root.geometry("500 * 300")

Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmethod = Label(root, text="Payment method")

root.mainloop()
