#importamos el "choice" de random para quitar "cartas" aleatoriamente de nuestro mazo
from random import choice

#cargamos nuestro mazo en una lista
mazo = ["uno_de_espadas","dos_de_espadas","tres_de_espadas","cuatro_de_espadas","cinco_de_espadas","seis_de_espadas","siete_de_espadas","diez_de_espadas","once_de_espadas","doce_de_espadas", "uno_de_oro","dos_de_oro","tres_de_oro","cuatro_de_oro","cinco_de_oro","seis_de_oro","siete_de_oro","diez_de_oro","once_de_oro","doce_de_oro","uno_de_basto","dos_de_basto","tres_de_basto","cuatro_de_basto","cinco_de_basto","seis_de_basto","siete_de_basto","diez_de_basto","once_de_basto","doce_de_basto","uno_de_copas","dos_de_copas","tres_de_copas","cuatro_de_copas","cinco_de_copas","seis_de_copas","siete_de_copas","diez_de_copas","once_de_copas","doce_de_copas"]

#cargamos el mazo en otra lista, la que se va a modificar dentro del bucle de reparticion de barajas, la lista "mazo" no se modifica en ningun momento
mazo_modificable = list(mazo)

#ponemos en 0 la cantidad de cartas de los 2 jugadores
jugador_1_barajas_cantidad = 0
jugador_2_barajas_cantidad = 0

#cargamos 2 listas vacias para las barajas de cada jugador
jugador_1_barajas = []
jugador_2_barajas = []
repartir = 1

#bucle que reparte las cartas para el jugador 1
#en si lo que hace es pegar vueltas mientras que "jugador_1_barajas_cantidad" sea menor que 3, quitando las cartas ya repartidas

if repartir == 1:

    while jugador_1_barajas_cantidad < 3:
        carta_aleatoria = choice(mazo_modificable)
        jugador_1_barajas.append(carta_aleatoria)
        mazo_modificable.remove(carta_aleatoria)
        jugador_1_barajas_cantidad = jugador_1_barajas_cantidad + 1
        
#hacemos lo mismo para el segundo jugador, cambiando el nombre de las variables simplemente, y usando el mismo mazo ...

while jugador_2_barajas_cantidad < 3:
    carta_aleatoria = choice(mazo_modificable)
    jugador_2_barajas.append(carta_aleatoria)
    mazo_modificable.remove(carta_aleatoria)
    jugador_2_barajas_cantidad = jugador_2_barajas_cantidad + 1
    


print("\nCartas del jugador 1: ",jugador_1_barajas)
print("\nCartas del jugador 2: ",jugador_2_barajas)


