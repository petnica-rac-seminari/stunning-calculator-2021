from tkinter import *
import tkinter
import tkinter.messagebox as mb
import os
import numpy
import image_parse

window = Tk()
window.title('Racunajka')
window.geometry("400x600")
window.configure(bg='black')

#CRTANJE
current_x, current_y = 0,0
color = 'black'

nizTacaka = []
misJePritisnut = False

def mouseDown(event):
     global current_x, current_y, misJePritisnut
     misJePritisnut = True
     nizTacaka.append([])
     current_x, current_y = event.x, event.y

def mouseUp(event):
     global misJePritisnut
     misJePritisnut = False

def mouseMotion(event):

     global current_x, current_y, misJePritisnut

     if misJePritisnut and event.x > 0 and event.x < 337 and event.y > 0 and event.y < 339:

          canvas.create_line((current_x,current_y,event.x,event.y),fill = color)        

          current_x, current_y = event.x, event.y
          nizTacaka[-1].append(numpy.array([event.x, event.y]))


canvas= Canvas(window,background='white',width=337,height=339) 
canvas.place(x=0,y=0)

canvas.bind('<Button-1>', mouseDown)
canvas.bind('<ButtonRelease-1>', mouseUp)
canvas.bind('<B1-Motion>', mouseMotion)


#BUTTON
# #FUNKCIJE ZA BUTTONE
operacija =' '
def sabiranje():
     operacija = '+'
def oduzimanje():
     operacija = '-'
def mnozenje():
     operacija = '*'
def deljnje():
     operacija = '/'
#FUNKCIJA ZA SLANJE 
def slanje():          
     image_parse.ParseImage(nizTacaka)    
     nizTacaka.clear()
     canvas.delete("all")
     #print(izlaz)

    
#VELICINA
wid = 50 #sirina
hei = 80 #visina
#POZICIJA
prvax = 342
prvay = 0

#SABIRANJE
common_img = PhotoImage(width = 1 , height = 1)
but_sabiranje = Button(window,text='+', image = common_img,
width= wid ,height= hei, bd = 3,
compound="c",bg='orange',fg='white',
font= ("Verdana" , 30,'bold'),
command = sabiranje
)
but_sabiranje.place(x =prvax, y= prvay)
#ODUZIMANJE
but_oduzimanje = Button(window,text='-', image = common_img,
width= wid ,height= hei, bd = 3,
compound="c",bg='orange',fg='white',
font= ("Verdana" , 30,'bold'),
command = oduzimanje
)
but_oduzimanje.place(x =prvax, y= prvay+81)
#MNOZENJE
but_mnozenje = Button(window,text='x', image = common_img,
width= wid ,height= hei, bd = 3,
compound="c",bg='orange',fg='white',
font= ("Verdana" , 30,'bold'),
command = mnozenje
)
but_mnozenje.place(x =prvax, y= prvay+169)
#DELJENJE
but_deljenje = Button(window,text='÷', image = common_img,
width= wid ,height= hei, bd = 3,
compound="c",bg='orange',fg='white',
font= ("Verdana" , 30,'bold'),
command = deljnje
)
but_deljenje.place(x =prvax, y= prvay+255)
#SALJI
but_deljenje = Button(window,text='✓', image = common_img,
width= wid ,height= hei, bd = 3,
compound="c",bg='green',fg='white',
font= ("Verdana" , 30,'bold'),
command = slanje
)
but_deljenje.place(x =prvax, y= prvay+341)

#ISPIS IZRAZA
#myLabel1=Label(window,)

#ISPRIS REZULTATA
#Label2= Label(window,'ovde ide rezultat')
#Label2.place(x=0,y=580)
      
    

#EROR BLOK


window.mainloop()

