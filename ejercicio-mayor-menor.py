#coding: utf-8

A=input ("Introdueix el numero 1: ")
B=input("Introdueix el numero 2:  ")
C=input("Introdueix el numero 3:  ")

if (A==B) and (B==C):

    print " Los tres son iguales "

else:

    if (A==B and C!=A or
        A==C and B!=A or
         B==C and A!=B):

        print "Hay 2 iguales"



    else:



        if (A>B) and  (B>C):

            print A,"Es el mayor y",C,"Es el menor"

        if (A>C) and (C>B):

            print A, "Es el mayor y" ,B, "Es el menor"

        if (B>A) and (A>C):

            print B, "Es el mayor y" , C , "Es el menor"

        if (B>C) and (C>A):

            print B, "Es el mayor y" , A , "Es el menor"

        if (C>A) and (A>B):

            print C, "Es el mayor y" , B , "Es el menor"

        if (C>B) and (B>A):

            print C, "Es el mayor y" , A , "Es el menor"
