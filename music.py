class Musician(object):
    
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name

    def solo(self, length):
        music =[]
        for i in range(length):
            music.append(self.sounds[i % len(self.sounds)])
            #print(self.sounds[i % len(self.sounds)], end=" ")
        #print()
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
  
Band_hire = {
        Guitarist: "Do you want a Guitarist?",
        Bassist: "Do you want a Bassist?",
        Pianist: "Do you want a Pianist?",
}

class Band:
    def __init__(self):
        self.members = []

    def hire(self, player):
    
        for player in Band_hire: 
            answer =input(Band_hire[player])
            if answer in {"Yes","Y", "yes", "y"}:
            
                band_member = player()
                band_member.solo(6)
        
                #print(band_member.sounds)
                self.members.append(band_member)

New_Band = Band()
New_Band.hire()

  