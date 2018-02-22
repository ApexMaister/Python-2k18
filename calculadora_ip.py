#coding: utf8
import os

os.system('clear')


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
