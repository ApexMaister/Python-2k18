#coding: utf8

import os

os.system('clear')

print """

        ############################
        # Comparador de Multiplos  #
        ############################
"""

num1 = input ("Introdueix un num:   ")
num2 = input ("Introdueix un altre num:     ")

if (num1 <0 or num2 <0):

    print "Negativos no"

elif (num1 == 0 or num2 == 0 ):

    print "No se puede cero"

else:

    if  (num1 > num2):

        mayor = num1
        menor = num2

    else:

        mayor = num2
        menor = num1



    if (mayor % menor == 0):


        print mayor , "es multiplo de ", menor


    else:


        print mayor , "no es multiplo de ", menor
