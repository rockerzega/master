#!/usr/bin/env python
from perceptron import Perceptron

## Datos de hombres y mujeres
input_data = [[170,56,1], # Mujer de 1.70m y 56kg
              [172,63,0],# Hombre de 1.72m y 63kg
              [160,50,1], # Mujer de 1.60m y 50kg
              [170,63,0], # Hombre de 1.70m y 63kg
              [174,66,0],# Hombre de 1.74m y 66kg
              [158,55,1],# Mujer de 1.58m y 55kg
              [183,80,0],# Hombre de 1.83m y 80kg
              [182,70,0],# Hombre de 1.82m y 70kg
              [165,54,1]]# Mujer de 1.65m y 54kg

## Creamos el perceptron
pr = Perceptron(3,0.1) # Perceptron con 3 entradas
weights = [] # Lista con los pesos
errors = []  # Lista con los errores

## Fase de entrenamiento
for _ in range(100):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1] # Agregamos un uno por default
        weights.append(pr._w)
        err = pr.train(inp,output)
        errors.append(err)

h = float(raw_input("Introduce tu estatura en centimetros.- "))
w = float(raw_input("Introduce tu peso en kilogramos.- "))

if pr.predict([1,h,2]) == 1: print "Mujer"
else: print "Hombre"

#print """
#Nota: El resultado puede estar incorrecto. 
#Esto puede ser debido a sesgo en la muestra, o porque es imposible separar
#a hombres y mujeres perfectamente basados unicamente en talla y peso."""

## Fase de graficacion
import imp

can_plot = True
try:
    imp.find_module('matplotlib')
except:
    can_plot = False

if not can_plot:
    print "No es posible graficar los resultados porque no tienes matplotlib"
    sys.exit(0)
    pass

import matplotlib.pyplot as plt

plt.plot(errors)
plt.show()