import random
import customtkinter as ctk
from tkinter import messagebox



app = ctk.CTk()
app.geometry("300x200")
app.title("Rock Paper Scissors")
app.resizable(False , False)


frame = ctk.CTkFrame(app , corner_radius = 0)
frame.pack()


ctk.set_appearance_mode("System")


rs = 0
ys = 0


labelsyr = ctk.CTkLabel(frame , text = f"Your Score : {ys}\nRobot Score {rs}" , font = ("defult" , 19) , fg_color = "#20A5E2" , text_color = "white" , corner_radius = 10 , width = 300, height = 35)
labelsyr.pack(pady = 5 , padx = 7)


device = ctk.CTkOptionMenu(frame , values = ['Select the device' , 'Rock' , 'Paper' , 'Scissors'] , anchor = 'center' , width = 300 , height = 38 , font = ("defult" , 19) , dropdown_font = ("defult"  , 15) ,  dropdown_hover_color = "#9CA3AF")
device.pack(pady = 4 , padx = 7)


system_choices = ["Rock" , "Paper" , "Scissors"]

def usl():
    global ys , rs
    labelsyr.configure(text = f"Your Score : {ys}\nRobot Score {rs}")


def check():
    global rs , ys

    device1 = device.get().strip()
    system_choice = random.choice(system_choices)

    if device1 == 'Select the device':
        messagebox.showerror('Error' , 'Select the device')
    
    elif device1 == system_choice:
        messagebox.showinfo("Equal" , "You are tied")
    
    elif (device1 == "Rock" and system_choice == "Scissors") or \
            (device1 == "Scissors" and system_choice == "Paper") or \
            (device1 == "Paper" and system_choice == "Rock"):
        messagebox.showinfo("Win" , f"You won! Robot chose: {system_choice}")
        ys += 1

    else:
        messagebox.showinfo("Loss" , f"You lost! Robot chose: {system_choice}")
        rs += 1
        
    usl()


check_btn = ctk.CTkButton(frame , text = "Check" , font = ("defult" , 19) , command = check , width = 300 , height = 38)
check_btn.pack(padx= 7 , pady = 4)


def out():
    global ys , rs
    if ys > rs:
        messagebox.showinfo("Final Result", "Congratulations, you have won the game.")
    elif rs > ys:
        messagebox.showinfo("Final Result", "Unfortunately, you lost the game.")
    else:
        messagebox.showinfo("Final Result", "The game ended in a tie.")
    app.quit() 

out_btn = ctk.CTkButton(frame , text = "Exit" , font = ("defult" , 19) , fg_color ="#CE0000" ,  hover_color = "#990000" , command = out , width=300 , height = 40)
out_btn.pack(pady = 6 , padx = 7)


app.mainloop()
