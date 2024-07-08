from pokemon import pokemon
class trainer:
    def __init__(self, name, pokemoni):
        self.name = name
        self.pokemoni = pokemoni

    def alege_pokemon(self):
        # Make a copy of the list to iterate over
        for pokemon in list(self.pokemoni):
            if pokemon.isalive():
                print("A fost introdus in lupta", pokemon.name, "cu nivelul de viata", pokemon.health)
                return pokemon
            else:
                print("\n\n\nPokemon:", pokemon.name, "died\n\n\n")
                self.pokemoni.remove(pokemon)
                print(self.pokemoni)

        #
        if len(self.pokemoni) < 1:
            print("Nu este nici un pokemon gata de lupta\n")
            return None

        #
        if self.pokemoni[0].isalive():
            return self.pokemoni[0]
        else:
            return None

    def anyleft(self):
        return any(pokemon.isalive() for pokemon in self.pokemoni)