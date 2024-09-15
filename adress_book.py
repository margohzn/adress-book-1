from tkinter import * 


window = Tk()
window.title("Adress Book")
window.geometry("500x500")


left_frame = Frame(window)

title = Label(left_frame, text = "My address book:", font = ("times", 20)).grid(row = 1, column = 1)
listbox = Listbox(left_frame, width = 30, height = 20)
edit_button = Button(left_frame, text = "Edit", font = ("times", 17)).grid(row = 3, column = 1)
delete_button = Button(left_frame, text = "Delete")

listbox.grid(row = 2, column = 1, columnspan = 2, pady = 10, padx = 10)


left_frame.grid(row = 1, column = 1)





window.mainloop()