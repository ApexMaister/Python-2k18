#coding: utf8
import os

os.system('clear')

print """

        #############################
        #       Calculadora IP      #
        #############################

        1- netmask
        2- Wildcard

"""

opcion == ("Introduce una Opcion:  ")


if opcion ==1 :

    netmask= raw_input("Introdueix la netmask   (/1-8):   ")

    if netmask == "/0" :

        print "Invalid"

    elif netmask == "/1" :

        print "128"

    elif netmask == "/2":

        print "192"

    elif netmask == "/3":

        print "224"

    elif netmask == "/4":

        print "240"

    elif netmask == "/5":

        print "248"

    elif netmask == "/6":

        print "252"

    elif netmask == "/7":

        print "254"

    elif netmask == "/8":

        print "255"

if opcion == 2 :
