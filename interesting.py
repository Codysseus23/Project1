class Daggers(object):
    cost = 15
    name = 'dagger'
    def apply(self, hero):
        hero.double_hit = True
        print(f"{hero.name} now attacks twice. ")

def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.double_hit = False


class Bloodletter(Character):
    def __init__(self):
        self.name = 'Bloodletter'
        self.health = 25
        self.power = 1
        self.bounty = 8

    def attack(self, enemy):
        
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)
        
        enemy.receive_damage(self.power)
        self.power += 2