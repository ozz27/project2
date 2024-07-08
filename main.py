from pokemon import pokemon
from trainer import trainer
from batalie import batalie

pikachu = pokemon("Pikachu", "foc", "301", "10")
florges = pokemon("Florges", "foc", "302", "10")
malmar = pokemon("Malmar", "foc", "303", "10")

Mihai = trainer("Mihai",[pikachu,florges,malmar])

talonflame = pokemon("Talonflame", "foc", "251", "10")
godra = pokemon("Godra", "pamant", "352", "9")
howlucha = pokemon("Howlucha", "apa", "403", "8")

Razvan = trainer("Razvan", [talonflame,godra,howlucha])

lupta= batalie()
lupta.battle(Mihai,Razvan)