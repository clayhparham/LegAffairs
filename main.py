
from tkinter import *

from pandas import *

pd = pandas
df = pd.read_excel('List of Elected Representatives.xlsx')
k = 0
pd.options.display.max_colwidth = 80

# function for printing the specific line
def selected_item():
    for i in listbox.curselection():
        text.delete('1.0', END)
        text.insert(INSERT, df.iloc[i])

# builds the tkinter
top = Tk()
top.geometry('1000x300')
top.title('Congresspeople')
text = Text(top)

# makes the list of congresspeople
listbox = Listbox(top, height = 10,
                  width = 15,
                  bg = "grey",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "yellow")

# prints the list of congresspeople in the listbox
for i in range(len(df)):
    listbox.insert(k, df.loc[k, "Name"])
    listbox.bind('<<ListBoxSelect>>')
    k = k+1

# makes the output textbox
text=Text(top, height=10, width=100)

# makes the "print selected" button
btn = Button(top, text='Print Selected', command=selected_item)

# packs the aforementioned
listbox.pack(side = 'left')
btn.pack(side='bottom')
text.pack(side='right')

def getTextInput():
    result=textExample.get("1.0","end")
    print(result)

top.mainloop()