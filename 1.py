#coding: utf8




dividendo=input("Escriba el dividendo:  ")
divisor=input("Escriba el divisor: ")



if (divisor==0):

    print "no se puede"
else:   
    resto= dividendo % divisor
    cociente= dividendo / divisor
   
    if ( resto==0 ):

        print ("La división es exacta. Cociente:", cociente)

    else:

        print("La division no es exacta. Cociente:", cociente , "Resto" , resto)
