#coding: utf-8

#Nom: Arnau De Los Riscos

#importo la llibreria os


import os

#utilitzo el comando clear per rentar la pantalla quan l executem

os.system('clear')

#declaro la variable edat

edad = input("Indica la edad:    ")

#si la edat es entre 17 i 23 pot pasar

if (edad >= 18 and edad <= 23):


	print " Pots pasar  "

else:
#si  es menor
		if (edad <18):

			print "Ets menor ,No pots pasar"

#si la edat es menor que 0 la considero erronea

		if (edad <0 ):

			print "Valor incorrecte posa una edat major que 0"


#la gent de mes de 23 no poden pasar
		if (edad >23 ):

			print "Eres demasiado grandullon para pasar"
#faig una espera de 3 segons abans de sortir del programa perque quedi net

os.system('sleep 3')
