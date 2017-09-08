import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print()
    print('-----------------------------------------------------------------------')
    print('''
       (  )   /\   _                 (
        \ |  (  \ ( \.(               )                      _____
      \  \ \  `  `   ) \             (  ___                 / _   \\
     (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
    - .-               \+  ;          (  O                           \____
         WIZARD BATTLE        )        \_____________  `              \  /
    (__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
    (_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
      .    /./.+-  . .- /  +--  - .     \______________//_              \_______
      (__ ' /x  / x _/ (                                  \___'          \     /
     , x / ( '  . / .  /                                      |           \   /
        /  /  _/ /    +                                      /              \/
       '  (__/                                             /                  \\
        ''')
    print()
    print('-----------------------------------------------------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 20, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    # print(creatures)

    while True:

        active_creature = random.choice(creatures)
        print()
        print('A {} of level {} has appear from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)  # if creature is defeated, it should be removed from active creatures
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)  # delay 5 seconds
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard has become unsure of his powers and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the sorroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('OK, exiting game... bye!')
            break

        if not creatures:  # This is 'activated' if creatures-list is empty
            print("You've defeated all the creatures, well done!")
            break

if __name__ == '__main__':
    main()

