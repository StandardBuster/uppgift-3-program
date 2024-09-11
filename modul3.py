import os
import random
import math

os.system('cls')


name = str(input("What's your name, boy?: "))
while True:
    try:
        age = int(input("HOW OLD YOU ARE?: "))
        break
    except:
        print("Only use numbers mistah!")
        continue


age = int(input("your age: "))

if age >= 18 :          #Krokodilmunnen äter det större talet
    print("You can come inside my pub")

else: 
    print("You're too little - Get lost scrub!")



if age == 18:   #variabel - datatyp: int
    print("You are just old enough!")


elif age > 18:  #else if
    print("You're older than 18 - and elite")

elif age < 15:
    print("You are younger than 15 and have to seriously level up bro!")

else: 
    print("You are GAY")




# 1) Om baldur är (TRUE) och du är 1.4 eller högre kan du få min banan.
# 2) Man kan bara få min banan om du är mellan 1.4 och 1.99

# 3) se till att programmet är tydlig med att attraktionen är av och det är därför ud inte får åka eller för att du är fel höjd



baldur_online = True

if baldur_online:
    while True:
        try:
            height = float(input("Höjd: "))
            break
        except:
            print("Skriv höjd i nummer")
            continue

if baldur_online == True:           #baldur_online == True
    if height >= 1.4 and height <= 1.99:
        print("Du kan får åka min bana")
    else:
        print("Du får inte åka min bana")

else:
    print("Baldur är tyvärr borta")

if height <= 1.7: 
    print("YOU ARE TOO SHORT DWARF")

else:
    print("Hey there, dont hit your head!")






fire_alarm = True
fire_extinguisher = True

if fire_alarm == True and fire_extinguisher == True:
    print("ALARM, but everyone has extinguishers!")

elif fire_alarm and fire_extinguisher == False:
    print("ALARM, nobody has any extinguishers!")
elif not fire_alarm and not fire_extinguisher:
    print("Everything is fine and buy fire extinguishers")
elif not fire_alarm and fire_extinguisher:
    print("Everything is fine - no fire. You have fire extinguishers!")
else:
    print("Everything is fine - school's open!")




from random import randint



print(random.randint(1, 6))



random_number = randint(1, 6)

random_number=0

while random_number != 6:
    random_number = randint(1, 6)
    print(random_number)


dice = int(input("How many dice? "))

rolls = dice

while True: 
    die = randint(1, 6)
    print(die)
    rolls -= 1
    if rolls == 0:
        break



while True:
    try:
        dice = int(input("How many dice? "))
        rolls = 0
        while rolls < dice:
            die = randint(1, 6)
            print(die)
            rolls += 1
        break
    except:
        print("Please input a number")
        continue



while True:
    try: 
        Height = float(input("What's your height?: "))
        Weight = float(input("How much do you weigh?: "))
        break
    except:
        print("Please input numbers")
        continue

print("You weight is:", Weight/Height**2)



radius = float(input("Put in the radius of the circle: "))

area = math.pi*radius**2

print("area of the circle is: ", area)








