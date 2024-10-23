#!/usr/bin/env python

'''Bones practiques. Calcula la divisió entera de dos nombres.

Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

A partir de dos nombres, dividend i divisor, el programa
calcula el quocient i el residu i els mostra en pantalla.
A part mostra la divisió realitzada per pantalla.
'''
__author__ = "Roger León Arbó"
__email__ = "rleon@instituticaria.cat"
__date__ = "2024/10/23"

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
