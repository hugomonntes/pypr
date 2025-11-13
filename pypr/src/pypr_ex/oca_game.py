import random
# # # Realiza el juego de la Oca. Ten en cuenta que aunque visualmente es una
# # # espiral, el tablero se puede representar como un array unidimensional con reglas
# # # en ciertas casillas. Además puedes hacer que la CPU juegue, pues sería una IA muy
# # # sencilla, con lo que puedes plantear uno o dos jugadores. Puedes usar el ejemplo
# # # dado en teoría como base inicial para el juego.º 
# la posada (19), donde pierdes un turno; 
# la cárcel (56), donde pierdes turnos; 

def initTablero(casillas: list):    
    for i in range (1,64):
        casillas.append(i)
    return casillas    

def definirJugador(numeroCasilla):
    return numeroCasilla + tirarDado()

def tirarDado():
    return random.randint(1, 7)

def caerEnPuente(numeroCasilla):
    return 12 if numeroCasilla == 6 else 6

def caerEnPozo(casillaOtroJugador):
    while (casillaOtroJugador != 31):
        turno = False
        casillaOtroJugador += tirarDado()
    turno = True 
    return turno

def caerEnCalavera():
    return 1

def caerEnOca(numeroCasilla):
    if numeroCasilla == 60:
        return 63
    numeroCasilla += 5
    numeroCasilla += tirarDado()
    return numeroCasilla
    
def caerEnLaberinto():
    return 30

def caerEnDados(numeroCasilla):
    return 53 if numeroCasilla == 26 else 26

    contador= 0
def caerEnCarcel(contador):
    while (contador<3):
        turno=False
        contador=contador+1
        break
    if contador==3:
        turno= True

def caerEnPosada(contador):
    contador = 0
    while (contador<1):
        turno=False
        contador=contador+1
        break
    if contador==1:
        turno= True

def pintarAvanzarEnTablero(casillas,numeroCasilla):
    casillas[numeroCasilla] = "🔵"
    
#MAIN

initTablero(casillas = [])
casilla = 1
juegaElUsuario = True
fin = False
while (not fin):
    if (juegaElUsuario):
        jugador1 = definirJugador(casilla)
    else:
        jugador2 = definirJugador(casilla)


    #Acaba el juego
    if (jugador1 == 63 or jugador2 == 63):
        fin = True
