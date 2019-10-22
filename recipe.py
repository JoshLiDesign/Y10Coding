#import requests
import json
import random
from tkinter import *

root = Tk()


#base window
root.title("Recipe Finder (Food2Fork)")
root.config(bg = "#1F6377")
root.geometry("410x280")
root.columnconfigure(0, weight = 3)
root.rowconfigure(0, weight = 3)


#title label
lblttl = Label(root, text = "Recipe Finder", bg = "#1F6377", fg = "white", font=("Times", 30), anchor = "center")
lblttl.pack()


#first text label
lblfir = Label(root, text = "Enter Ingredients", bg = "#1F6377", fg = "#BADADD", font=("Times", 12), anchor = "center")
lblfir.pack(pady = 5)


#first text input
txtfir = Text(root)
txtfir.config(font = ("Times", 12), relief = "flat", width = 20, height = 5, bg = "#BADADD", borderwidth = 10)
txtfir.pack()

#disappearing text prompt within text field
def on_entry_click_start(event):
    if txtfir.get(1.0, END)[:18] == 'separated by comma':
        txtfir.delete(1.0, END)
        txtfir.insert(END, '')
        txtfir.config(fg = 'black')
def on_focusout_start(event):
    if len(txtfir.get(1.0, END)) == 1:
        txtfir.insert(END, 'separated by comma')
        txtfir.config(fg = 'grey')

txtfir.delete(1.0, END)
txtfir.insert(1.0, 'separated by comma')
txtfir.bind('<FocusIn>', on_entry_click_start)
txtfir.bind('<FocusOut>', on_focusout_start)
txtfir.config(fg = 'grey')

#spacer
lbla = Label(root, text = "", bg = "#1F6377", fg = "#BADADD", font=("Times", 8), anchor = "center")
lbla.pack()


########main function########
def runExe(*args):
    #clear document
    ofile = open("site.html", "w")
    ofile.write("")
    ofile.close()
    
    #initialize css
    ofile = open("site.html","a")
    ofile.write("<!DOCTYPE html><html><head>")
    ofile.write("<link rel='stylesheet' href='style.css'>")
    ofile.write("<link href='https://fonts.googleapis.com/css?family=Quicksand&display=swap' rel='stylesheet'>")
    ofile.write("</head>")

    #randomized rows of recipes
    x = random.randint(2,4)
    
    #title text
    ofile.write("<body>")
    ofile.write("<center><div class = 'fonttop' style = 'margin-top: 54px'><span style='color:red'>"+str(x*3)+" </span>")
    ofile.write("Possible Recipes with <span style='color:red'>"+txtfir.get(1.0, END)+"</span> by popularity </div></centre>")
    
    #myrequest = requests.get("https://www.food2fork.com/api/search?key=25a8e1457d1e279b84de46e340370714&q="+txtfir.get(1.0, END))
    #datajson = myrequest.json()

    #parse json file
    datajson = ""
    with open('sourcecode.json') as f:
        datajson = json.load(f)

    ofile.write("<div class='row'>")

    if (response.status_code = 200):
        
        for j in range(x):
            for i in range(3):
                #access elements
                results = datajson['recipes'][j*3+i]
                publisher = results['publisher']
                title = results['title']
                image = results['image_url']
                source = results['source_url']
                publisher = results['publisher']

                #structure
                ofile.write("<div class = 'column'>")
                ofile.write("<div class = 'fontbod'>")
                #popularity rank
                ofile.write("<h1 style='color: red; font-size = 40px'>"+ str(j*3+i+1) + "</h1>")
                #title of recipe
                ofile.write("<h2 style='font-size = 15px'>"+ title + "</h2>")
                #image with hover overlay and link
                ofile.write("<div class='container'>")
                ofile.write("<a href="+source+" target='_blank'>")
                ofile.write("<img src="+image+" class = 'imgborder image' style='width:300px; height:300px;'>")
                ofile.write("<div class='overlay'>")
                ofile.write("<div class='text'>"+publisher+"</div>")
                ofile.write("</div>")
                ofile.write("</a>")
                ofile.write("</div>")
                ofile.write("</div>")
                ofile.write("</div>")
        
        ofile.write("</body>")
        ofile.write("</html>")
        ofile.close()

    else:
        ofile.write("<h1> An error has occured while processing this data </h1>")

#input & execution catalyst
lblExec = Label(root, text = "find recipe", font = 40, background = "#363A4C", width = 100, foreground = "white", borderwidth = 2)
lblExec.config(relief = GROOVE)
lblExec.pack(padx = 100, pady = 20)
root.bind('<Return>', runExe)
lblExec.bind("<Button-1>", runExe)

#clarification label
lblcla = Label(root, text = "Randomized selection of 6, 9 or 12 recipes", bg = "#1F6377", fg = "white", font=("Times", 10), anchor = "center")
lblcla.pack()

mainloop()
