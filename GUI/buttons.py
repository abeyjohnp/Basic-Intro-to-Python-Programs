from breezypythongui import EasyFrame
class buttondemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.label=self.addLabel(text="Hello Button",row=0,column=0,columnspan=2,sticky="NSEW")
        self.clearbtn=self.addButton(text="Clear ",row=1,column=0,command=self.clear)
        self.restorebtn=self.addButton(text="Restore",row=1,column=1,state="disabled",command=self.restore)

    def clear(self):
        self.label["text"]=""
        self.clearbtn["state"]="disabled"
        self.restorebtn["state"]="normal"
    
    def restore(self):
        self.label["text"]="Hellow World!"
        self.clearbtn["state"]="normal"
        self.restorebtn["state"]="disabled"
def main():
    buttondemo().mainloop()

if __name__=="__main__":
    main()