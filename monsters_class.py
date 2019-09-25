class Monsters():

# Behaviours

    def scare(self, scare_mode = '*generic scare*'):
        return 'Humans are REAL! ' + scare_mode

    def eat(self, food = 'nothing else'):
        return 'Avocados and Pumpkin Spice Lattes and ' + food

    def transform(self, transformation = '*fwoop*'):
        return 'ALAKAZAM! ' + transformation

    def exercise(self, workout = '*flex*'):
        return '20 minute morning Pilates! ' + workout

    def learn(self, learning = 'basically it'):
        return 'Origami ' + learning

    def watch(self, view = ';)'):
        return 'Monflix and No Chill! ' + view

#Characteristics

    def __init__(self, name, eye_number, fur, skills_list, cuteness):
        self.name = name
        self.eye_number = eye_number
        self.fur = fur
        self.skills_list = skills_list
        self.cuteness = cuteness