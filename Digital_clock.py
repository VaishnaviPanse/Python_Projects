# import modules
from tkinter import *
from tkinter.ttk import *

# importing strftime function to retrieve system's time
# strftime function is used to convert date and time objects to their string representation
from time import strftime 

# creating tkinter window
root = Tk()
root.title("Clock")

# Function used to display time on label
def time():
     string = strftime("%H:%M:%S %p")
     label.config(text=string)
     label.after(1000,time)

# Styling the label widget   
label = Label(root,font=("ds-digital",150), background = "gray", foreground="black")

#Placing clock at the centre of the tkinter window
label.pack(anchor="center")
time()

# infinite loop used to run the application
mainloop()