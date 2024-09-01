from tkinter import *

#Creating a window:
win = Tk()

#Window Customization:
win.geometry('900x600')
win.minsize(900 , 600)
win.maxsize(900, 600)
win.title('Gnome Auto Theming')
win.state('normal')
win.config(background='grey')

#welcoming Label:
welcomeLabel = Label(win , text='Welcome to Gnome Auto-Theming tweaker !' , bg='grey' , font=('Courrier' , 20) , foreground='White')
welcomeLabel.pack()

#TopFrame:
topFrame = Frame(win , background='#c0c5c0')
topFrame.pack(fill=BOTH, side=TOP )

#Themes:

#whiteSur:
whiteSurFrame = Frame(topFrame , background='#c9c5b0')
whiteSurFrame.pack(padx=5 , side=LEFT)

whiteSurLabel = Label(whiteSurFrame , text='WhiteSur' , bg='#c9c5b0' , font=('Courrier' , 17))
whiteSurLabel.pack()

whiteSurIconsButton = Button(whiteSurFrame , text='Icons' , bg='White' , foreground='Black' , font=("Courrier" , 15))
whiteSurThemesButton = Button(whiteSurFrame , text='Themes' , bg='White' , foreground='Black' , font=("Courrier" , 15))

whiteSurThemesButton.pack()
whiteSurIconsButton.pack()

#Orchis:
OrchisFrame = Frame(topFrame , background='#c9c5b0')
OrchisFrame.pack(padx=5 , side=LEFT)

OrchisLabel = Label(OrchisFrame, text='Orchis' , bg='#c9c5b0' , font=('Courrier' , 17))
OrchisLabel.pack()

OrchisIconsButton = Button(OrchisFrame , text='Icons' , bg='White' , foreground='Black' , font=("Courrier" , 15))
OrchisThemesButton = Button(OrchisFrame , text='Themes' , bg='White' , foreground='Black' , font=("Courrier" , 15))

OrchisThemesButton.pack()
OrchisIconsButton.pack()

#Vimix
vimixFrame = Frame(topFrame , background='#c9c5b0')
vimixFrame.pack(padx=5 , side=LEFT)

vimixLabel = Label(vimixFrame, text='Vimix' , bg='#c9c5b0' , font=('Courrier' , 17))
vimixLabel.pack()

vimixIconsButton = Button(vimixFrame , text='Icons' , bg='White' , foreground='Black' , font=("Courrier" , 15))
vimixThemesButton = Button(vimixFrame , text='Themes' , bg='White' , foreground='Black' , font=("Courrier" , 15))

vimixThemesButton.pack()
vimixIconsButton.pack()

#Yaru :
yaruFrame = Frame(topFrame , background='#c0c5b0')
yaruFrame.pack(padx=5 , side=LEFT)

yaruLabel = Label(yaruFrame , text='Yaru' , bg='#c0c5b0' ,font=('Courrier' , 17) , fg="Black")
yaruLabel.pack()

yaruIconsButton = Button(yaruFrame , text='Icons' ,bg='White' , foreground='Black' , font=('Courrier' , 15))
yaruThemesButton = Button(yaruFrame , text='Themes' , bg='white' , foreground='Black' , font=('Courrier' , 15))

yaruThemesButton.pack()
yaruIconsButton.pack()

#Other Theme:
themenameFrame = Frame(topFrame , background='#c0c5b0')

#Running the window (win):
win.mainloop()
