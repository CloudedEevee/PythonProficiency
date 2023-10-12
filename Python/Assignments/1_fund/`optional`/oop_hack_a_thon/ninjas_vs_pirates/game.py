from classes.ninja import Ninja
from classes.pirate import Pirate



michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")



while jack_sparrow.health > 0 and michelangelo.health > 0:
    
    can_attack = michelangelo.attack(jack_sparrow)
    if can_attack and jack_sparrow.health > 0:
        jack_sparrow.show_stats()
        can_attack = jack_sparrow.attack(michelangelo)
        if can_attack and michelangelo.health > 0:
            michelangelo.show_stats()
    elif jack_sparrow.health < 0:
        break

if jack_sparrow.health <= 0:
    is_winner = michelangelo.name
elif michelangelo.health <= 0:
    is_winner = jack_sparrow.name

print(f"{is_winner} wins!!")
