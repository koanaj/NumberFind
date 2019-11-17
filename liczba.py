#program do zgadywania liczby

import random, sys

def clos():
    print('do widzenia'\
          ' nastepnym razem')
    sys.exit()

print('jak masz na imię?: ')
name = input()

print('ok, witam ' + name + ' mysle nad liczba od 0 do 50 ')
liczba = random.randint(0,50)

#print('DEBUG '+str(liczba))

for ilosczgadyw in range(1, 7):
    print('zgaduj ')
    zgad = int(input())

    if zgad < liczba:
        print('za nisko')
    elif zgad > liczba:
        print('za wysoko')
    else:
        break # jak wykorzysta range (1-7) 6 razy zle odpowie

if zgad == liczba:
    print('dobrze ' + name + ' dales rade w ' + str(ilosczgadyw) + ' powtorzen!')
else:
    print('niestety, liczba o ktorej myslalem to ' + str(liczba))

clos()