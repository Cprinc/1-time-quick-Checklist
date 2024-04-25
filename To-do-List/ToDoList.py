import tkinter as tk

row = 0
padding_increment = 6
def make_new_row(): #adds a new item to the list
    global row
    row += 1
    if row < 13: #check if row is less than 12
        new_checkBox = tk.Checkbutton(GUI,text=f"Item {row}: ", font=('Arial',12)) #Create new checkbutton instance
        new_checkBox.grid(row=row+2,column=0,sticky="w",pady=padding_increment,columnspan=3,padx= 3) #place checkbox
        new_text_box = tk.Entry(GUI, font =('Arial',12)) #Create textbox instance
        new_text_box.grid(row=row+2,column=0,pady=padding_increment,columnspan=3,padx= 3) #place textbox
    elif row == 13: #if row is 13 let the user know they cant have any more items
        new_label = tk.Label(GUI, text = f"Can't place anymore items (Try to stick with 12 things at a time)", font=('Arial',13))
        new_label.grid(row=row+2,column=0,sticky="w", pady=padding_increment, padx= 3)

def remove_last_row(): #method that will remove all widgets in the last row whatever it is 
    global row 
    if row > 0:
        # Destroy or remove widgets in the last row
        for widget in GUI.grid_slaves(row=row+2):
            widget.grid_forget()
            widget.destroy()
        
        # Decrement row count
        row -= 1
    


GUI = tk.Tk() #Create tk instance
GUI.geometry("500x700") #Chose size of GUI
GUI.title("To Do List") #title GUI
todo_frame = tk.Frame(GUI) #Create a frame for centering purposes
todo_frame.grid(row=0, column=0, padx=115, pady=10) #place frame in designated location

title_label = tk.Label(todo_frame, text="Today To-Do-List", font=('Lubalin Graph', 24)) #Create title label instance in frame
title_label.grid(row=0, column=0, columnspan=4) #place title label 

add_more_items = tk.Button(todo_frame, text="add new Item", font=('Arial', 15), command=make_new_row) #create new row button instance in frame
add_more_items.grid(row=1, column=0, columnspan=4) #place new row button

add_remove_Button = tk.Button(todo_frame,text="Remove Last Row", font=('Arial',12),command=remove_last_row) #create remove button in frame
add_remove_Button.grid(row=2,column=0,columnspan=4,pady= 10) #place remove button 



GUI.mainloop() #Open GUI in a loop to allow multiple button presses (Code will loop)