from tkinter import *

#Tkinter configuration
root = Tk()
root.title("calculator")
root.configure(background='#0D0D0F')
root.geometry("260x310")

#Global variables
funct_numb = None
action = None

#Main panel
main_panel = Entry(root, width = 40, fg = "White", bg = "#0D0D0F", relief = "flat")
main_panel.grid(row = 0, column = 0, columnspan = 4, ipady = 30)

### Calculator functions

# CE button- Clean main panel
def action_clear():
    main_panel.delete(0,END)

# Click on the number
def action_click(number):
    current = main_panel.get()
    main_panel.delete(0,END)
    main_panel.insert(0, str(current) + str(number))

# Negative number
def action_p_m():
    current = main_panel.get()
    main_panel.delete(0,END)
    main_panel.insert(0, (float(current)*(-1)))
        
# Percentage. formula= X% of 
def action_percentage():
    first_number = main_panel.get()
    global funct_numb
    global action
    action= "percentage"  
    funct_numb = float(first_number)
    main_panel.delete(0,END)

# Math operation "+"
def action_add():
    first_number = main_panel.get()
    global funct_numb
    global action
    action= "adition"  
    funct_numb = float(first_number)
    main_panel.delete(0,END)

# Math operation "-"
def action_subtract():
    first_number = main_panel.get()
    global funct_numb
    global action
    action= "substraction"  
    funct_numb = float(first_number)
    main_panel.delete(0,END)

#Math operation "*"
def action_multiple():
    first_number = main_panel.get()
    global funct_numb
    global action
    action= "multiplaction"  
    funct_numb = float(first_number)
    main_panel.delete(0,END)

#Math operation "/"
def action_divide():
    first_number = main_panel.get()
    global funct_numb
    global action
    action = "division"  
    funct_numb = float(first_number)
    main_panel.delete(0,END)

#Math operation EQUAL
def action_equal():
    second_number = main_panel.get()
    main_panel.delete(0,END)
    if action == "adition":
        main_panel.insert(0, funct_numb + float(second_number))
    if action == "substraction":
        main_panel.insert(0, funct_numb - float(second_number))
    if action == "multiplaction":
        main_panel.insert(0, funct_numb * float(second_number))
    if action == "division":
        main_panel.insert(0, funct_numb / float(second_number))
    if action == "percentage":
        main_panel.insert(0, funct_numb / 100* float(second_number))  
        


### Key pad buttons

# First column
button_CE = Button(root, text = "CE", height = 2, width = 7, fg = "White",bg="#144072", activebackground= "White",
                    activeforeground = "#144072", relief = "flat", command = action_clear)
button_CE.grid(row = 1, column = 0, pady = 2, padx = 2)

button_p_m = Button(root, text = "+/-", height = 2, width = 7, fg = "White",bg="#144072", activebackground= "White",
                    activeforeground = "#144072", relief = "flat", command = action_p_m)
button_p_m.grid(row = 1, column = 1, pady = 2, padx = 2)

button_perc = Button(root, text = "%", height = 2, width = 7, fg = "White",bg="#144072", activebackground= "White",
                     activeforeground = "#144072", relief = "flat", command = action_percentage)
button_perc.grid(row = 1, column = 2, pady = 2, padx = 2)

button_division = Button(root, text = "/", height = 2, width = 7, fg = "White",bg="#144072", activebackground= "White",
                         activeforeground = "#144072", relief = "flat", command = action_divide)
button_division.grid(row = 1, column = 3, pady = 2, padx = 2)

# Second column
button_7 = Button(root, text = "7", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(7))
button_7.grid(row = 2, column = 0,  pady = 2, padx = 2)

button_8 = Button(root, text = "8", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(8))
button_8.grid(row = 2, column = 1, pady = 2, padx = 2)

button_9 = Button(root, text = "9", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(9))
button_9.grid(row = 2, column = 2, pady = 2, padx = 2)

button_multiple = Button(root, text = "*", height = 2, width = 7, fg = "White",bg="#144072", activebackground= "White",
                         activeforeground = "#144072", relief = "flat", command = action_multiple)
button_multiple.grid(row = 2, column = 3, pady = 2, padx = 2)

# Third column
button_4 = Button(root, text = "4", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(4))
button_4.grid(row = 3, column = 0, pady = 2, padx = 2)

button_5 = Button(root, text = "5", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(5))
button_5.grid(row = 3, column = 1, pady = 2, padx = 2)

button_6 = Button(root, text = "6", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(6))
button_6.grid(row = 3, column = 2, pady = 2, padx = 2)

button_subtract = Button(root, text = "-", height = 2, width = 7, fg = "White",bg="#144072", activebackground= "White",
                         activeforeground = "#144072", relief = "flat", command = action_subtract)
button_subtract.grid(row = 3, column = 3, pady = 2, padx = 2)

# Forth column
button_1 = Button(root, text = "1", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(1))
button_1.grid(row = 4, column = 0, pady = 2, padx = 2)

button_2 = Button(root, text = "2", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(2))
button_2.grid(row = 4, column = 1, pady = 2, padx = 2)

button_3 = Button(root, text = "3", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(3))
button_3.grid(row = 4, column = 2, pady = 2, padx = 2)

button_plus = Button(root, text = "+", height = 5, width = 7, fg = "White",bg="#144072", activebackground= "White",
                     activeforeground = "#144072", relief = "flat", command = action_add)
button_plus.grid(row = 4, column = 3,  rowspan = 2, pady = 2, padx = 2 )

# Fifth column
button_0 = Button(root, text = "0", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                  activeforeground = "#556577", relief = "flat", command = lambda: action_click(0))
button_0.grid(row = 5, column = 0 , pady = 2, padx = 2 )

button_coma = Button(root, text = ".", height = 2, width = 7, fg = "White",bg="#556577", activebackground= "White",
                     activeforeground = "#556577", relief = "flat", command = lambda: action_click("."))
button_coma.grid(row = 5, column = 1, pady = 2, padx = 2)

button_equal = Button(root, text = "=", height = 2, width = 7, fg = "White",bg="#144072", activebackground= "White",
                      activeforeground = "#144072", relief = "flat", command = action_equal)
button_equal.grid(row = 5, column = 2, pady = 2, padx = 2)

root.mainloop()


