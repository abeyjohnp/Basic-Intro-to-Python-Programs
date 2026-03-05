from breezypythongui import EasyFrame
class LabelDemo (EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Window",background="red",resizable=False)
        #easyframe object created
        # you can pass these as attributes or as methods
        # setBackground(color)
        self.addLabel(text="Hello World!",row=0,column=0) #adding components

def main():
    LabelDemo().mainloop()

if __name__=="__main__":
    main()


#LabelDemo()