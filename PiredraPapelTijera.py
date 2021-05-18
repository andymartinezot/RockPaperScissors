import os
import time 
from random import randint 

#-----------Instruccion para borrar pantalla---------

if os.name == "posix":
   var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

#----Funcion wque define al ganador---------
def ganador(eleccion1,eleccion2):
    if eleccion1=="Piedra" and eleccion2=="Piedra":
        resultado = "Es Empate!"
        return resultado
    if eleccion1=="Piedra" and eleccion2=="Papel":
        resultado = "Gano Computadora!"
        return resultado
    if eleccion1=="Piedra" and eleccion2=="Tijera":
        resultado = "Gano Jugador!"
        return resultado
    if eleccion1=="Papel" and eleccion2=="Papel":
        resultado = "Es Empate!"
        return resultado
    if eleccion1=="Papel" and eleccion2=="Piedra":
        resultado = "Gano Jugador!"
        return resultado
    if eleccion1=="Papel" and eleccion2=="Tijera":
        resultado = "Gano Computadora!"
        return resultado
    if eleccion1=="Tijera" and eleccion2=="Tijera":
        resultado = "Es Empate!"
        return resultado
    if eleccion1=="Tijera" and eleccion2=="Papel":
        resultado = "Gano Jugador!"
        return resultado
    if eleccion1=="Tijera" and eleccion2=="Piedra":
        resultado = "Gano Computadora!"
        return resultado

#------Pantalla de introduccion-------------

print("")
print("")
print("**********************************************") 
print("*                                            *")
print("*   ¡Bienvenido al Piedra, Papel o Tijera!   *")
print("*                                            *")
print("**********************************************")


#-------Definiendo variables--------------
empezarjuego = True
jugardenuevo = False
time.sleep(3)
os.system(var) 

#------Seleccion de opciones Usuario y PC------

elegircompu = randint(1,3)
while True:##Excepcion en caso de que el usario seleccione una tecla diferente a numeros
    try:
        elegir = int(input("\n\nSeleccione:\n1 - Piedra\n2 - Papel\n3 - Tijeras\nIngrese eleccion: "))
        time.sleep(0.5)
        break
    except ValueError:
        print("Introduzca valores numericos entre 1-3.")
        time.sleep(1)
        os.system(var)         

#--------Contadores----------
count=0
contadorinterno=0
contadorvictoria=0
contadorempate=0
contadorderrota=0

#--------Programacion de la aplicacion----------

while empezarjuego == True or jugardenuevo == True:
    if elegir == 1:
        elegir = "Piedra"
        if elegircompu == 1:
            elegircompu = "Piedra"
        if elegircompu == 2:
            elegircompu = "Papel"   
        if elegircompu == 3:
            elegircompu = "Tijera"
        valorganador = ganador(elegir,elegircompu)
        print("Jugador: " + elegir + " - Computadora: " + elegircompu)    
        print(valorganador)
        if valorganador == "Gano Jugador!":
            contadorvictoria = contadorvictoria+1
        elif valorganador == "Es Empate!":
            contadorempate = contadorempate+1
        elif valorganador == "Gano Computadora!":
            contadorderrota = contadorderrota+1
        empezarjuego = False
        decision = input("Quieres jugar de nuevo? Y/y = Si. Cualquier otra tecla = No. : ").lower()
        if decision=="y":
            jugardenuevo = True
            elegircompu = randint(1,3)
            contadorinterno = 0
            os.system(var) 
        else:
            jugardenuevo = False
        count=count+1

            
    elif elegir == 2:
        elegir = "Papel"
        if elegircompu == 1:
            elegircompu = "Piedra"
        if elegircompu == 2:
            elegircompu = "Papel"   
        if elegircompu == 3:
            elegircompu = "Tijera"
        valorganador = ganador(elegir,elegircompu)
        print("Jugador: " + elegir + " - Computadora: " + elegircompu)    
        print(valorganador)
        if valorganador == "Gano Jugador!":
            contadorvictoria = contadorvictoria+1
        elif valorganador == "Es Empate!":
            contadorempate = contadorempate+1
        elif valorganador == "Gano Computadora!":
            contadorderrota = contadorderrota+1
        empezarjuego = False
        decision = input("Quieres jugar de nuevo? Y/y = Si. Cualquier otra tecla = No. : ").lower()
        if decision=="y":
            jugardenuevo = True
            elegircompu = randint(1,3)
            contadorinterno = 0
            os.system(var) 
        else:
            jugardenuevo = False
        count=count+1


    elif elegir == 3:
        elegir = "Tijera"
        if elegircompu == 1:
            elegircompu = "Piedra"
        if elegircompu == 2:
            elegircompu = "Papel"   
        if elegircompu == 3:
            elegircompu = "Tijera"
        valorganador = ganador(elegir,elegircompu)
        print("Jugador: " + elegir + " - Computadora: " + elegircompu)    
        print(valorganador)
        if valorganador == "Gano Jugador!":
            contadorvictoria = contadorvictoria+1
        elif valorganador == "Es Empate!":
            contadorempate = contadorempate+1
        elif valorganador == "Gano Computadora!":
            contadorderrota = contadorderrota+1
        empezarjuego = False
        decision = input("Quieres jugar de nuevo? Y/y = Si. Cualquier otra tecla = No. : ").lower()
        if decision=="y":
            jugardenuevo = True
            elegircompu = randint(1,3)
            contadorinterno = 0
            os.system(var) 
        else:
            jugardenuevo = False
        count=count+1
    

    else:
        if empezarjuego == True or jugardenuevo == False:
            print("La seleccion ha sido incorrecta, vuelva a elegir.")
            time.sleep(1)
            os.system(var) 
            while True:
                try:
                    elegir = int(input("\n\nSeleccione:\n1 - Piedra\n2 - Papel\n3 - Tijeras\nIngrese eleccion: "))
                    time.sleep(0.5)
                    break
                except ValueError:
                    print("Introduzca valores numericos entre 1-3.")
                    time.sleep(1)
                    os.system(var)                       
        elif empezarjuego == False and jugardenuevo == True:
            if contadorinterno == 0:
                while True:
                    try:
                        elegir = int(input("\n\nSeleccione:\n1 - Piedra\n2 - Papel\n3 - Tijeras\nIngrese eleccion: "))
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("Introduzca valores numericos entre 1-3.")
                        time.sleep(1)
                        os.system(var)                   
                contadorinterno = contadorinterno+1
            elif contadorinterno > 0:
                print("La seleccion ha sido incorrecta, vuelva a elegir.")
                time.sleep(1)
                os.system(var) 
                while True:
                    try:
                        elegir = int(input("\n\nSeleccione:\n1 - Piedra\n2 - Papel\n3 - Tijeras\nIngrese eleccion: "))
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("Introduzca valores numericos entre 1-3.")
                        time.sleep(1)
                        os.system(var)                   

os.system(var) 
#print("\n\n-----------------\nJugaste " + str(count) + " veces.\nGanaste: " + str(contadorvictoria) + " veces.\nEmpataste: " + str(contadorempate) + " veces.\nPerdiste: " + str(contadorderrota) + " veces.\nFin de la partida.")
print("\n\n**********************************************") 
print("               FIN DE LA PARTIDA!             ")
print("               Ganaste: " + str(contadorvictoria) + " veces")
print("               Empataste: " + str(contadorempate) + " veces")
print("               Perdiste: " + str(contadorderrota) + " veces")
print("**********************************************")

        






