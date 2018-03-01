#coding: utf-8
import os

os.system("clear")

print """
	---------------------
	  Calcular Bisiesto
	---------------------
"""
anyo= input ("Introduce un año:  ")


if ( anyo % 400 == 0 ):
	print "El año",anyo," es Bisiesto y Multiplo de 400"

elif (anyo % 4 == 0 and anyo % 100 != 0):
	print "El año",anyo," es Bisiesto y Multiplo de 4 y no de 100"

else:
	print "El año",anyo,"No es bisiesto"
