'''
Simulacion de batalla Pokemon sin utilizar OOP.
'''

from random import choice
from time import sleep


def waiting():
    print('\n...')
    sleep(0.5)


def crear_pokemon(nombre: str, tipo: str, hp: int, ad: int):
    return {
        'nombre': nombre.capitalize(),
        'tipo': tipo,
        'hp': hp,
        'ad': ad,
    }


def obtener_ataque(tipo: str):
    if tipo == 'electrico':
        return 'Impactrueno'
    elif tipo == 'planta':
        return 'Hoja navaja'
    elif tipo == 'fuego':
        return 'Llamarada'
    else:
        return 'Canon de agua'


def hacer_dano(pokemon, hp_perdido: int):
    pokemon['hp'] = pokemon['hp'] - hp_perdido


def atacar(atacante, rival):
    ataque = obtener_ataque(atacante['tipo'])
    hacer_dano(rival, atacante['ad'])
    print(f"\n({atacante['nombre']}) Ataca con {ataque} | -{atacante['ad']}")


pikachu = crear_pokemon('pikachu', 'electrico', 60, 15)
chikorita = crear_pokemon('chikorita', 'planta', 45, 10)
charmander = crear_pokemon('charmander', 'fuego', 40, 10)
froakie = crear_pokemon('froakie', 'agua', 40, 20)

pokemon_posibles = [pikachu, chikorita, charmander, froakie]

poke_1 = choice(pokemon_posibles)
poke_2 = choice(pokemon_posibles)

print('\n ------ POKEMON SELECCIONADOS ------')

waiting()
print(f"\nPokemon 1: {poke_1['nombre']} (HP: {poke_1['hp']} | AD: {poke_1['ad']})")
print(f"Pokemon 2: {poke_2['nombre']} (HP: {poke_2['hp']} | AD: {poke_2['ad']})")

while True:
    waiting()
    atacar(poke_1, poke_2)

    if poke_2['hp'] <= 0:
        print(f"\nGAME OVER: {poke_1['nombre']} vencio a {poke_2['nombre']}")
        break

    waiting()
    atacar(poke_2, poke_1)

    if poke_1['hp'] <= 0:
        print(f"\nGAME OVER: {poke_2['nombre']} vencio a {poke_1['nombre']}")
        break

    waiting()
    print('\nHPs restantes')
    print(f"{poke_1['nombre']}: {poke_1['hp']}")
    print(f"{poke_2['nombre']}: {poke_2['hp']}")
    