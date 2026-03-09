"""
    Write Python GUI program to take the birth date and output the age when a button is
pressed.
"""

"design a python gui that takes user input for length and width of a rectangle, if a button pressed area is calculated"

from breezypythongui import EasyFrame
class buttondemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.setSize(width=500, height=200)
        self.label=self.addLabel(text="Enter the width : ",row=0,column=0)
        self.inputFld1=self.addTextField(text="",row=0,column=1)
        self.addLabel(text="Enter the height : ",row=1,column=0)
        self.inputFld2=self.addTextField(text="",row=1,column=1)
        self.btn=self.addButton(text="convert",row=2,column=1,command=self.concatenate)
    
    def concatenate(self):
        self.label=self.addLabel(text="Output : ",row=3,column=0)
        t1=self.inputFld1.getText()
        t2=self.inputFld2.getText()
        t3=int(t1)*int(t2)
        self.output=self.addTextField(text=t3,row=3,column=1)
def main():
    buttondemo().mainloop()

if __name__=="__main__":
    main()