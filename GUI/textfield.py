from breezypythongui import EasyFrame
class textfield(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Input",row=0,column=0,columnspan=2,sticky="NSEW")
        self.inputField=self.addTextField(text="",row=0,column=0)
        self.addLabel(text="Output",row=1,column=0,columnspan=2,sticky="NSEW")
        self.outputField=self.addTextField(text="",row=0,column=0)
        self.addButton(text="Convert",row=2,column=0,command=self.convert)

    def convert(self):
        text=self.inputField.getText()
        


def main():
    textfield().mainloop()

if __name__=="__main__":
    main()