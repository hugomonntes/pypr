import random
# # # Realiza el juego de la Oca. Ten en cuenta que aunque visualmente es una
# # # espiral, el tablero se puede representar como un array unidimensional con reglas
# # # en ciertas casillas. Además puedes hacer que la CPU juegue, pues sería una IA muy
# # # sencilla, con lo que puedes plantear uno o dos jugadores. Puedes usar el ejemplo
# # # dado en teoría como base inicial para el juego.º
# # Las casillas más importantes en el juego de la oca son
# # las ocas, que permiten avanzar y tirar de nuevo. 
# son los puentes (6 y 12), te mueven entre ellos
# la posada (19), donde pierdes un turno; 
# el pozo (31), donde quedas atrapado hasta que otro jugador cae en él; 
# el laberinto (42), que te hace retroceder a la casilla 30; 
# la cárcel (56), donde pierdes turnos; 
# los dados (26 y 53), que te hacen avanzar el número que indiquen; 
# y la calavera o la muerte (58), que te devuelve al inicio.

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

def pintarAvanzarEnTablero(casillas,numeroCasilla):
    casillas[numeroCasilla] = "🔵"
    
#MAIN

initTablero(casillas = [])
juegaElUsuario = True
fin = False
while (not fin):
    if (juegaElUsuario):
        jugador1 = definirJugador(casilla)
    else:
        jugador2 = definirJugador(casilla)
    
    if (jugador1 == 63 or jugador2 == 63):
        fin = True
