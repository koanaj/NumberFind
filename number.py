#program do zgadywania liczby

import random, sys

def clos():
    print('do widzenia'\
          ' nastepnym razem')
    sys.exit()

print('jak masz na imie?: ')
name = input()

print('ok, witam ' + name + ' mysle nad liczba od 0 do 50 ')
liczba = random.randint(0,50)

#print('DEBUG '+str(liczba))

for ilosczgadyw in range(1, 7):
    print('zgaduj liczbe: ')
    zgad = int(input())

    if zgad < liczba:
        print('za niska')
    elif zgad > liczba:
        print('za wysoka')
    else:
        break # jak wykorzysta range (1-7) 6 razy zle odpowie

if zgad == liczba:
    print('dobra robota ' + name + ' odgadywanie zajelo: ' + str(ilosczgadyw) + ' prob!')
else:
    print('niestety, liczba ktora wylosowalem to: ' + str(liczba))

clos()
