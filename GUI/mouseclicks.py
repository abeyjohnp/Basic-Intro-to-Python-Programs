from breezypythongui import EasyFrame
class MouseClickWindowDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Mouse Click on Window")
        self.addLabel(text="X Coordinate:", row=0, column=0)
        self.xField = self.addIntegerField(value=0, row=0, column=1)
        self.addLabel(text="Y Coordinate:", row=1, column=0)
        self.yField = self.addIntegerField(value=0, row=1, column=1)
        self.master.bind("<Button-1>", self.showCoordinates)

    def showCoordinates(self, event):
        x = event.x
        y = event.y
        self.xField.setNumber(x)
        self.yField.setNumber(y)
def main():
    MouseClickWindowDemo().mainloop()

if __name__ == "__main__":
    main()
