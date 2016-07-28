class Musician(object):
    
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name

    def solo(self, length):
        music =[]
        for i in range(length):
            music.append(self.sounds[i % len(self.sounds)])
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        return music
        

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"], 'bassist')

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"], 'guitarist')

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
        
class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Pa", "Rum", "Pum", "Pum", "Pum", "Ba", "Bum"], 'drummer')
        #self.sounds = ["Pa", "Rum", "Pum", "Pum", "Pum", "Ba", "Bum"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print("And a ONE, and a TWO, and a Three, FOUR, BOOOOOOOOOOOOOM")
        
class Pianist(Musician):
    def __init__(self):
        super(Pianist, self).__init__(["Din", "Din", "Din", "Din", "Din, ""Dun", "Dunnnnnn"], 'pianist')
        #self.sounds = ["Din", "Din", "Din", "Din", "Din, ""Dun", "Dunnnnnn"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print("Let's get classical...")
        print("Dun, Dun, Din, Din")
  

class Band:
    def __init__(self):
        
        self.members = []

    def hire(self):
    
        for player in (Bassist, Guitarist, Drummer, Pianist): 
            answer =input("Do you want a " + player.__name__ + "?")
            if answer in {"Yes","Y", "yes", "y"}:
            
                band_member = player()
                band_member.solo(6)
                #print(band_member.sounds)
                self.members.append(band_member)
                #print(self.members)
                
    def fire(self):
        
        for player in (self.members):
            firing = input("Do you want to fire " + str(player) + "?")
            if firing in {"Yes","Y", "yes", "y"}:
                self.members.remove(player)
                
band_hired = Band()
band_hired.hire()
band_hired.fire()
print(band_hired.members)

#objects dont have names...