import tkinter
import os
from tkinter import messagebox
#from tkinter import *
from tkinter import StringVar
from tkinter import Entry
import subprocess

this_user = os.popen('echo -n "$USER"').read()

def servers_list(user_input):
    if user_input == 1:
        subprocess.run('xterm -hold -e nmcli',shell=True)
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        tk.mainloop(exit())

tk = tkinter.Tk()
tk.geometry('550x300')
#tk.resizable(False, False)
tk.title("OpenConnect GUI")
#tk.config(bg='#E1941A')

pad_general = 50
btn_font = 7

server_var = StringVar()

def server_var_func(usr_input):
    if usr_input == 1:
        pass
    if usr_input == 2:
        print(server_var.get())


label = tkinter.Label(tk , text=f"Welcome {this_user} !  \n \n Type Your OpenConnect Server Down Blow \n",font=("", 11))
label.grid(row=0,column=1,padx=pad_general,pady=pad_general)
label.pack()

Entry(tk,textvariable = server_var, font=btn_font).pack()

label_2 = tkinter.Label(tk)
#label_2.grid(row=0,column=1)
label_2.pack()

button1 = tkinter.Button(tk , text="Connect",padx=pad_general, font= btn_font,command=lambda:server_var_func(1))
button1.pack()


button2 = tkinter.Button(tk , text="Debug",padx=pad_general, font= btn_font,command=lambda:print(server_var_func(2)))
button2.pack()

button_quit = tkinter.Button(tk , text="Quit", font= btn_font,padx=pad_general,command=lambda:servers_list(4))
button_quit.pack()

#button2 = tkinter.Button(tk , text="Server2",font= 10, command=lambda:k_maker_servers(2))
#button2.pack()

#button3 = tkinter.Button(tk , text="Server3", font= 10,command=lambda:k_maker_servers(3))
#button3.pack()

tk.mainloop()