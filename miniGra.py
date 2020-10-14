"""
Napisz krótką grę w której masz 5 ruchów jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona: 75%
pomarańczowa: 20%
fioletowa: 4%
złota (legendarna): 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60% że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000
pomarańczowy - 4000
fioletowy - 9000
zlota - 16000
"""
import random

Box = [
    "zielony", 
    "pomarańczowy", 
    "fioletowy", 
    "zlota"
    ]
how_many_steps = int(input("How many steps forward you want to make ?"))
chance_box = [0,1]

Player_Score = []

def Journey(cage, how_many_steps):
    for step in range(1, (how_many_steps + 1)):
        rand = random.choices(chance_box, [40, 60], k=1)
        if rand == [1]:
            print("Step:",step)
            box_choice = (random.choices(Box, [75, 20, 4, 1]))
            print("You are lucky, you found the", str(box_choice), "box!")
            if box_choice == ["zielony"]:
                print("You have gained 1000 points !!")
                Player_Score.append(1000)
            elif box_choice == ["pomaranczowy"]:
                print("You have gained 4000 points !!")
                Player_Score.append(4000)                
            elif box_choice == ["fioletowy"]:
                print("You have gained 9000 points !!")
                Player_Score.append(9000)
            elif box_choice == ["zlota"]:
                print("You have gained 16000 points !!")
                Player_Score.append(16000)
        else :
            print("Step:",step)
            print("You have bad luck, there is nothing here")
    score = sum(Player_Score)
    print("Your final score is:",score)

Journey(Box, how_many_steps)
