# Importation de différentes bibliothèques
from tkinter import *
from random import *

#VARIABLES############################################################################################################################

(couleur)=['red','blue','yellow','white','orange','green']

# cr est l'abréviation de cube résolu.

# Définition des couleurs
red='red'
orange='orange'
white='white'
green='green'
yellow='yellow'
blue='blue'

# Définition des listes
CC=[]  # Cube en cours (non résolu)
cm1=[] # Cube après le mouvement 1



# Partie graphique :

ag= int(input(' Enter 0 for display 2D or 1 for display 3D '))

windowHeight = 800  # Windows height in pixels
windowWidth = 1100

i = int(windowHeight/12)
j = int(windowHeight/12)
x = int(windowHeight/22.5)
y = int(windowWidth/30)

window = Tk()

window.geometry(str(windowWidth)+"x"+str(windowHeight))
background = Canvas(window, width=windowWidth , heigh=windowHeight ,bg='#C7BEBE')
background.pack(side=LEFT)

#Functions############################################################################################################################


# Functions of the solved cube

def CubeResolue() :
    global cr,red,orange,white,green,yellow,blue,CC
    cr=[[[red,red,red],[red,red,red],[red,red,red]],
        [[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]],
        [[white,white,white],[white,white,white],[white,white,white]],
        [[green,green,green],[green,green,green],[green,green,green]],
        [[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]],
        [[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]]]
    CC=cr

CubeResolue ()



def AfficheGraphique ():
    global a,b,x,y

# Creation des faces avec des abréviation F pour face et C pour carré :

    F1C1=background.create_rectangle(4*i , 1*j , 5*i , 2*j ,  outline='black' , fill=CC [0] [0] [0])
    F1C2=background.create_rectangle(4*i , 2*j , 5*i , 3*j ,  outline='black' , fill=CC [0] [0] [1])
    F1C3=background.create_rectangle(4*i , 3*j , 5*i , 4*j ,  outline='black' , fill=CC [0] [0] [2])
    F1C4=background.create_rectangle(5*i , 1*j , 6*i , 2*j ,  outline='black' , fill=CC [0] [1] [0])
    F1C5=background.create_rectangle(5*i , 2*j , 6*i , 3*j ,  outline='black' , fill=CC [0] [1] [1])
    F1C6=background.create_rectangle(5*i , 3*j , 6*i , 4*j ,  outline='black' , fill=CC [0] [1] [2])
    F1C7=background.create_rectangle(6*i , 1*j , 7*i , 2*j ,  outline='black' , fill=CC [0] [2] [0])
    F1C8=background.create_rectangle(6*i , 2*j , 7*i , 3*j ,  outline='black' , fill=CC [0] [2] [1])
    F1C9=background.create_rectangle(6*i , 3*j , 7*i , 4*j ,  outline='black' , fill=CC [0] [2] [2])

# Creation face 2 :

    F2C1=background.create_rectangle(4*i , 7*j , 5*i , 8*j  , outline='black' , fill=CC [1] [0] [0])
    F2C2=background.create_rectangle(4*i , 8*j , 5*i , 9*j  , outline='black' , fill=CC [1] [0] [1])
    F2C3=background.create_rectangle(4*i , 9*j , 5*i , 10*j , outline='black' , fill=CC [1] [0] [2])
    F2C4=background.create_rectangle(5*i , 7*j , 6*i , 8*j  , outline='black' , fill=CC [1] [1] [0])
    F2C5=background.create_rectangle(5*i , 8*j , 6*i , 9*j  , outline='black' , fill=CC [1] [1] [1])
    F2C6=background.create_rectangle(5*i , 9*j , 6*i , 10*j , outline='black' , fill=CC [1] [1] [2])
    F2C7=background.create_rectangle(6*i , 7*j , 7*i , 8*j  , outline='black' , fill=CC [1] [2] [0])
    F2C8=background.create_rectangle(6*i , 8*j , 7*i , 9*j  , outline='black' , fill=CC [1] [2] [1])
    F2C9=background.create_rectangle(6*i , 9*j , 7*i , 10*j , outline='black' , fill=CC [1] [2] [2])

# Creation face 3 :

    F3C1=background.create_rectangle(1*i , 4*j , 2*i , 5*j ,  outline='black' , fill=CC [2] [0] [0])
    F3C2=background.create_rectangle(1*i , 5*j , 2*i , 6*j ,  outline='black' , fill=CC [2] [0] [1])
    F3C3=background.create_rectangle(1*i , 6*j , 2*i , 7*j ,  outline='black' , fill=CC [2] [0] [2])
    F3C4=background.create_rectangle(2*i , 4*j , 3*i , 5*j ,  outline='black' , fill=CC [2] [1] [0])
    F3C5=background.create_rectangle(2*i , 5*j , 3*i , 6*j ,  outline='black' , fill=CC [2] [1] [1])
    F3C6=background.create_rectangle(2*i , 6*j , 3*i , 7*j ,  outline='black' , fill=CC [2] [1] [2])
    F3C7=background.create_rectangle(3*i , 4*j , 4*i , 5*j ,  outline='black' , fill=CC [2] [2] [0])
    F3C8=background.create_rectangle(3*i , 5*j , 4*i , 6*j ,  outline='black' , fill=CC [2] [2] [1])
    F3C9=background.create_rectangle(3*i , 6*j , 4*i , 7*j ,  outline='black' , fill=CC [2] [2] [2])

# Creation face 4 :

    F4C1=background.create_rectangle(4*i , 4*j , 5*i , 5*j ,  outline='black' , fill=CC [3] [0] [0])
    F4C2=background.create_rectangle(4*i , 5*j , 5*i , 6*j ,  outline='black' , fill=CC [3] [0] [1])
    F4C3=background.create_rectangle(4*i , 6*j , 5*i , 7*j ,  outline='black' , fill=CC [3] [0] [2])
    F4C4=background.create_rectangle(5*i , 4*j , 6*i , 5*j ,  outline='black' , fill=CC [3] [1] [0])
    F4C5=background.create_rectangle(5*i , 5*j , 6*i , 6*j ,  outline='black' , fill=CC [3] [1] [1])
    F4C6=background.create_rectangle(5*i , 6*j , 6*i , 7*j ,  outline='black' , fill=CC [3] [1] [2])
    F4C7=background.create_rectangle(6*i , 4*j , 7*i , 5*j ,  outline='black' , fill=CC [3] [2] [0])
    F4C8=background.create_rectangle(6*i , 5*j , 7*i , 6*j ,  outline='black' , fill=CC [3] [2] [1])
    F4C9=background.create_rectangle(6*i , 6*j , 7*i , 7*j ,  outline='black' , fill=CC [3] [2] [2])

# Creation face 5 :

    F5C1=background.create_rectangle(7*i , 4*j , 8*i , 5*j ,  outline='black' , fill=CC [4] [0] [0])
    F5C2=background.create_rectangle(7*i , 5*j , 8*i , 6*j ,  outline='black' , fill=CC [4] [0] [1])
    F5C3=background.create_rectangle(7*i , 6*j , 8*i , 7*j ,  outline='black' , fill=CC [4] [0] [2])
    F5C4=background.create_rectangle(8*i , 4*j , 9*i , 5*j ,  outline='black' , fill=CC [4] [1] [0])
    F5C5=background.create_rectangle(8*i , 5*j , 9*i , 6*j ,  outline='black' , fill=CC [4] [1] [1])
    F5C6=background.create_rectangle(8*i , 6*j , 9*i , 7*j ,  outline='black' , fill=CC [4] [1] [2])
    F5C7=background.create_rectangle(9*i , 4*j , 10*i , 5*j , outline='black' , fill=CC [4] [2] [0])
    F5C8=background.create_rectangle(9*i , 5*j , 10*i , 6*j , outline='black' , fill=CC [4] [2] [1])
    F5C9=background.create_rectangle(9*i , 6*j , 10*i , 7*j , outline='black' , fill=CC [4] [2] [2])
    
# Creation face 6 :

    F6C1=background.create_rectangle(10*i , 4*j , 11*i , 5*j ,outline='black' , fill=CC [5] [0] [0])
    F6C2=background.create_rectangle(10*i , 5*j , 11*i , 6*j ,outline='black' , fill=CC [5] [0] [1])
    F6C3=background.create_rectangle(10*i , 6*j , 11*i , 7*j ,outline='black' , fill=CC [5] [0] [2])
    F6C4=background.create_rectangle(11*i , 4*j , 12*i , 5*j ,outline='black' , fill=CC [5] [1] [0])
    F6C5=background.create_rectangle(11*i , 5*j , 12*i , 6*j ,outline='black' , fill=CC [5] [1] [1])
    F6C6=background.create_rectangle(11*i , 6*j , 12*i , 7*j ,outline='black' , fill=CC [5] [1] [2])
    F6C7=background.create_rectangle(12*i , 4*j , 13*i , 5*j ,outline='black' , fill=CC [5] [2] [0])
    F6C8=background.create_rectangle(12*i , 5*j , 13*i , 6*j ,outline='black' , fill=CC [5] [2] [1])
    F6C9=background.create_rectangle(12*i , 6*j , 13*i , 7*j ,outline='black' , fill=CC [5] [2] [2])


# Fonction permettant l'affichage du Rubik's Cube en 3D

def AfficheGraphique3D ():
    
    c = 2*x
    d = 2*y
    
# Creation des faces avec des abréviation F pour face et C pour carré :

    F1C1=background.create_polygon(c+4.32*x ,  d+2*y ,     c+2.66*x ,  d+2.66*y , c+1*x ,    d+2*y ,    c+2.66*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [0] [0])
    F1C2=background.create_polygon(c+5.98*x ,  d+2.66*y ,  c+4.32*x ,  d+3.33*y , c+2.66*x , d+2.66*y , c+4.32*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [0] [1])
    F1C3=background.create_polygon(c+7.66*x ,  d+3.34*y ,  c+6*x ,     d+4*y ,    c+4.32*x , d+3.33*y , c+5.98*x ,    d+2.66*y  ,outline='black' ,  fill=CC [0] [0] [2])
    F1C4=background.create_polygon(c+5.98*x ,  d+1.34*y ,  c+4.32*x ,  d+2*y ,    c+2.66*x , d+1.34*y , c+4.32*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [1] [0])
    F1C5=background.create_polygon(c+7.66*x ,  d+2*y ,     c+5.98*x ,  d+2.66*y , c+4.32*x , d+2*y ,    c+5.98*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [1] [1])
    F1C6=background.create_polygon(c+9.32*x ,  d+2.67*y ,  c+7.66*x ,  d+3.34*y , c+5.98*x , d+2.66*y , c+7.64*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [1] [2])
    F1C7=background.create_polygon(c+7.66*x ,  d+0.66*y ,  c+5.98*x ,  d+1.34*y , c+4.32*x , d+0.67*y , c+6*x ,       d+0*y     ,outline='black' ,  fill=CC [0] [2] [0])
    F1C8=background.create_polygon(c+9.32*x ,  d+1.33*y ,  c+7.64*x ,  d+2*y ,    c+5.98*x , d+1.34*y , c+7.66*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [2] [1])
    F1C9=background.create_polygon(c+11*x ,    d+2*y ,     c+9.32*x ,  d+2.67*y , c+7.64*x , d+2*y ,    c+9.32*x ,    d+1.33*y  ,outline='black' ,  fill=CC [0] [2] [2])

# Creation face 2 :

    F2C1=background.create_polygon(c+22*x ,    d+2*y ,     c+20.32*x , d+2.67*y , c+18.64*x , d+2*y ,    c+20.32*x ,  d+1.33*y  ,outline='black' ,  fill=CC [1] [0] [0])
    F2C2=background.create_polygon(c+20.32*x , d+2.67*y ,  c+18.66*x , d+3.34*y , c+16.98*x , d+2.66*y , c+18.64*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [1] [0])
    F2C3=background.create_polygon(c+18.66*x , d+3.34*y ,  c+17*x ,    d+4*y ,    c+15.32*x , d+3.33*y , c+16.98*x ,  d+2.66*y  ,outline='black' ,  fill=CC [1] [2] [0])
    F2C4=background.create_polygon(c+20.32*x , d+1.33*y ,  c+18.64*x , d+2*y ,    c+16.98*x , d+1.34*y , c+18.66*x ,  d+0.66*y  ,outline='black' ,  fill=CC [1] [0] [1])
    F2C5=background.create_polygon(c+18.66*x , d+2*y ,     c+16.98*x , d+2.66*y , c+15.32*x , d+2*y ,    c+16.98*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [1] [1])
    F2C6=background.create_polygon(c+16.98*x , d+2.66*y ,  c+15.32*x , d+3.33*y , c+13.66*x , d+2.66*y , c+15.32*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [2] [1])
    F2C7=background.create_polygon(c+18.66*x , d+0.66*y ,  c+16.98*x , d+1.34*y , c+15.32*x , d+0.67*y , c+17*x ,     d+0*y     ,outline='black' ,  fill=CC [1] [0] [2])
    F2C8=background.create_polygon(c+16.98*x , d+1.34*y ,  c+15.32*x , d+2*y ,    c+13.66*x , d+1.34*y , c+15.32*x ,  d+0.67*y  ,outline='black' ,  fill=CC [1] [1] [2])
    F2C9=background.create_polygon(c+15.32*x , d+2*y ,     c+13.66*x , d+2.66*y , c+12*x ,    d+2*y ,    c+13.66*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [2] [2])    


# Creation face 3 :

    F3C1=background.create_polygon(c+2.66*x ,  d+5.03*y ,  c+1*x ,     d+4.36*y ,  c+1*x ,    d+2*y ,    c+2.66*x ,   d+2.66*y  ,outline='black' ,  fill=CC [2] [0] [0])
    F3C2=background.create_polygon(c+2.66*x ,  d+7.36*y ,  c+1*x ,     d+6.66*y ,  c+1*x ,    d+4.36*y , c+2.66*x ,   d+5.03*y  ,outline='black' ,  fill=CC [2] [0] [1])
    F3C3=background.create_polygon(c+2.66*x ,  d+9.66*y ,  c+1*x ,     d+9*y ,     c+1*x ,    d+6.66*y , c+2.66*x ,   d+7.32*y  ,outline='black' ,  fill=CC [2] [0] [2])
    F3C4=background.create_polygon(c+4.32*x ,  d+5.69*y ,  c+2.66*x ,  d+5.03*y ,  c+2.66*x , d+2.66*y , c+4.32*x ,   d+3.33*y  ,outline='black' ,  fill=CC [2] [1] [0])
    F3C5=background.create_polygon(c+4.32*x ,  d+8.02*y ,  c+2.66*x ,  d+7.36*y ,  c+2.66*x , d+5.03*y , c+4.32*x ,   d+5.69*y  ,outline='black' ,  fill=CC [2] [1] [1])
    F3C6=background.create_polygon(c+4.32*x ,  d+10.33*y , c+2.66*x ,  d+9.66*y ,  c+2.66*x , d+7.36*y , c+4.32*x ,   d+8.02*y  ,outline='black' ,  fill=CC [2] [1] [2])
    F3C7=background.create_polygon(c+6*x ,     d+6.33*y ,  c+4.32*x ,  d+5.69*y ,  c+4.32*x , d+3.33*y , c+6*x ,      d+4*y     ,outline='black' ,  fill=CC [2] [2] [0])
    F3C8=background.create_polygon(c+6*x ,     d+8.66*y ,  c+4.32*x ,  d+8.02*y ,  c+4.32*x , d+5.69*y , c+6*x ,      d+6.33*y  ,outline='black' ,  fill=CC [2] [2] [1])
    F3C9=background.create_polygon(c+6*x ,     d+11*y ,    c+4.32*x ,  d+10.33*y , c+4.32*x , d+8.02*y , c+6*x ,      d+8.66*y  ,outline='black' ,  fill=CC [2] [2] [2])      

# Creation face 4 :

    F4C1=background.create_polygon(c+7.66*x ,  d+5.69*y ,  c+6*x ,     d+6.33*y ,   c+6*x ,    d+4*y ,    c+7.66*x ,  d+3.33*y  ,outline='black' ,  fill=CC [3] [0] [0])
    F4C2=background.create_polygon(c+7.66*x ,  d+8.02*y ,  c+6*x ,     d+8.66*y ,   c+6*x,     d+6.33*y , c+7.66*x,   d+5.69*y  ,outline='black' ,  fill=CC [3] [0] [1])
    F4C3=background.create_polygon(c+7.66*x ,  d+10.33*y , c+6*x ,     d+11*y ,     c+6*x ,    d+8.66*y , c+7.66*x ,  d+8.02*y  ,outline='black' ,  fill=CC [3] [0] [2])
    F4C4=background.create_polygon(c+9.32*x ,  d+5.04*y ,  c+7.66*x ,  d+5.7*y ,    c+7.66*x , d+3.34*y , c+9.32*x ,  d+2.67*y  ,outline='black' ,  fill=CC [3] [1] [0])
    F4C5=background.create_polygon(c+9.32*x ,  d+7.34*y ,  c+7.66*x ,  d+8*y ,      c+7.66*x , d+5.7*y ,  c+9.32*x ,  d+5.04*y  ,outline='black' ,  fill=CC [3] [1] [1])
    F4C6=background.create_polygon(c+9.32*x ,  d+9.67*y ,  c+7.66*x ,  d+10.33*y ,  c+7.66*x , d+8*y ,    c+9.32*x ,  d+7.33*y  ,outline='black' ,  fill=CC [3] [1] [2])
    F4C7=background.create_polygon(c+11*x ,    d+4.36*y ,  c+9.32*x ,  d+5.04*y ,   c+9.32*x , d+2.67*y , c+11*x ,    d+2*y     ,outline='black' ,  fill=CC [3] [2] [0])
    F4C8=background.create_polygon(c+11*x ,    d+6.67*y ,  c+9.32*x ,  d+7.34*y ,   c+9.32*x , d+5.04*y , c+11*x ,    d+4.36*y  ,outline='black' ,  fill=CC [3] [2] [1])
    F4C9=background.create_polygon(c+11*x ,    d+9*y ,     c+9.32*x ,  d+9.67*y ,   c+9.32*x , d+7.33*y , c+11*x ,    d+6.66*y  ,outline='black' ,  fill=CC [3] [2] [2])
  
# Creation face 5   :

    F5C1=background.create_polygon(c+18.66*x , d+5.66*y ,  c+17*x ,    d+6.33*y ,  c+17*x ,    d+4*y ,    c+18.66*x , d+3.33*y  ,outline='black' ,  fill=CC [5] [0] [0])
    F5C2=background.create_polygon(c+18.66*x , d+8*y ,     c+17*x ,    d+8.66*y ,  c+17*x ,    d+6.33*y , c+18.66*x , d+5.66*y  ,outline='black' ,  fill=CC [5] [0] [1])
    F5C3=background.create_polygon(c+18.66*x , d+10.33*y , c+17*x ,    d+11*y ,    c+17*x ,    d+8.66*y , c+18.66*x , d+8*y     ,outline='black' ,  fill=CC [5] [0] [2])
    F5C4=background.create_polygon(c+20.32*x , d+5*y ,     c+18.66*x , d+5.66*y ,  c+18.66*x , d+3.33*y , c+20.32*x , d+2.66*y  ,outline='black' ,  fill=CC [5] [1] [0])
    F5C5=background.create_polygon(c+20.32*x , d+7.33*y ,  c+18.66*x , d+8*y ,     c+18.66*x , d+5.66*y , c+20.32*x , d+5*y     ,outline='black' ,  fill=CC [5] [1] [1])
    F5C6=background.create_polygon(c+20.32*x , d+9.66*y ,  c+18.66*x , d+10.33*y , c+18.66*x , d+8*y ,    c+20.32*x , d+7.33*y  ,outline='black' ,  fill=CC [5] [1] [2])
    F5C7=background.create_polygon(c+22*x ,    d+4.36*y ,  c+20.32*x , d+5*y ,     c+20.32*x , d+2.66*y , c+22*x ,    d+2*y     ,outline='black' ,  fill=CC [5] [2] [0])
    F5C8=background.create_polygon(c+22*x ,    d+6.66*y ,  c+20.32*x , d+7.33*y ,  c+20.32*x , d+5*y ,    c+22*x ,    d+4.36*y  ,outline='black' ,  fill=CC [5] [2] [1])
    F5C9=background.create_polygon(c+22*x ,    d+9*y ,     c+20.32*x , d+9.66*y ,  c+20.32*x , d+7.33*y , c+22*x ,    d+6.66*y  ,outline='black' ,  fill=CC [5] [2] [2])
# Creation face 6 :

    F6C1=background.create_polygon(c+13.66*x , d+5*y ,     c+12*x ,    d+4.36*y ,  c+12*x ,    d+2*y ,    c+13.66*x , d+2.66*y  ,outline='black' ,  fill=CC [4] [2] [0])
    F6C2=background.create_polygon(c+13.66*x , d+7.32*y ,  c+12*x ,    d+6.66*y ,  c+12*x ,    d+4.36*y , c+13.66*x , d+5*y     ,outline='black' ,  fill=CC [4] [2] [1]) 
    F6C3=background.create_polygon(c+13.66*x , d+9.66*y ,  c+12*x ,    d+9*y ,     c+12*x ,    d+6.66*y , c+13.66*x , d+7.32*y  ,outline='black' ,  fill=CC [4] [2] [2])
    F6C4=background.create_polygon(c+15.32*x , d+5.66*y ,  c+13.66*x , d+5*y ,     c+13.66*x , d+2.66*y , c+15.32*x , d+3.33*y  ,outline='black' ,  fill=CC [4] [1] [0])
    F6C5=background.create_polygon(c+15.32*x , d+8*y ,     c+13.66*x , d+7.32*y ,  c+13.66*x , d+5*y ,    c+15.32*x , d+5.66*y  ,outline='black' ,  fill=CC [4] [1] [1])  
    F6C6=background.create_polygon(c+15.32*x , d+10.33*y , c+13.66*x , d+9.66*y ,  c+13.66*x , d+7.32*y , c+15.32*x , d+8*y     ,outline='black' ,  fill=CC [4] [1] [2])
    F6C7=background.create_polygon(c+17*x ,    d+6.33*y ,  c+15.32*x , d+5.66*y ,  c+15.32*x , d+3.33*y , c+17*x ,    d+4*y     ,outline='black' ,  fill=CC [4] [0] [0])
    F6C8=background.create_polygon(c+17*x ,    d+8.66*y ,  c+15.32*x , d+8*y ,     c+15.32*x , d+5.66*y , c+17*x ,    d+6.33*y  ,outline='black' ,  fill=CC [4] [0] [1])
    F6C9=background.create_polygon(c+17*x ,    d+11*y ,    c+15.32*x , d+10.33*y , c+15.32*x , d+8*y ,    c+17*x ,    d+8.66*y  ,outline='black' ,  fill=CC [4] [0] [2])


    
# Fonctions définissant les mouvements.


def Opt_Affichage () :

    if ag == 0 :
        AfficheGraphique ()
    elif ag == 1 :
        AfficheGraphique3D ()

# Cette fonction effectue un mouvement vers l'avant de la première colonne.
def Mvt1():
    global CC,cm1
    cm1=[[[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]], 
         [[CC[5][2][2],CC[5][2][1],CC[5][2][0]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][2][0],CC[2][1][0],CC[2][0][0]],[CC[2][2][1],CC[2][1][1],CC[2][0][1]],[CC[2][2][2],CC[2][1][2],CC[2][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[0][0][2],CC[0][0][1],CC[0][0][0]]]]

    CC=cm1

    Opt_Affichage ()
    

# Cette fonction effectue un mouvement vers l'arrière de la première colonne.
def Mvt2():
    global CC,cm2
    
    cm2=[[[CC[5][2][0],CC[5][2][1],CC[5][2][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][2],CC[2][1][2],CC[2][2][2]],[CC[2][0][1],CC[2][1][1],CC[2][2][1]],[CC[2][0][0],CC[2][1][0],CC[2][2][0]]],
         [[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[1][0][0],CC[1][0][1],CC[1][0][2]]]]
    CC=cm2

    Opt_Affichage ()
        
# Mvt3 correspond au mouvement vers l'avant de la 2ème colonne.
def Mvt3():
    global CC,cm3
    cm3=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[5][1][2],CC[5][1][1],CC[5][1][0]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[0][1][2],CC[0][1][1],CC[0][1][0]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm3

    Opt_Affichage ()
        
# Mvt4 correspond au mouvement vers l'arrière de la 2ème colonne.

def Mvt4():
    global CC,cm4

    cm4=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]], 
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm4

    Opt_Affichage ()
        

# Mvt5 correspond au mouvement vers l'avant de la 3ème colonne.
def Mvt5 ():
    global CC ,cm5
    cm5=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[4][0][2],CC[4][1][2],CC[4][2][2]],[CC[4][0][1],CC[4][1][1],CC[4][2][1]],[CC[4][0][0],CC[4][1][0],CC[4][2][0]]],
         [[CC[0][2][2],CC[0][2][1],CC[0][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm5

    Opt_Affichage ()
        

# Mvt6 correspond au mouvement vers l'arrière de la 3ème colonne.
def Mvt6():
   global CC,cm6
   cm6=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
        [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
        [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
        [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
        [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
        [[CC[1][2][2],CC[1][2][1],CC[1][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
   CC=cm6

   Opt_Affichage ()
    
# Mvt7 correspond au mouvement vers la gauche de la 1ère ligne.
def Mvt7():
    global CC ,cm7
    cm7=[[[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[0][0][1],CC[0][1][1],CC[0][2][1]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[3][0][0],CC[2][0][1],CC[2][0][2]],[CC[3][1][0],CC[2][1][1],CC[2][1][2]],[CC[3][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[4][0][0],CC[3][0][1],CC[3][0][2]],[CC[4][1][0],CC[3][1][1],CC[3][1][2]],[CC[4][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[5][0][0],CC[4][0][1],CC[4][0][2]],[CC[5][1][0],CC[4][1][1],CC[4][1][2]],[CC[5][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[2][0][0],CC[5][0][1],CC[5][0][2]],[CC[2][1][0],CC[5][1][1],CC[5][1][2]],[CC[2][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm7

    Opt_Affichage ()


# Mvt8 correspond au mouvement vers la droite de la 1ère ligne.
def Mvt8():
    global CC ,cm8
    cm8=[[[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[0][2][1],CC[0][1][1],CC[0][0][1]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[5][0][0],CC[2][0][1],CC[2][0][2]],[CC[5][1][0],CC[2][1][1],CC[2][1][2]],[CC[5][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[2][0][0],CC[3][0][1],CC[3][0][2]],[CC[2][1][0],CC[3][1][1],CC[3][1][2]],[CC[2][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[3][0][0],CC[4][0][1],CC[4][0][2]],[CC[3][1][0],CC[4][1][1],CC[4][1][2]],[CC[3][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[4][0][0],CC[5][0][1],CC[5][0][2]],[CC[4][1][0],CC[5][1][1],CC[5][1][2]],[CC[4][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm8

    Opt_Affichage ()
        

 #Mvt9 correspond au mouvement vers la gauche de la 2ème ligne.
def Mvt9():
    global CC ,cm9
    cm9=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[3][0][1],CC[2][0][2]],[CC[2][1][0],CC[3][1][1],CC[2][1][2]],[CC[2][2][0],CC[3][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[4][0][1],CC[3][0][2]],[CC[3][1][0],CC[4][1][1],CC[3][1][2]],[CC[3][2][0],CC[4][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[5][0][1],CC[4][0][2]],[CC[4][1][0],CC[5][1][1],CC[4][1][2]],[CC[4][2][0],CC[5][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[2][0][1],CC[5][0][2]],[CC[5][1][0],CC[2][1][1],CC[5][1][2]],[CC[5][2][0],CC[2][2][1],CC[5][2][2]]]]
    CC=cm9

    Opt_Affichage ()
        

# Mvt 10 correspond au mouvement vers la droite de la 2ème ligne.
def Mvt10():
    global CC ,cm10
    cm10=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[5][0][1],CC[2][0][2]],[CC[2][1][0],CC[5][1][1],CC[2][1][2]],[CC[2][2][0],CC[5][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[2][0][1],CC[3][0][2]],[CC[3][1][0],CC[2][1][1],CC[3][1][2]],[CC[3][2][0],CC[2][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[3][0][1],CC[4][0][2]],[CC[4][1][0],CC[3][1][1],CC[4][1][2]],[CC[4][2][0],CC[3][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[4][0][1],CC[5][0][2]],[CC[5][1][0],CC[4][1][1],CC[5][1][2]],[CC[5][2][0],CC[4][2][1],CC[5][2][2]]]]
    CC=cm10

    Opt_Affichage ()
    

# Mvt 11 correspond au mouvement vers la gauche de la 3ème ligne.
def Mvt11():
    global CC ,cm11
    cm11=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[1][2][1],CC[1][1][1],CC[1][0][1]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[3][0][2]],[CC[2][1][0],CC[2][1][1],CC[3][1][2]],[CC[2][2][0],CC[2][2][1],CC[3][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[4][0][2]],[CC[3][1][0],CC[3][1][1],CC[4][1][2]],[CC[3][2][0],CC[3][2][1],CC[4][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[5][0][2]],[CC[4][1][0],CC[4][1][1],CC[5][1][2]],[CC[4][2][0],CC[4][2][1],CC[5][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[2][0][2]],[CC[5][1][0],CC[5][1][1],CC[2][1][2]],[CC[5][2][0],CC[5][2][1],CC[2][2][2]]]]
    CC=cm11

    Opt_Affichage ()
      

# Mvt 12 correspond au mouvement vers la droite de la 3ème ligne.
def Mvt12():
    global CC ,cm12
    cm12=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[1][0][1],CC[1][1][1],CC[1][2][1]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[2][0][0],CC[2][0][1],CC[5][0][2]],[CC[2][1][0],CC[2][1][1],CC[5][1][2]],[CC[2][2][0],CC[2][2][1],CC[5][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[2][0][2]],[CC[3][1][0],CC[3][1][1],CC[2][1][2]],[CC[3][2][0],CC[3][2][1],CC[2][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[3][0][2]],[CC[4][1][0],CC[4][1][1],CC[3][1][2]],[CC[4][2][0],CC[4][2][1],CC[3][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[4][0][2]],[CC[5][1][0],CC[5][1][1],CC[4][1][2]],[CC[5][2][0],CC[5][2][1],CC[4][2][2]]]]
    CC=cm12

    Opt_Affichage ()
     

def Mvt13():
    global CC,cm13
    cm13=[[[CC[4][2][0],CC[0][0][1],CC[0][0][2]],[CC[4][2][1],CC[0][1][1],CC[0][1][2]],[CC[4][2][2],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[2][0][0]],[CC[1][1][0],CC[1][1][1],CC[2][0][1]],[CC[1][2][0],CC[1][2][1],CC[2][0][2]]],
          [[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[5][0][2],CC[5][1][2],CC[5][2][2]],[CC[5][0][1],CC[5][1][1],CC[5][2][1]],[CC[5][0][0],CC[5][1][0],CC[5][2][0]]]]
    CC=cm13

    Opt_Affichage ()     
        
def Mvt14():
    global CC,cm14
    cm14=[[[CC[2][0][2],CC[0][0][1],CC[0][0][2]],[CC[2][0][1],CC[0][1][1],CC[0][1][2]],[CC[2][0][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[4][2][2]],[CC[1][1][0],CC[1][1][1],CC[4][2][1]],[CC[1][2][0],CC[1][2][1],CC[4][2][0]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
          [[CC[5][2][0],CC[5][1][0],CC[5][0][0]],[CC[5][2][1],CC[5][1][1],CC[5][0][1]],[CC[5][2][2],CC[5][1][2],CC[5][0][2]]]]
    CC=cm14

    Opt_Affichage ()
  
        
def Mvt15():
    global CC,cm15
    cm15=[[[CC[0][0][0],CC[4][1][0],CC[0][0][2]],[CC[0][1][0],CC[4][1][1],CC[0][1][2]],[CC[0][2][0],CC[4][1][2],CC[0][2][2]]],
          [[CC[1][0][0],CC[2][1][0],CC[1][0][2]],[CC[1][1][0],CC[2][1][1],CC[1][1][2]],[CC[1][2][0],CC[2][1][2],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[0][2][1],CC[0][1][1],CC[0][0][1]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[1][2][1],CC[1][1][1],CC[1][0][1]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm15

    Opt_Affichage ()    
        

def Mvt16():
    global CC,cm16
    cm16=[[[CC[0][0][0],CC[2][1][2],CC[0][0][2]],[CC[0][1][0],CC[2][1][1],CC[0][1][2]],[CC[0][2][0],CC[2][1][0],CC[0][2][2]]],
          [[CC[1][0][0],CC[4][1][2],CC[1][0][2]],[CC[1][1][0],CC[4][1][1],CC[1][1][2]],[CC[1][2][0],CC[4][1][0],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[1][0][1],CC[1][1][1],CC[1][2][1]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[0][0][1],CC[0][1][1],CC[0][2][1]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm16

    Opt_Affichage ()
    

def Mvt17():
    global CC,cm17
    cm17=[[[CC[0][0][0],CC[0][0][1],CC[4][0][0]],[CC[0][1][0],CC[0][1][1],CC[4][0][1]],[CC[0][2][0],CC[0][2][1],CC[4][0][2]]],
          [[CC[2][2][0],CC[1][0][1],CC[1][0][2]],[CC[2][2][1],CC[1][1][1],CC[1][1][2]],[CC[2][2][2],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
          [[CC[3][2][0],CC[3][1][0],CC[3][0][0]],[CC[3][2][1],CC[3][1][1],CC[3][0][1]],[CC[3][2][2],CC[3][1][2],CC[3][0][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm17

    Opt_Affichage ()


def Mvt18():
    global CC,cm18
    cm18=[[[CC[0][0][0],CC[0][0][1],CC[2][2][2]],[CC[0][1][0],CC[0][1][1],CC[2][2][1]],[CC[0][2][0],CC[0][2][1],CC[2][2][0]]],
          [[CC[4][0][2],CC[1][0][1],CC[1][0][2]],[CC[4][0][1],CC[1][1][1],CC[1][1][2]],[CC[4][0][0],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[3][0][2],CC[3][1][2],CC[3][2][2]],[CC[3][0][1],CC[3][1][1],CC[3][2][1]],[CC[3][0][0],CC[3][1][0],CC[3][2][0]]],
          [[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm18

    Opt_Affichage ()
    

#BOUTONS 

# Création des boutons permettant les mouvements.

def Boutons():
     
    Bmvt1 = Button(window, text="Mvt1", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt1 , image = photo)
    Bmvt1_window = background.create_window(x+260, y-10, window=Bmvt1)

    Bmvt2 = Button(window, text="Mvt2", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt2 , image = photo2)
    Bmvt2_window = background.create_window(x+260, 700, window=Bmvt2)

    Bmvt3 = Button(window, text="Mvt3", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt3 , image = photo)
    Bmvt3_window = background.create_window(x+325, y-10, window=Bmvt3)
    
    Bmvt4 = Button(window, text="Mvt4", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt4 , image = photo2)
    Bmvt4_window = background.create_window(x+325, 700, window=Bmvt4)

    Bmvt5 = Button(window, text="Mvt5", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt5 , image = photo)
    Bmvt5_window = background.create_window(x+390, y-10 , window=Bmvt5)
    
    Bmvt6 = Button(window, text="Mvt6", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt6 , image = photo2)
    Bmvt6_window = background.create_window(x+390, 700 , window=Bmvt6)

    Bmvt7 = Button(window, text="Mvt7", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt7 , image = photo3)
    Bmvt7_window = background.create_window(x-5, 300, window=Bmvt7)

    Bmvt8 = Button(window, text="Mvt8", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt8 , image = photo1)
    Bmvt8_window = background.create_window(x+860, 300 , window=Bmvt8)

    Bmvt9 = Button(window, text="Mvt9", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt9 , image = photo3)
    Bmvt9_window = background.create_window(x-5, 360, window=Bmvt9)

    Bmvt10 = Button(window, text="Mvt10", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt10 , image = photo1)
    Bmvt10_window = background.create_window(x+860, 360, window=Bmvt10)

    Bmvt11 = Button(window, text="Mvt11", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt11 , image = photo3)
    Bmvt11_window = background.create_window(x-5, 420, window=Bmvt11)

    Bmvt12 = Button(window, text="Mvt12", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt12 , image = photo1)
    Bmvt12_window = background.create_window(x+860 , 420, window=Bmvt12)

    Bmvt13 = Button(window, text="Mvt13", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt13 , image = photo1)
    Bmvt13_window = background.create_window(x+470 , 625, window=Bmvt13)

    Bmvt14 = Button(window, text="Mvt14", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt14 , image = photo3)
    Bmvt14_window = background.create_window(x+180, 625, window=Bmvt14)

    Bmvt15 = Button(window, text="Mvt15", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt15 , image = photo1)
    Bmvt15_window = background.create_window(x+470 , 560, window=Bmvt15)

    Bmvt16 = Button(window, text="Mvt16", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt16 , image = photo3)
    Bmvt16_window = background.create_window(x+180 , 560, window=Bmvt16)

    Bmvt17 = Button(window, text="Mvt17", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt17 , image = photo1)
    Bmvt17_window = background.create_window(x+470 , 500, window=Bmvt17)

    Bmvt18 = Button(window, text="Mvt18", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt18 , image = photo3)
    Bmvt18_window = background.create_window(x+180 , 500, window=Bmvt18) 


def Boutons_3D():
     
    Bmvt1 = Button(window, text="Mvt1", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt1 , image = photo)
    Bmvt1_window = background.create_window(3.5*x, 105, window=Bmvt1)

    Bmvt2 = Button(window, text="Mvt2", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt2 , image = photo2)
    Bmvt2_window = background.create_window(23.25*x, 430, window=Bmvt2)

    Bmvt3 = Button(window, text="Mvt3", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt3 , image = photo)
    Bmvt3_window = background.create_window(5.25*x, 80, window=Bmvt3)
    
    Bmvt4 = Button(window, text="Mvt4", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt4 , image = photo2)
    Bmvt4_window = background.create_window(21.5*x, 455, window=Bmvt4)

    Bmvt5 = Button(window, text="Mvt5", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt5 , image = photo)
    Bmvt5_window = background.create_window(7*x, 55 , window=Bmvt5)
    
    Bmvt6 = Button(window, text="Mvt6", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt6 , image = photo2)
    Bmvt6_window = background.create_window(20*x, 475 , window=Bmvt6)

    Bmvt7 = Button(window, text="Mvt7", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt7 , image = photo3)
    Bmvt7_window = background.create_window(2*x, 180, window=Bmvt7)

    Bmvt8 = Button(window, text="Mvt8", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt8 , image = photo1)
    Bmvt8_window = background.create_window(25*x, 180 , window=Bmvt8)

    Bmvt9 = Button(window, text="Mvt9", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt9 , image = photo3)
    Bmvt9_window = background.create_window(2*x, 265, window=Bmvt9)

    Bmvt10 = Button(window, text="Mvt10", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt10 , image = photo1)
    Bmvt10_window = background.create_window(25*x, 265, window=Bmvt10)

    Bmvt11 = Button(window, text="Mvt11", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt11 , image = photo3)
    Bmvt11_window = background.create_window(2*x, 350, window=Bmvt11)

    Bmvt12 = Button(window, text="Mvt12", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt12 , image = photo1)
    Bmvt12_window = background.create_window(25*x , 350, window=Bmvt12)

    Bmvt13 = Button(window, text="Mvt13", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt13 , image = photo2)
    Bmvt13_window = background.create_window(3.5*x , 460, window=Bmvt13)

    Bmvt14 = Button(window, text="Mvt14", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt14 , image = photo)
    Bmvt14_window = background.create_window(20*x, 65 , window=Bmvt14)

    Bmvt15 = Button(window, text="Mvt15", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt15 , image = photo2)
    Bmvt15_window = background.create_window(5.25*x , 480, window=Bmvt15)

    Bmvt16 = Button(window, text="Mvt16", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt16 , image = photo)
    Bmvt16_window = background.create_window(21.5*x , 85, window=Bmvt16)

    Bmvt17 = Button(window, text="Mvt17", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt17 , image = photo2)
    Bmvt17_window = background.create_window(7*x , 500, window=Bmvt17)

    Bmvt18 = Button(window, text="Mvt18", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt18 , image = photo)
    Bmvt18_window = background.create_window(23.25*x , 108, window=Bmvt18) 

        
# Définition des fléches.
photo = PhotoImage(file='arrow1.png')
photo1 = PhotoImage(file='arrowdroite.png')
photo2 = PhotoImage(file='arrowbas.png')
photo3 = PhotoImage(file='arrowgauche.png')


# Création du bouton permettant de fermer la fenêtre.
fermer = Button(window, text="Exit", bg='SlateGray1' , bd= 10 , activebackground ='red',command=window.destroy)
fermer_window = background.create_window(40, 20, window=fermer)

# Titre
phrase = Label(background, text="RUBIKS CUBE :)", fg='black' , bg ='#C7BEBE' , font= "Chicago")
phrase.pack()
background.create_window(700, 590, window=phrase)

#MAINS################################################################################################################################



if ag == 0 :
        AfficheGraphique (),Boutons()
elif ag == 1 :
        AfficheGraphique3D (),Boutons_3D()

window.mainloop()

