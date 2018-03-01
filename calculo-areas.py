#coding: utf-8

from math import pi

print"""
  Calculadora de areas
  --------------------
- Triangulo
- Circulo

"""

menu = raw_input("Escriba T o C:    ")


if (menu == "T"):
    base=input ("Introduce la base:  ")
    altura=input ("Introduce la altura:   ")

    if base <0 or altura <0 :
        print "Negativo no"

    else:
        resultat= base*altura / 2
        print"Un triangulo de base:  ",base
        print"y altura:  ",altura
        print "Tiene un area de" ,round( resultat , 2)

elif (menu == "C"):
    radio=input ("Escriba el radio:  ")

    if (radio <0):
        print "Negativo no"
    else:
        resultat= pi*radio**2
        print"Un circulo de radio:  ",radio
        print"Tiene un area de:   " ,round( resultat ,2)

elif (menu != "T" or menu !="C"):
    print"Opcion incorrecta"
