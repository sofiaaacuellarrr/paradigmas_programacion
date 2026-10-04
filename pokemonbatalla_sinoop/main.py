'''
Simulacion de batalla Pokemon sin utilizar OOP.
'''

from random import choice
from time import sleep

def crear_pokemon(nombre: str, tipo: str, hp: int, ad: int):
    return {
        'nombre': nombre.capitalize(),
        'tipo': tipo,
        'hp': hp,
        'ad': ad,
    }
pikachu = crear_pokemon('pikachu', 'electrico', 60, 15)
chikorita = crear_pokemon('chikorita', 'planta', 45, 10)
charmander = crear_pokemon('charmander', 'fuego', 40, 10)
froakie = crear_pokemon('froakie', 'agua', 40, 20)

pokemon_posibles = [pikachu, chikorita, charmander, froakie]

poke_1 = choice(pokemon_posibles)
poke_2 = choice(pokemon_posibles)

print('\n ------ POKEMON SELECCIONADOS ------')

print(f"\nPokemon 1: {poke_1['nombre']} (HP: {poke_1['hp']} | AD: {poke_1['ad']})")
print(f"Pokemon 2: {poke_2['nombre']} (HP: {poke_2['hp']} | AD: {poke_2['ad']})")










