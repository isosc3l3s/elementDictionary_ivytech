from tkinter import *
from periodicTable import elements

#RELIC
givenInfo = input("please enter an the information you were given about the element, and I will enter the info for it:") #prompt for what they were provided
#RELIC
#if else route to designate each entry of givenInfo as str, int, or float
if givenInfo.isdigit():
    givenInfo = int(givenInfo)
elif givenInfo.replace('.', '', 1).isdigit():
    givenInfo = float(givenInfo)
else:
    givenInfo = givenInfo.capitalize()

#The proper designations for the data, for the start, it is all empty
name = ""
symbol = ""
atomNum = 0
atomMass = 0


#Loop to run through elements dictionry and make list of the values there
result = [] #List needed 
def getElementList(input):
    for element, element_dict in elements.items():
        if (input in element_dict):
            result = list(element_dict)
            break
    return result
#RELIC
print(getElementList(givenInfo))
print(givenInfo)        
#RELIC


#______________________________________________________________Margin from main program engine______________________________________________________________#
root = Tk()

#myText=givenInfo;

firstframe = Frame(root)
firstframe.pack()

secondframe= Frame(root)
secondframe.pack( side = BOTTOM )


#Text label prompt for what user was provided in the problem label in row 0
Label(firstframe, text='What were you provded for the element?').grid(row=0)

#Result1 label in row 1
Label(firstframe, text=f"{'The symbol for the element is: '+ symbol}").grid(row=1) #this line prints the result as needed

#Result2 label in row 2
Label(firstframe, text='result2 this might be the atomic number').grid(row=2)

#Result3 label in row 3
Label(firstframe, text='result3 this might be the atomic mass').grid(row=3)

#Result4 label in row 4
Label(firstframe, text='The atomic number is:').grid(row=4)

#entry field
entry = Entry(firstframe)
#place it next to "what were you given"
entry.grid(row=0, column=1)


#Loop to assign each value to its proper designation
i=0
while i < len(getElementList(givenInfo)):
    if type(getElementList(givenInfo)[i]) is int:
        atomNum = getElementList(givenInfo)[i]
        print("The atomic number is:", atomNum)
        i+=1
    elif type(getElementList(givenInfo)[i]) is float:
        atomMass = getElementList(givenInfo)[i]
        print("The atomic mass is:", atomMass)
        i+=1
    elif type(getElementList(givenInfo)[i]) is str and len(getElementList(givenInfo)[i]) > 2:
        name = getElementList(givenInfo)[i]
        print("The element name:", name)
        i+=1
    elif type(getElementList(givenInfo)[i]) is str and len(getElementList(givenInfo)[i]) <= 2:
        symbol = getElementList(givenInfo)[i]
        print("The symbol for the element:", symbol)
        #Label(firstframe, text=f"{'The symbol for the element is: '+ symbol}").grid(row=1)
        i+=1
    else:
        print(type(getElementList(givenInfo)[i]))
        i+=1

#answer label adjacent to label Result , so row 2 column 1
Label(firstframe,text="",textvariable=givenInfo).grid(row=2,column=1)

#creating a search button. Clicking the button should initiate the search through the dictionary.
#command attribute is for on click event.
searchButton = Button(secondframe, text ='Search', command=getElementList(givenInfo))
searchButton.pack()

#creating a new button, should clear the results when clicked.
clearButton = Button(secondframe, text ='Clear')
clearButton.pack()

#creating a new window to search another element with
newWindowButton = Button(secondframe, text="New Window", command=root.mainloop)
newWindowButton.pack()

#creating a Celsius to Exit button. root.destroy will exit the window
exitbutton = Button(secondframe, text ='Exit', fg ='red', command=root.destroy)
exitbutton.pack()
root.mainloop()