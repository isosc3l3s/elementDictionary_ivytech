#Title: Elementary
#Authoer: Ian Schaak
#Date last modified: 12/16/2023 10:43 am
#Purpose: To take in atomic nuumber, atomic mass, atomic symbol, or element name, and display what ever was not entered.



import tkinter as tk
from periodicTable import elements


#if else route to designate each entry of givenInfo as str, int, or float
def ConvertType(text):
    if text.isdigit():
        item = int(text)#item made an in
    elif '.' in text and text.replace('.', '', 1).isdigit() or text.isdigit() > 118:
        item = float(text)#item made a float
    else:
        item = text.capitalize()#item first letter capitalized
    return item

#Loop to run through elements dictionry and make list of the values there
def getElementList(item):
    item = ConvertType(item)#item type conversion called on
    for key, element_dict in elements.items():
        if item in element_dict:
            return element_dict
    return

#Loop to assign each value to its proper designation           
def updateLabels(text):
    """Display result in Labels"""
    
    
    element = getElementList(text)#element attribute list established
    
    if element is None:
        labelOne['text'] = 'No Found'
        labelTwo['text'] = ''  
        labelThree['text'] = ''  
        labelFour['text'] = ''  
        return
        
    name, symbol, atom_num, atom_mass = element#order of list defined

    text = f"The symbol is: {symbol}"
    labelOne['text'] = text
    
    text = f"The atomic number is: {atom_num}"    
    labelTwo['text'] = text

    text = f"The atomic mass is: {atom_mass}"
    labelThree['text'] = text

    text = f"The element name: {name}"
    labelFour['text'] = text

#Clear enttry field function to prep for new entries
def clearEntry():
    labelOne['text'] = ''
    labelTwo['text'] = ''
    labelThree['text'] = ''
    labelFour['text'] = ''
    given_info_var.set('')




root = tk.Tk()
root.title("Elementary")

firstframe = tk.Frame(root)#first frame with entry
firstframe.pack()

secondframe= tk.Frame(root)#second frame with buttons
secondframe.pack()

#Text label prompt for what user was provided in the problem label in row 0
tk.Label(firstframe, text='What were you provided for the element:').grid(row=0)

#string var for entry field
given_info_var = tk.StringVar() #String variable for use in tkinter
#entry field
entry = tk.Entry(firstframe, textvariable = given_info_var)#assigning string variable.
entry.grid(row=0, column=1)
entry.bind('<Return>', lambda event: updateLabels(given_info_var.get()))


#Result label in rows 1-4
labelOne = tk.Label(firstframe)
labelOne.grid(row=1) 
labelTwo = tk.Label(firstframe)
labelTwo.grid(row=2)
labelThree = tk.Label(firstframe)
labelThree.grid(row=3)
labelFour = tk.Label(firstframe)
labelFour.grid(row=4)



#answer label adjacent to label Result , so row 2 column 1
tk.Label(firstframe, text='', textvariable = given_info_var).grid(row=2,column=1)

#creating a search button. Clicking the button should initiate the search through the dictionary.
searchButton = tk.Button(secondframe, text ='Search', command=lambda: updateLabels(given_info_var.get()))
searchButton.pack()

#creating a new button, should clear the results when clicked.
clearButton = tk.Button(secondframe, text ='Clear', command= clearEntry)
clearButton.pack()

#creating a Celsius to Exit button. root.destroy will exit the window
exitbutton = tk.Button(secondframe, text ='Exit', fg ='red', command=root.destroy)
exitbutton.pack()


root.mainloop()