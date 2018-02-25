#coding: utf8


import os

os.system('clear')

print """

        #############################
        #       Calculadora IP      #
        #############################

        1- Netmask
        2- Wildcard

"""

opcion = input ("Introduce una Opcion:  ")


if opcion == 1 :

    netmask= raw_input("Introdueix la netmask   (/1-24):   ")

    if netmask == "/0" :

        print "Invalid"

    elif netmask == "/1" :

        print "128.0.0.0 = 1"

    elif netmask == "/2":

        print "192.0.0.0 = 2"

    elif netmask == "/3":

        print "224.0.0.0 = 3 "

    elif netmask == "/4":

        print " 240.0.0.0 = 4"

    elif netmask == "/5":

        print "248.0.0.0 = 5 "

    elif netmask == "/6":

        print "252.0.0.0 = 6 "

    elif netmask == "/7":

        print "254.0.0.0 = 7 "

    elif netmask == "/8":

        print "255.0.0.0 = 8"

    elif netmask == "/9":

        print "255.128.0.0 = 9 "

    elif netmask == "/10":

        print "255.192.0.0 = 10 "

    elif netmask == "/11":

        print " 255.224.0.0 = 11 "

    elif netmask == "/12":

        print "255.240.0.0 = 12"

    elif netmask == "/13":

        print " 255.248.0.0 = 13 "

    elif netmask == "/14":

        print "255.252.0.0 = 14 "

    elif netmask == "/15":

        print " 255.254.0.0 = 15 "

    elif netmask == "/16":

        print "255.255.0.0 = 16 "

    elif netmask == "/17":

        print "255.255.128.0 = 17"

    elif netmask == "/18":

        print "255.255.192.0 = 18"

    elif netmask == "/19":

        print "255.255.224.0 = 19"

    elif netmask == "/20":

        print " 255.255.240.0 = 20"

    elif netmask == "/21":

        print " 255.255.248.0 = 21 "

    elif netmask == "/22":

        print " 255.255.252.0 = 22"

    elif netmask == "/23":

        print " 255.255.254.0 = 23 "

    elif netmask == "/24":

        print "255.255.255.0 = 24 "






if opcion == 2 :

    wildcard = input ("Introdueix la netmask per saber la wildcard:  (/1-24):   ")


    if wildcard == "/0" :
        print "Invalid"

    elif wildcard == "/1" :
        print "127.255.255.255"

    elif wildcard == "/2" :
        print "63.255.255.255 "

    elif wildcard == "/3":
        print "31.255.255.255"

    elif wildcard == "/4":
        print "15.255.255.255 "

    elif wildcard == "/5":
        print "7.255.255.255"

    elif wildcard == "/6":
        print "3.255.255.255 "

    elif wildcard == "/7":
        print "1.255.255.255 "

    elif wildcard == "/8":
        print "0.255.255.255 "

    elif wildcard == "/9":
        print " 0.127.255.255"

    elif wildcard == "/10":
        print "0.63.255.255 "

    elif wildcard == "/11":
        print " 0.31.255.255"

    elif wildcard == "/12":
        print " 0.15.255.255 "

    elif wildcard == "/13":
        print "0.7.255.255 "

    elif wildcard == "/14":
        print "0.3.255.255"

    elif wildcard == "/15":
        print "0.1.255.255"

    elif wildcard == "/16":
        print "0.0.255.255 "

    elif wildcard == "/17":
        print " 0.0.127.255"

    elif wildcard == "/18":
        print " 0.0.63.255  "

    elif wildcard == "/19":
        print "0.0.31.255  "

    elif wildcard == "/20":
        print " 0.0.15.255  "

    elif wildcard == "/21":
        print " 0.0.7.255  "

    elif wildcard == "/22":
        print " 0.0.3.255 "

    elif wildcard == "/23":
        print "0.0.1.255 "

    elif wildcard == "/24":
        print "0.0.0.255  "
