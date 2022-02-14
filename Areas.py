# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 15:12:19 2022

@author: georg
"""

import cProfile 

print("Area del rectangulo")

def main():
    class rectangulo:
        pass
    C = rectangulo()
    C.altura = int(input("Ingrese la altura:"))
    C.base = int(input("Ingrese la medida de la base:"))
    area = C.base*C.altura
    
    print("El area del rectangulo es:",area)
    
cProfile.run("main()")
    