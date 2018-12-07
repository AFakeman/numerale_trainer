import random
import sys

if len(sys.argv) != 2:
    print("Verwendung: python3 trainer.py <Anzahl>")

count = int(sys.argv[1])
correct = 0

with open("dictionary.txt") as f:
    numerals = [tuple(row.split('\t')) for row in f]

for i in range(count):
    tup = random.choice(numerals)
    numerals.remove(tup)
    number, numerale = tup
    numerale = numerale.strip()
    inp = input("Numerale für {}: ".format(number))
    if (numerale != inp):
        print("Falsche Antwort! Es ist {}".format(numerale))
    else:
        print("Richtich!")
        correct += 1

print("Richtich: {}/{}".format(correct, count))
