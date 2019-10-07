import requests
from tkinter import *

root = Tk()


#congiguring base window
root.title("Recipe Finder (Recipepupy)")
root.config(bg = "#1F6377")
root.geometry("300x350")
root.columnconfigure(0, weight = 3)
root.rowconfigure(0, weight = 3)


#setting title label
lblttl = Label(root, text = "Recipe Finder", bg = "#1F6377", fg = "#9FC5C9", font=("Times", 30), anchor = "center")
lblttl.pack()


#creating first text text input
txtfir = Text(root)
txtfir.config(font = ("Times", 12), relief = "flat", width = 20, height = 5, bg = "#BADADD", borderwidth = 10)
txtfir.pack(pady = 10)


def on_entry_click_start(event):
    if txtfir.get(1.0, END)[:32] == 'Ingredients (separated by comma)':
        txtfir.delete(1.0, END)
        txtfir.insert(END, '')
        txtfir.config(fg = 'black')
def on_focusout_start(event):
    if len(txtfir.get(1.0, END)) == 1:
        txtfir.insert(END, 'Ingredients (separated by comma)')
        txtfir.config(fg = 'grey')

txtfir.delete(1.0, END)
txtfir.insert(1.0, 'Ingredients (separated by comma)')
txtfir.bind('<FocusIn>', on_entry_click_start)
txtfir.bind('<FocusOut>', on_focusout_start)
txtfir.config(fg = 'grey')


#creating second text label
txtsec = Text(root)
txtsec.config(font = ("Times", 12), relief = "flat", width = 20, height = 5, bg = "#BADADD", borderwidth = 10)
txtsec.pack(pady = 20)

def on_entry_click_start(event):
    if txtsec.get(1.0, END)[:12] == 'Name of Dish':
        txtsec.delete(1.0, END)
        txtsec.insert(END, '')
        txtsec.config(fg = 'black')
def on_focusout_start(event):
    if len(txtsec.get(1.0, END)) == 1:
        txtsec.insert(END, 'Name of Dish')
        txtsec.config(fg = 'grey')

txtsec.delete(1.0, END)
txtsec.insert(1.0, 'Name of Dish')
txtsec.bind('<FocusIn>', on_entry_click_start)
txtsec.bind('<FocusOut>', on_focusout_start)
txtsec.config(fg = 'grey')


#taking input & execution catalyst

lblExec = Label(root, text = "find recipe", font = 40, background = "#363A4C", width = 100, foreground = "white", borderwidth = 2)
lblExec.pack()
#root.bind('<Return>', runExe)

'''
myrequest = requests.get("http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=1")
datajson = myrequest.json()

results = datajson['results'][0]
title = results['title']
ingredients = results['ingredients']

ofile = open("newtesting.html","w")

ofile.write("<h1>" + title + "</h1>")
ofile.write("<p>" + ingredients + "</p>")

#ofile.write("<p>" + ingredients + "</p>")
ofile.close()
'''
mainloop()
