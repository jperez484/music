class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Pianist(Musician):
    def __init__(self):
        self.sounds = ["Din", "Din", "Din", "Din", "Din, ""Dun", "Dunnnnnn"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print("Let's get classical...")
        print("Dun, Dun, Din, Din")
        
        
class Drummer(Musician):
    def __init__(self):
        self.sounds = ["Pa", "Rum", "Pum", "Pum", "Pum", "Ba", "Bum"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print("And a ONE, and a TWO, and a Three, FOUR, BOOOOOOOOOOOOOM")
  
Band_hire = {
        Guitarist: "Do you want a Guitarist?",
        Bassist: "Do you want a Bassist?",
        Pianist: "Do you want a Pianist?",
}

class Band:
    def __init__(self):
        self.members = []

    def interactive_hire(self):
    
        for player in Band_hire: 
            answer =input(Band_hire[player])
            if answer in {"Yes","Y", "yes", "y"}:
            
                band_member = player()
                band_member.solo(6)
        
                #print(band_member.sounds)
                self.members.append(band_member)

New_Band = Band()
New_Band.interactive_hire()

  