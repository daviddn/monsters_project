from monsters_class import *

monster_1 = Monsters('Mike Wazowski', 1, 'bald', ['charisma', 'rolling', 'intelligence'], 'cute')
monster_2 = Monsters('Sullivan', 2, 'fluffy', ['strong', 'stealth', 'sonic beam'], 'super cute')
monster_3 = Monsters('Fred', 6, 'smooth as butter', ['mind reading', 'cooking', 'fire breath'], 'unbearable')

print(monster_1.name)
print(monster_1.eat())
print(monster_1.scare('HOOOOOOOLY MOLY'))
print(monster_1.transform())
print(monster_1.watch())

print('///////////////////////////////////////')

print(monster_2.name)
print(monster_2.eat('sushi'))
print(monster_2.scare())
print(monster_2.learn('DevOps'))
print(monster_2.exercise())

print('///////////////////////////////////////')

print(monster_3.name)
print(monster_3.eat())
print(monster_3.exercise('Power running'))
print(monster_3.learn())
print(monster_3.transform('Slug form'))
