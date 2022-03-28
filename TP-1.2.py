import random
from cmath import sqrt
import numpy as np # importando numpy
from turtle import color
import matplotlib.pyplot as plt
from pyparsing import col 
from scipy import stats # importando scipy.stats
apuesta_minima_ruleta = 10000
dinero_ganado_paridad = 15000
rojo = "Rojo"
negro = "Negro"
par = "Par"
impar = "Impar"

menu = """###### MENU RULETA #######
1. JUGAR
2. SALIR
Elige: """

explicacion_ruleta = f"""Se puede apostar por:
1) Numero y color: si acertás ambos, la apuesta se multiplica por 10. Si no, se pierde la apuesta
2) Solamente color: si se acierta el color, la apuesta se multiplica por 2. Si no, se pierde la apuesta
3) Solo paridad: si se acierta par o impar, se ganan 15000. Si no, se pierde la apuesta.
Los numeros van del 0 al 36, colores son rojo y negro, paridades son par e impar"""

#Está sin implementar, simplemente lo traje para utilizar después y no olvidarnos
conjuntoValores = []
conjuntoValoresHi = []

def funcion(rep, corr):
    for c in range(corr):
        valoresInt = []
        hi =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(rep):
            nRandom = ran.randint (0,36)
            valoresInt.append(nRandom)
            hi[nRandom] += 1
        conjuntoValores.append(valoresInt)
        conjuntoValoresHi.append(hi)


def solicitarDineroRuleta(saldo):
    dinero_apostado = 0
    while dinero_apostado < apuesta_minima_ruleta or dinero_apostado > saldo:
        dinero_apostado = float(input(f"¿Cuanto apostás? Debe ser al menos {apuesta_minima_ruleta} pesos, y no debe superar el saldo: "))
    return dinero_apostado

def pedirNumero():
    numero = int(input("Elige un numero entre 0 y 36: "))
    band = True
    while (band): 
        if 0 < numero < 36:
            band = False
            return numero
        else:
            band = True

def main():
    saldo_global = 50000 #El saldo con el que se inicia
    eleccion = ""
    while eleccion != "2":
        eleccion = input(menu)
        if eleccion == "1":
            print(f"Dinero disponible: {saldo_global}")
            colores = [rojo, negro]
            if saldo_global < apuesta_minima_ruleta:
                print(f"Necesita de al menos {apuesta_minima_ruleta} pesos para jugar a la ruleta")
                continue
            print(explicacion_ruleta)
            dinero_apostado = solicitarDineroRuleta(saldo_global)
            eleccion_ruleta = ""
            while eleccion_ruleta != "4":
                print(f"Dinero disponible: {saldo_global}")
                eleccion_ruleta = input("""1. Número y color
                                            2. Solo color (negro y rojo)
                                            3. Paridad (par e impar)
                                            4. Volver
                                            Elige: """)
                if eleccion_ruleta == "1":
                    if saldo_global < apuesta_minima_ruleta:
                        print(f"Necesita de al menos {apuesta_minima_ruleta} pesos para jugar a la ruleta")
                        break
                    numero_usuario = pedirNumero()
                    color_eleccion_usuario = input("1. Rojo\n2.Negro\nElige: ")
                    if color_eleccion_usuario == "1":
                        color_usuario = rojo
                    else:
                        color_usuario  = negro
                    
                    #Se elige aleatoriamente
                    nRandom = random.randint(0, 36)
                    cRandom = colores[random.randinit(0, len(colores)-1)]
                    print("Numero obtenido: " + str(nRandom))
                    print("Color obtenido: " + str(cRandom))
                    if nRandom == numero_usuario and cRandom == color_eleccion_usuario:
                        #Acierta numero y color
                        print("Gana el dinero apostado multiplicado por 10.")
                        saldo_global += dinero_apostado*9
                    else:
                        print("Pierde lo apostado numero y color...")
                        saldo_global -= dinero_apostado
                    pass
                elif eleccion_ruleta == "2":
                    if saldo_global < apuesta_minima_ruleta:
                        print(f"Necesitas de al menos {apuesta_minima_ruleta} pesos para jugar.")
                        break
                    color_eleccion_usuario = input("1.Rojo\n2.Negro\nElige: ")
                    if color_eleccion_usuario == "1":
                        color_usuario = rojo
                    else: 
                        color_usuario = negro
                    color_aleatorio = colores[random.randinit(0, len(colores)-1)]
                    print("Color obtenido: " + str(cRandom))
                    if color_usuario == cRandom:
                        #Acierta color
                        print("La apuesta se multiplica por 2")
                        saldo_global += dinero_apostado * 2
                    else:
                        print("Pierde lo apostado en color...")
                        saldo_global -= dinero_apostado
                elif eleccion_ruleta == "3":
                    if saldo_global < apuesta_minima_ruleta:
                        if saldo_global < apuesta_minima_ruleta:
                            print(f"Necesitas al menos {apuesta_minima_ruleta} pesos para jugar a la ruleta")
                            break
                        paridad_eleccion_usuario = input("1.Par\n2.Impar\nElige: ")
                        if paridad_eleccion_usuario == "1":
                            paridad_usuario = par
                        else:
                            paridad_usuario = impar
                        nRandom = random.randint(0, 36)
                        print("Numero obtenido: " + str(nRandom))
                        if nRandom % 2 == 0 and paridad_usuario == par:
                            print("El numero es par.")
                            print(f"Gana {dinero_ganado_paridad} pesos.")
                            saldo_global += dinero_ganado_paridad
                        elif nRandom % 2 != 0 and paridad_usuario == impar:
                            print("El numero es impar.")
                            print(f"Gana {dinero_ganado_paridad} pesos.")
                            saldo_global += dinero_ganado_paridad
                        else:
                            print("Pierde lo apostado en paridad...")
                            saldo_global -= dinero_apostado

    print(f"Saldo final: {saldo_global}")
                        
main()
