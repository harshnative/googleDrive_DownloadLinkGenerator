# importing things we need
from tkinter import *
import pyperclip
from googleDriveLink import *


def main():
    # creating a new tkinter window
    newWindow = Tk()
    newWindow.geometry("1000x500")

    # showing the paste your link here text 
    inputLabel = Label(newWindow , text = "Paste your link here - ")
    labelfont = ('arial', 16) # changed the font and font size 
    inputLabel.config(font = labelfont) 
    inputLabel.place(x = 50 , y = 20)

    # making a input window - text widget
    t = Text(newWindow , height = 1 , width = 500 , padx = 5 , pady = 5)
    labelfont = ('arial', 12)
    t.config(font = labelfont)
    t.pack(padx=50, pady=50)

    # function to get the input inputted in the text widget 
    def retrieve_input():
        inputValue = t.get("1.0",'end-1c')
        showOutput(inputValue)

    # making a button so that we can get the input and work on it - it call the retrieve_input() func
    myButton = Button(newWindow , bd = "5" , bg = "blue" , fg = "white" , text = "Generate" , padx = 50 , pady = 10 , command = retrieve_input)
    labelfont = ('arial', 20 , 'bold')
    myButton.config(font = labelfont)
    myButton.place(relx = 0.5 , y = 150 , anchor=CENTER)

    # showing the output
    def showOutput(inputString):
        result = driverFunc(inputString)    # imported file GoogleDriveLink.py
        if(result == 0):
            result = "Invalid Link :("
        # we are just working on some particular type of links

        # generating a new text widget to show our output as if we output text as label then we cannot select that text
        # but this text widget is going to be passive - you cannot input data in it
        tOutput = Text(newWindow , height = 1 , width = 500 , padx = 5 , pady = 5 )
        labelfont = ('arial', 12)
        tOutput.config(font = labelfont)
        tOutput.insert(1.0, result)     # we preinserted the data into the text widget
        tOutput.configure(relief="flat")
        tOutput.configure(state="disabled")
        tOutput.pack(padx=50, pady=100 , anchor=CENTER)
        
        # showing the text - press reset to start again
        jobDone = Label(newWindow , text = "Press reset to start again")
        labelfont = ('arial', 12)
        jobDone.config(font = labelfont)
        jobDone.pack()

        # function to copy the text to the clipBoard using a pyperclip libary that we imported at the starting
        def copyToClipboard():
            pyperclip.copy(result)
            pyperclip.paste()
            copiedLabel = Label(newWindow , text = "Text copied to clipboard")
            copiedLabel.pack()


        photo = PhotoImage(file = "images\clipboard-regular.png") 

        photoSmall = photo.subsample(8,8)

        # button to call the copy to clipboard function
        myButtonForCopy = Button(newWindow , bd = "5" , bg = "blue" , fg = "white" , text = "Copy to clipboard", image = photoSmall  , padx = 20 , pady = 10 , compound  = LEFT, command = copyToClipboard)
        labelfont = ('arial', 12 , 'bold')
        myButtonForCopy.config(font = labelfont)
        myButtonForCopy.image = photoSmall
        myButtonForCopy.place(relx = 0.5 , y = 320 , anchor=CENTER)

        # function so that you can reset the things and generate new link
        def reset():
            newWindow.destroy()
            main()

        # button to call reset
        myButtonForReset = Button(newWindow , bg = "Red" , fg = "white" , text = "Reset" , padx = 20 , pady = 10 , command = reset)
        labelfont = ('arial', 12 , 'bold')
        myButtonForReset.config(font = labelfont)
        myButtonForReset.place(relx = 0.7 , y = 150 , anchor=CENTER)


    newWindow.mainloop()


if __name__ == "__main__":
    main()