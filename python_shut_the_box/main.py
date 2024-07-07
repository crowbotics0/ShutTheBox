
import Dice

flip_status_list = [False, False, False, False, False, False, False, False, False]
game_active = True

while game_active:

    print("~~ Current Box ~~")

    for num in range(9):
            if flip_status_list[num] == False:
                print(str(num + 1), end = " ")
            else:
                print("_", end=" ")

    print("\n~~ Your Dice Roll ~~")
    dice1 = Dice.roll()
    dice2 = Dice.roll()

    print("First dice is " + str(dice1))
    print("Second dice is " + str(dice2))
    print("Total is " + str(dice1+ dice2))

    game_active = False


