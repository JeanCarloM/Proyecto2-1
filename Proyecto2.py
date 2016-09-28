#!/usr/bin/env python
# -*- coding: latin-1 -*-

def Fact(rec=1):
	Num = input("Ingresa el numero a calcular: ")
	if Num 

print "Bienvenido a tu calculadora de Factoriales"
print "Ingresa el numero a calcular"

def Factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        resultado = 0 #¿No se si esto sobra?
        resultado = n * Factorial(n-1)
        return resultado

Num = input("Ingresa el numero a calcular: ") 
print (Factorial(Num))
