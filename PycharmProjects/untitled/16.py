from tkinter import *

class Page(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self,*args,**kwargs)
        label = Label(self, text="This is Page1")
        label.pack(side="top", fill="both", expand=True)

class Page2(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self,*args,**kwargs)
        label = Label(self, text="This is Page2")
        label.pack(side="top", fill="both", expand=True)

class MainView(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self, *args,**kwargs)
        p1=Page1(self)
        p2=Page2(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container,x=0,y=0,relwidth=1,relheight=1)
        p2.place(in_=container,x=0,y=0,relwidth=1,relheight=1)

        b1=Button(buttonframe, text="Page 1", command=p1.lift)
        b2=Button(buttonframe, text="Page 2", command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root= Tk()
    main = MainView(root)
    main.pack(side="top",fill="both",expand=True)
    root.wm_geometry()
    root.mainloop()