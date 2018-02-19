#coding: utf8
print "Buenos dias , Que le pongo??"
print ""
print "-Super: Normal(1.5€), Turbo(1.55€)"
print "-Sin plomo: Normal(1.6€), Con aditivos(sabor naranja)(1.65€)"
print "-Diesel: Normal(1.7€), Fast&Furius(1.75€)"
print ""


tipodegasolina= raw_input ("Introduce El tipo de gasolina:   ")
litros = input ("Introdueix Els Litres:   ")


if (tipodegasolina == "Super Normal" ):

    print litros * 1.5 ,"€"

if (tipodegasolina == "Super Turbo"):

    print litros * 1.55 ,"€"

if (tipodegasolina == "Sin Plomo Normal"):

    print litros * 1.6 ,"€"

if (tipodegasolina == "Sin Plomo Con aditivos"):

    print litros * 1.65, "€"

if (tipodegasolina == "Diesel Normal"):

    print litros * 1.7 , "€"

if (tipodegasolina == "Diesel Fast&Furius"):

    print litros * 1.75 , "€"
