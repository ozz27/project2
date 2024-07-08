class pokemon:
  def __init__(self, name, type, health, strenght):
    self.name = name
    self.type = type
    self.health = int(health)
    self.strenght = strenght

  def attack(self,other):
    if( self.health > 0):
      multiplier = int(self.attackmultiplier(other.type))
      damage = self.strenght
#      print("\n\nDamage: ",damage," Strenght: ",self.strenght," Multiplier: ",multiplier, "Other health:",other.health)
      other.health -= int(damage)
      if other.health <= 0:
          other.health = 0
      print(self.name," has succesfully attacked: ",other.name)
    else: print(self.name, "'s attack failed against: ", other.name)

  def attackmultiplier(self, other):
    m=1
    if(self.type == other):
      return m
    elif(self.type == "apa" and other == "foc"):
      return m*2
    elif(self.type == "foc" and other == "pamant"):
      return m*2
    elif(self.type == "pamant" and other == "foc"):
      return m*2
    else: return m


  def isalive(self):
    return int(self.health) > 0
