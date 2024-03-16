import os
from tkinter import *
from tkinter import font
from tkinter.colorchooser import *
from tkinter.messagebox import *
from tkinter.filedialog import *

#this is font_color function
def font_color():
    #color=colorchooser.askcolor(title="pick a color for your text")
    #text_area.config(fg=color[1])
    text_area.config(fg=askcolor(title="pick a color for your text")[1])

#this is font change function

def change_font(*args):
    text_area.config(font=(font_name.get(),font_size.get()))

def newfile():
    window.title("Untitle")
    text_area.delete("1.0",END)

def openfile():
    filepath=askopenfilename(initialdir="C:\\Users\\admin\\OneDrive\\Desktop\\notepad python",
                                        title="Open file name",
                                        defaultextension=".txt",
                                        filetypes=(("all file","*.*"),("Text file","*.txt"),
                                                   ("Python file","*.py")))
    try:
        window.title(os.path.basename(filepath)) #ethu vanthu ne open panra file name title ha display agum
        text_area.delete("1.0",END) #already erka file delete panitu ne open panra file nottepad la display agum

        file=open(filepath,"r")
        text_area.insert("1.0",file.read())
    except Exception:
        print("Couldn't read a file")
    finally:
        file.close()
def savefile():
    filepath=asksaveasfilename(initialdir="C:\\Users\\admin\\OneDrive\\Desktop\\notepad python",
                                          title="save file as",
                                          defaultextension="*.txt",
                                          filetypes=(("Text file","*.txt"),("Python file","*.py"),
                                                     ("All file","*.*")))
    if filepath is None:
        return
    else:
        try:
            window.title(os.path.basename(filepath))
            file=open(filepath,"w")
            file.write(text_area.get("1.0",END))
        except Exception:
            print("Couldn't save file")

def quit():
    window.destroy()

def cut():
    text_area.event_generate("<<Cut>>")
def copy():
    text_area.event_generate("<<Copy>>")
def paste():
    text_area.event_generate("<<Paste>>")
def Delete():
    text_area.delete("1.0",END)

def message():
    showinfo(title="info",message="you only written a code",icon="info")


window=Tk()
window.title("Notepad")
icon=PhotoImage(file="notepad.png")
window.iconphoto(True,icon)

#We are declaring a height and width constant value and variable
window_height=500
window_width=500

#This is for screen height and width
screen_height=window.winfo_screenheight()
screen_width=window.winfo_screenwidth()

x=int((screen_height/2)-(window_height/2))
y=int((screen_width/2)-(window_width/2))

window.geometry("{}x{}+{}+{}".format(window_height,window_width,x,y))
#window.geometry(f"{window_height}x{window_height}+{x}+{y}")#string format method

#font_area nu oru textvariable athu stringvar
font_name=StringVar(window)
font_name.set("Arial")
#font_size nu oru textvariable athu stringvar
font_size=StringVar(window)
font_size.set("25")

#Creating Text box and also scroll bar
text_area=Text(window,font=(font_name.get(),font_size.get()))
scroll_bar=Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E +S + W)
scroll_bar.pack(side="right",fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

#frame for buttons
frame=Frame(window)
frame.grid()
#This is for text color button
choose_Textcolor =Button(frame,text="fontcolor",command=font_color)
choose_Textcolor .grid(row=0,column=0)
#this for change font
change_fonts= OptionMenu(frame,font_name,*font.families(),command=change_font)
change_fonts.grid(row=0,column=1)

change_size=Spinbox(frame,from_=1,to=100,textvariable=font_size,command=change_font)
change_size.grid(row=0,column=2)

menu_bar=Menu(window)
window.config(menu=menu_bar)

#File menu

filemenu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

#Edit menu

edit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut",command=cut)
edit_menu.add_command(label="copy",command=copy)
edit_menu.add_command(label="paste",command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Delete",command=Delete)

#Help menu

help_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="View",menu=help_menu)
help_menu.add_command(label="help",command=message)
window.mainloop()