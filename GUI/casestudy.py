from breezypythongui import EasyFrame
class Library(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self)
        self.setSize(width=500,height=200)
        self.booklabel=self.addLabel(text="Book Title : ",row=0,column=0)
        self.booktext=self.addTextField(text="",row=0,column=1)
        self.idlabel=self.addLabel(text="Book ID : ",row=1,column=0)
        self.idnum=self.addIntegerField(value=0,row=1,column=1,columnspan=2)
        self.authorlabel=self.addLabel(text="Author Name : ",row=2,column=0)
        self.authortext=self.addTextField(text="",row=2,column=1)
        self.books=[]
        self.addbookbtn=self.addButton(text="Add Book",row=3,column=0,command=self.addbook)
        self.showbookbtn=self.addButton(text="Show Books",row=3,column=1,command=self.showbook)
    def addbook(self):
        flag=0
        author=self.authortext.getText()
        bookname=self.booktext.getText()
        bookid=self.idnum.getNumber()
        for i in self.books:
            if i["bookid"]==bookid:
                self.addLabel(text="ALREADY THIS ID PRESENT, SORRY!",row=4,column=2)
                flag=1
        if (flag==0):
            b={}
            b["author"]=author
            b["bookname"]=bookname
            b["bookid"]=bookid
            self.books.append(b)
    def showbook(self):
        k=0
        self.addLabel(text="Book Name",row=5,column=0)
        self.addLabel(text="Book ID",row=5,column=1)
        self.addLabel(text="Author",row=5,column=2)
        for j in self.books:
            self.addLabel(text=j["bookname"],row=6+k,column=0)
            self.addLabel(text=j["bookid"],row=6+k,column=1)
            self.addLabel(text=j["author"],row=6+k,column=2)
            k=k+1
            


def main():
    Library().mainloop()

if __name__=="__main__":
    main()
