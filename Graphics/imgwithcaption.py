from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
class ImageDemo(EasyFrame):
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Image Demo")
        imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        textLabel = self.addLabel(text = "I am a boy", row = 1, column = 0, sticky = "NSEW")
        self.image = PhotoImage(file = "example.gif")
        imageLabel["image"] = self.image
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"  
def main():
    ImageDemo().mainloop()
if __name__ == "__main__":
    main() 