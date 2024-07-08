from trainer import trainer

class batalie:
    def battle(self, trainer1, trainer2):
        contor0=1
        while contor0>0:
            p1 = trainer1.alege_pokemon()
            p2 = trainer2.alege_pokemon()
            print("\n1 executat , p1hp=",p1.name)
            print("\n2 executat , p2hp=",p2.name)
            contor =1
            while contor>0:
                p1.attack(p2)
#                print("\n1 executat , p1hp=", p1.name)
#                print("\n2 executat , p2hp=", p2.name)
                print("Pokemonul: ", p1.name," a atacat pokemonul: ", p2.name," cu nivelul de viata: ", p2.health)
                if not p2.isalive():
                    print("Pokemonul antrenorului ", trainer2.name," a fost invins")
                    contor=0
                p2.attack(p1)
                print("Pokemonul: ", p2.name, " a atacat pokemonul: ", p1.name," cu nivelul de viata: ", p1.health)
                if not p1.isalive():
                    print("Pokemonul antrenorului ", trainer1.name, " a fost invins")
                    contor=0

            if(not trainer1.anyleft()):
                print("0 executat")
                print("Antrenorul ",trainer1.name," a fost invins")
                contor0=0
            if (not trainer2.anyleft()):
                print("0 executat")
                print("Antrenorul ", trainer2.name, " a fost invins")
                contor0 = 0

