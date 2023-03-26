###############################################################################
"""
Created By stking68
https://github.com/stking68


tkterminal by Saadmairaj
https://github.com/Saadmairaj/tkterminal
"""
###############################################################################

import tkinter
import os
import sys
from tkinter import messagebox
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import Menu
import subprocess
import sqlite3
from tkterminal import Terminal

this_user = os.popen('echo -n "$USER"').read()

tk = tkinter.Tk()
tk.geometry('493x605')
#tk.resizable(False, False)
tk.title("OC GUI")
tk.iconphoto(True,PhotoImage(file="ethernet-port-icon.png"))
tk.config(bg='#444444')
#tk.config(bg='#888A85')


################# Style ##############################
style = ttk.Style()

style.configure('W.TButton', font =('calibri', 10,),
                            foreground="white",background="black")

style.configure('L.TButton', font =('calibri', 9,),
                            foreground="white",background="black")

style.configure('Welcome.TLabel', font =('calibri', 10,),
                            foreground="white",background="black")

style.configure('CmBox.TButton' , font =('calibri', 10,),
                            foreground="black",background="white")
######################################################



################# Variable's #########################
pad_general = 50
list_of_usernames = list()
list_of_servers = list()
list_of_passwords = list()
server_field_user_input_var = StringVar()
username_field_user_input_var = StringVar()
password_field_user_input_var = StringVar()
######################################################


########### Terminal Window ##########################
terminal = Terminal(pady=1, padx=1,height=15,
                    width=70,background='black',foreground='white',
                    insertbackground='white')

terminal.grid(row=10,column=0,pady=6,columnspan = 10)
terminal.shell = True
######################################################


################## Sqlite Connection #################
try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()

except sqlite3.Error as error:
    terminal.run_command(f"echo 'Error occurred - {error}'")


sqliteConnection.execute('''CREATE TABLE IF NOT EXISTS Info
        (ID        INT              ,
        Username   TEXT             ,
        Server     TEXT             ,
        Password   TEXT 
                                    );''')
######################################################


######## Fetching Data From SQL Table ################
cursor.execute("""SELECT * FROM Info""")
rows = cursor.fetchall()
for row in rows:
    list_of_usernames.append(row[1])
    list_of_servers.append(row[2])
    list_of_passwords.append(row[3])

if len(list_of_servers) > 4 or len(list_of_usernames) > 4:
    cursor.execute("DROP TABLE Info")
    sqliteConnection.commit()
######################################################


################ Functions ###########################
def Connection_Func(user_input):
    if user_input == 1:
        #The Connect Button
        terminal.run_command(f"sudo echo \"{password_field_user_input_var.get()}\"| openconnect {server_field_user_input_var.get()} --user={username_field_user_input_var.get()} --passwd-on-stdin")
        
    elif user_input == 2:
        terminal.run_command(f"sudo openconnect {server_field_user_input_var.get()} --user={username_field_user_input_var.get()} --no-passwd")

    elif user_input == 3:
        #The Disconnect Button
        subprocess.run("killall -9 openconnect", shell= True)
        python = sys.executable
        os.execl(python, python, * sys.argv)
        tk.mainloop(exit())

    elif user_input == 4:
        #The Exit Button
        subprocess.run("killall -9 openconnect", shell= True)
        sys.exit()
    elif user_input == 5:
        cursor.execute("DROP TABLE Info")
        sqliteConnection.commit()
        

def checkbox_is_clicked():
    if server_field_user_input_var.get() not in list_of_servers and username_field_user_input_var.get() not in list_of_usernames and password_field_user_input_var.get() not in list_of_servers:
        cursor.execute(f"INSERT INTO Info (Username,Server,Password) VALUES (\"{username_field_user_input_var.get()}\",\"{server_field_user_input_var.get()}\",\"{password_field_user_input_var.get()}\")")
        sqliteConnection.commit()
        terminal.run_command('echo "Done!"')


def server_combobox_is_clicked(event):
    if server_field_user_input_var.get() == list_of_servers[0]:
        username_field_user_input_var.set(list_of_usernames[0])
        password_field_user_input_var.set(list_of_passwords[0])

    elif server_field_user_input_var.get() == list_of_servers[1]:
        username_field_user_input_var.set(list_of_usernames[1])
        password_field_user_input_var.set(list_of_passwords[1])

    elif server_field_user_input_var.get() == list_of_servers[2]:
        username_field_user_input_var.set(list_of_usernames[2])
        password_field_user_input_var.set(list_of_passwords[2])

    elif server_field_user_input_var.get() == list_of_servers[3]:
        username_field_user_input_var.set(list_of_usernames[3])
        password_field_user_input_var.set(list_of_passwords[3])



def username_combobox_is_clicked(event):
    if username_field_user_input_var.get() == list_of_usernames[0]:
        server_field_user_input_var.set(list_of_servers[0])
        password_field_user_input_var.set(list_of_passwords[0])

    elif username_field_user_input_var.get() == list_of_usernames[1]:
        server_field_user_input_var.set(list_of_servers[1])
        password_field_user_input_var.set(list_of_passwords[1])

    elif username_field_user_input_var.get() == list_of_usernames[2]:
        server_field_user_input_var.set(list_of_servers[2])
        password_field_user_input_var.set(list_of_passwords[2])

    elif username_field_user_input_var.get() == list_of_usernames[3]:
        server_field_user_input_var.set(list_of_servers[3])
        password_field_user_input_var.set(list_of_passwords[3])
######################################################


############### Top Left Menu ########################
# create a menubar
menubar = Menu(tk)
tk.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff = False
)
exit_menu = Menu(
    menubar,
    tearoff = False
)

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Change Theme',command=lambda:style.theme_use('alt'))

file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

file_menu.add_command(
    label='Exit',
    command=tk.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline = False
)

exit_menu.add_command(label="About",command=lambda:messagebox.showinfo('About'
                                                                    , 'Created by stking68\n https://github.com/stking68',icon='info'))
menubar.add_cascade(label="Help",menu=exit_menu)
######################################################


label_welcome = ttk.Label(tk , text=f"Welcome {this_user} !",font=("", 11),style='Welcome.TLabel')
label_welcome.grid(row=0,column=1)

########### Server / Username / Password #############
label_1 = ttk.Label(tk , text="Server",font=("", 11),style='L.TButton').grid(row=1,column=0,padx=10,ipady=7)
Entry1 = ttk.Combobox(tk, values=list_of_servers,font=("",11),textvariable=server_field_user_input_var,style='CmBox.TButton')
Entry1.bind('<<ComboboxSelected>>', server_combobox_is_clicked)
Entry1.grid(row=1,column=1,pady=4,ipadx=pad_general)

label_2 = ttk.Label(tk , text="Username",font=("", 11),style='L.TButton').grid(row=2,column=0,padx=10,ipady=7)
Entry2 = ttk.Combobox(tk, values=list_of_usernames,font=("",11),textvariable=username_field_user_input_var,style='CmBox.TButton')
Entry2.bind('<<ComboboxSelected>>', username_combobox_is_clicked)
Entry2.grid(row=2,column=1,pady=4,ipadx=pad_general)

label_3 = ttk.Label(tk , text="Password",font=("", 11),style='L.TButton').grid(row=3,column=0,padx=10,ipady=7)
Entry3 = ttk.Entry(tk, show="*",font=("",11),textvariable=password_field_user_input_var,style='CmBox.TButton')
Entry3.grid(row=3,column=1,pady=4,ipadx=pad_general)
######################################################


########### Button's #################################
button1 = ttk.Button(tk , text="Connect",command=lambda:Connection_Func(1),style='W.TButton')
button1.grid(row=4,column=1)

button2 = ttk.Button(tk , text="Connect W/out Pass",command=lambda:Connection_Func(2),style='W.TButton')
button2.grid(row=5,column=1)

button3 = ttk.Button(tk , text="Disconnect/Reset",command=lambda:Connection_Func(3),style='W.TButton')
button3.grid(row=6,column=1)

button_quit = ttk.Button(tk , text="Quit",command=lambda:Connection_Func(4),style='W.TButton')
button_quit.grid(row=9,column=1)

checkbox_saveinfo = ttk.Button(tk, text="Save Account Info",
                                    command=checkbox_is_clicked,
                                    style='W.TButton',
                                    )

checkbox_saveinfo.grid(row=7,column=1)

button_purge_database = ttk.Button(tk , text="Delete Account Info",command=lambda:Connection_Func(5),style='W.TButton')
button_purge_database.grid(row=8,column=1)
######################################################

tk.mainloop()
cursor.close()