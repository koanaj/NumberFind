#program do zgadywania liczby

import random, sys

def clos():
    print('goodbye'\
          ' until next time')
    sys.exit()

print('what is your name?: ')
name = input()

print('ok, hello ' + name + ' im thinking of a number between 0 and 50 ')
liczba = random.randint(0,50)

#print('DEBUG '+str(liczba))

for ilosczgadyw in range(1, 7):
    print('take a guess: ')
    zgad = int(input())

    if zgad < liczba:
        print('too low')
    elif zgad > liczba:
        print('too high')
    else:
        break # jak wykorzysta range (1-7) 6 razy zle odpowie

if zgad == liczba:
    print('good job ' + name + ' you managed in: ' + str(ilosczgadyw) + ' guesses!')
else:
    print('unfortunately, the number was: ' + str(liczba))

clos()
