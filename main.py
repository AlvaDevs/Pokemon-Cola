# Implementación de una cola para el centro Pokémon
from collections import deque

class ColaCentroPokemon:
    def __init__(self):
        self.cola = deque()  # Usamos deque para implementar la cola

    def encolar_pokemon(self, pokemon):
        # Añadir un Pokémon al final de la cola
        self.cola.append(pokemon)
        print(f"{pokemon} ha sido añadido a la cola del Centro Pokémon.")

    def desencolar_pokemon(self):
        # Eliminar y devolver el primer Pokémon en la cola
        if self.cola:
            pokemon = self.cola.popleft()
            print(f"{pokemon} ha sido atendido en el Centro Pokémon.")
            return pokemon
        else:
            print("La cola está vacía.")
            return None

    def mostrar_cola(self):
        # Mostrar todos los Pokémon en la cola
        if not self.cola:
            print("La cola está vacía.")
        else:
            print("Pokémon en la cola:")
            for pokemon in self.cola:
                print(f"- {pokemon}")


# Programa principal
if __name__ == "__main__":
    cola_centro_pokemon = ColaCentroPokemon()

    # Encolando Pokémon
    cola_centro_pokemon.encolar_pokemon("Sprigatito")
    cola_centro_pokemon.encolar_pokemon("Fuecoco")
    cola_centro_pokemon.encolar_pokemon("Quaxly")

    # Mostrando la cola actual
    cola_centro_pokemon.mostrar_cola()

    # Desencolando Pokémon
    cola_centro_pokemon.desencolar_pokemon()
    cola_centro_pokemon.desencolar_pokemon()

    # Mostrando la cola después de desencolar
    cola_centro_pokemon.mostrar_cola()
