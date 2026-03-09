"""
Write a GUI-based program that allows the user to convert amount in Indian Rupees to
amount in Euro. The interface should have labeled entry fields for these two values.
These components should be arranged in a grid where the labels occupy the first row and
the corresponding fields occupy the second row. At start-up, the Rupees field should
contain 0.0, and the Euro field should contain 0.0. The third row in the window contains
two command buttons, labeled R->E and E-&>R. When the user presses the first button,
the program should use the data in the Rupee field to compute the amount in Euro, which
should then be output in the Euro field. The second button should perform the inverse
function."""

from breezypythongui import EasyFrame
class MoneyConv(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.setSize(width=500,height=200)
        self.addLabel(text="Enter INR : ",row=0,column=0)
        self.addLabel(text="Enter EURO : ",row=1,column=0)
        self.inr=self.addTextField(text="0.0",row=0,column=1)
        self.euro=self.addTextField(text="0.0",row=1,column=1)
        self.inrbtn=self.addButton(text="R->E",row=2,column=0,command=self.inrconv)
        self.eurobtn=self.addButton(text="E->R",row=2,column=1,command=self.euroconv)
    
    def inrconv(self):
        euro=float(self.inr.getText())*0.0094
        self.euro.setText(euro)
    
    def euroconv(self):
        inr=float(self.euro.getText())*106.65
        self.inr.setText(inr)
    
def main():
    MoneyConv().mainloop()

if __name__ == "__main__":
    main()

