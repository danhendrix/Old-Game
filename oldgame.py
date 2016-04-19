from random import randint

class NewGame(object):

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.armour = 50
        self.attack_power = 100
        self.level = 1
        self.hp_enemy = 0
       

    def engagement(self):
        level = randint(1,10)

        Enemy1 = Enemy(level)
        print "\nYou're stumbling through the forest when you spot a huge enemy %d big." % Enemy1.hp_enemy
        while Enemy1.hp_enemy > 0 and self.hp > 0:         
            print "\nYou currently have %d health, %d armour, and %d attack power." % (self.hp, self.armour, self.attack_power)
            print "\nWhat would you like to do?"
            print "\n\n(1) Attack\n(2) Run"            

            user_choice = int(raw_input("\n> "))
            
            if user_choice == 1:
                attack = randint(1,self.attack_power)
                enemy_attack = randint(1,Enemy1.attackpower_enemy)

                print "You swing your weapon and hit for %d damage" % attack
                raw_input("\n> ")
                Enemy1.hp_enemy = (Enemy1.hp_enemy - attack)
                if Enemy1.hp_enemy <= 0:
                    print "You killed him! Nice."
                    raw_input("\n> ")
                    self.engagement()
                else:

                    print "\nThe drooling monster lunges at you and hits for %d damage" % enemy_attack
                    raw_input("\n> ")
                    self.hp = self.hp - enemy_attack

                    if self.hp <= 0:
                        "You died, bro."
                    else:
                        print "Don't let your guard down, he still has %d hp." % Enemy1.hp_enemy
                        pass
            
            else:
                self.engagement()

        self.engagement()
        
            

        

class Enemy(object):



    def __init__(self, level):

        self.enemy_level = level 
        self.hp_enemy = randint(level,(level*10))
        self.armour_enemy = randint(1,level*5)
        self.attackpower_enemy = randint(1,level *10)      

danny = NewGame("Danny")

danny.engagement()