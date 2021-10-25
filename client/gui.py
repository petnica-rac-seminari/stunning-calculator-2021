from tkinter import *
import tkinter
import tkinter.messagebox as mb
import os
import numpy
import image_parse
#import server_interface
import server_interface

window = Tk()
window.title('Racunajka')
window.geometry("400x503")
window.resizable(0, 0)
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
ispis = ''
def sabiranje():
     operacija = '+'
     global ispis
     ispis = ispis + operacija
     but_pos['text']= ispis
def oduzimanje():
     operacija = '-'
     global ispis
     ispis = ispis + operacija
     but_pos['text']= ispis
def mnozenje():
     operacija = '*'
     global ispis
     ispis = ispis + operacija
     but_pos['text']= ispis
def deljnje():
     operacija = '/'
     global ispis
     ispis = ispis + operacija
     but_pos['text']= ispis
#FUNKCIJA ZA SLANJE 
rezultat = 0
def slanje():        
     global ispis  
     arr = image_parse.ParseImage(nizTacaka)  
     canvas.delete('all')
     nizTacaka.clear()      

     try:
          result = server_interface.SendParsedImage(arr)               
          
          ispis = ispis + result
          but_pos['text'] = ispis

          try:
               but_rez['text'] = server_interface.evaluate(ispis)
          except:
               but_rez['text'] = 'Invalid input'
               print('failed to evalueate: ', ispis)
     except:
          print("Failed to send parsed image to server")           

def brisanje():
     global ispis
     ispis = ispis[:len(ispis)-1]
     but_pos['text'] = ispis 
     try:    
          but_rez['text'] = server_interface.evaluate(but_pos['text'])
     except:
          but_rez['text'] = 'Invalid input'
          print('failed to evalueate: ', ispis)


    
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
#BRISANJE
but_deljenje = Button(window,text='⤆', image = common_img,
width= wid ,height= hei, bd = 3,
compound="c",bg='red',fg='white',
font= ("Verdana" , 27,'bold'),
command= brisanje
)
but_deljenje.place(x =prvax, y= prvay+423)

#ISPIS REZULTATA
but_rez = Button(window,text=rezultat, image = common_img,
width= 337 ,height= 80, bd = 0,
compound="c",bg='white',fg='black',
font= ("Verdana" , 27,'bold'),
state= DISABLED,
)
but_rez.place(x =0, y=344)
#ISPIS POSTUPAK
but_pos = Button(window,text=ispis, image = common_img,
width= 337 ,height= 80, bd = 0,
compound="c",bg='white',fg='black',
font= ("Verdana" , 20,'bold'),
state= DISABLED,
)
but_pos.place(x =0, y=424)

    

#EROR BLOK


window.mainloop()

