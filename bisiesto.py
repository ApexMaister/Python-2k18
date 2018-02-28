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
	print "Bisiesto"
	
elif (anyo % 4 == 0 and anyo % 100 != 0):
     print "Bisiesto"
     
else:
    print "No es bisiesto"
