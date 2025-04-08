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


window = tk.Tk()
window.title('SOUNDBOARD')

lbl = tk.Label(window, text='Welcome to Lucas\' soundboard.')
button1 = tk.Button(window, text='Lobotomy')
button1.bind("<Button>", lobotomy)
button2 = tk.Button(window, text='Sax')
button2.bind("<Button>", sax)
button3 = tk.Button(window, text='Banjo')
button3.bind("<Button>", banjo)
button4 = tk.Button(window, text='Dance')
button4.bind("<Button>", dance)

lbl.place(x=0,y=0)
button1.place(x=0,y=50)
button2.place(x=100,y=50)
button3.place(x=150,y=50)
button4.place(x=0,y=100)

window.mainloop()