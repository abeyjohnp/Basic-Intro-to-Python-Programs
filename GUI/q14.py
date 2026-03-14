"""
    Write Python GUI program to take the birth date and output the age when a button is
pressed.
"""
from datetime import datetime
from breezypythongui import EasyFrame
class buttondemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.setSize(width=500, height=200)
        self.label=self.addLabel(text="Enter the day : ",row=0,column=0)
        self.day=self.addTextField(text="",row=0,column=1)
        self.addLabel(text="Enter the month : ",row=1,column=0)
        self.month=self.addTextField(text="",row=1,column=1)
        self.addLabel(text="Enter the year : ",row=2,column=0)
        self.year=self.addTextField(text="",row=2,column=1)
        self.btn=self.addButton(text="convert",row=3,column=1,command=self.dob)
    
    def dob(self):
        self.label=self.addLabel(text="Age : ",row=4,column=0)
        current_year = datetime.now().time
        self.output=self.addTextField(text=current_year-int(self.year.getText()),row=4,column=1)
def main():
    buttondemo().mainloop()

if __name__=="__main__":
    main()