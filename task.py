import playsound as p
import tkinter as tk

'''
list of sound effects:
lobotomy buzz
'''
def lobotomy(event):
    print(event)
    p.playsound("lobotomy-sound-effect.mp3", block=False)
def sax(event):
    print(event)
    p.playsound("brand new sax.mp3", block=False)
def banjo(event):
    print(event)
    p.playsound("banjo.mp3", block=False)
def dance(event):
    print(event)
    p.playsound("dance.mp3", block=False)
def chicken(event):
    print(event)
    p.playsound("chicken jockey.mp3", block=False)


window = tk.Tk()
window.title('SOUNDBOARD')
window.geometry('1094x325')
lobotomypic = tk.PhotoImage(file='lobotomy-icepick.png')
lobotomyfinal = lobotomypic.subsample(2,2)
druski = tk.PhotoImage(file='druski.png')
druskifinal = druski.subsample(2,2)
ashtonhall = tk.PhotoImage(file='ashton-hall.png')
ashtonhallfinal = ashtonhall.subsample(5,5)
glendo = tk.PhotoImage(file='glendo.png')
glendofinal = glendo.subsample(0,0)
chickenjockey = tk.PhotoImage(file='chicken jockey.png')
chickenjockeyfinal = chickenjockey.subsample(2,2)

lbl = tk.Label(window, text='Welcome to Lucas\' soundboard.')
button1 = tk.Button(window, image=lobotomyfinal)
button1.bind("<Button>", lobotomy)
button2 = tk.Button(window, image=druskifinal)
button2.bind("<Button>", sax)
button3 = tk.Button(window, image=ashtonhallfinal)
button3.bind("<Button>", banjo)
button4 = tk.Button(window, image=glendo)
button4.bind("<Button>", dance)
button5 = tk.Button(window, image=chickenjockeyfinal)
button5.bind("<Button>", chicken)

lbl.place(x=450,y=15)
button1.place(x=0,y=50)
button2.place(x=200,y=50)
button3.place(x=418,y=50)
button4.place(x=665,y=50)
button5.place(x=850,y=50)

window.mainloop()

#done