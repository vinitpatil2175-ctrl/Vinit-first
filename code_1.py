## X & O Tic-Tac-Toe game
import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.destroy()
            return

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

# Bind i=i to capture the loop variable correctly
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, 
                     command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player = "X"
winner = False    
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()


##Rock Paper Scissor Game
import random
item_list=["Rock","Scissor","Paper"]
user_choice = input("Enter your choice: ")
comp_choice=random.choice(item_list)
print(f"Use Choice={user_choice} , Computer Choice={comp_choice}")
if (user_choice==comp_choice):
    print("Math Tie")
elif (user_choice == "Rock"):
    if(comp_choice=="Paper"):
        print("Paper covers,COMP WINS!!")
    else:
        print("Rock smashed Scissor,YOU WON!!")
elif(user_choice=="Paper"):
    if(comp_choice=="Scissor"):
        print("Scissor cuts Paper,COMP WINS!!") 
    else:
        print("Paper covers Rock,YOU WON!!")
elif(user_choice=="Scissor"): 
    if(comp_choice=="Rock"):
        print("ROck smashed Scissor,COMP WINS!!")   
    else:
        print("Scissor cuts Paper,YOU WON!!")


##Contri per person calculator
rent =int(input("Enter your Rent:"))
food =int(input("\nEnter your Food Expenses:"))
extra=int(input("Enter your Extra expenses:"))
electricity_units =int(input("Enter units of Elec.used:"))
charge_per_unit=int(input("Enter charge of 1 unit Elec.in your Area:"))
electricity_bill = electricity_units*charge_per_unit
persons = int(input("No.of people living on room:"))
Amount_to_pay= (rent+food+extra+electricity_bill)//persons
print("Per Person Contri:",Amount_to_pay)



##Digital Clock
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
    
label = tk.Label(root,font=('calibri',60,'bold'),background='green',foreground='black')
label.pack(anchor='center')

def time():
    string = strftime( '%I:%M:%S  %p \n %D') #for 12hr clock use %I else for 24hr clock you need to use %H
    label.config(text=string)
    label.after(1000,time)

time()
root.mainloop()



##Text Editor (Notepad like) miniproject

import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0,tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes = [("Text Files","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0,tk.END,file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes = [("Text Files","*.txt")])   
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("Info","File Saves Successfully!")

root =tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label="File",menu = file_menu)
file_menu.add_command(label="New",command = new_file)
file_menu.add_command(label="Open",command= open_file)
file_menu.add_command(label="Save",command= save_file)
file_menu.add_separator()
text = tk.Text(root,wrap=tk.WORD,font=("calibri",12) ,fg="blue")
text.pack(expand=tk.YES,fill =tk.BOTH)

root.mainloop()




















