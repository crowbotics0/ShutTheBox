
import Dice

viable_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flip_status_list = [False, False, False, False, False, False, False, False, False]
game_active = True
total_flips = 0

def check_addition_possibilities(dice_total):
     if dice_total <= 9 and flip_status_list[int(dice_total) - 1] == False:
          return True  
     else:
          for i in viable_numbers:
               for j in viable_numbers:
                    print(str(i) + " + " + str(j) + " = " + str(i+j) + ", actual: " + str(dice_total))
                    if i + j == dice_total and i != j:
                         print("possible")
                         return True
     return False
               
def is_move_valid(input, dice_total):
    if input.isdigit() == False:
         return False
    else:
         num_input = int(input)
         if num_input > 9 or num_input < 1:
              return False
         else:
              if num_input > dice_total or not num_input in viable_numbers:
                   return False
              else:
                   return True
              
def check_for_input(dice_total, total_flips):
     user_input = input()
     while(is_move_valid(user_input, total) == False):
         print("Number not valid. Please try again.")
         user_input = input()

     total_flips = total_flips + 1
     num_input = int(user_input)
     dice_total = dice_total - num_input
     flip_status_list[num_input - 1] = True
     viable_numbers.remove(num_input)
     return dice_total

while len(viable_numbers) > 0:
    print("~~ Current Box ~~")

    for num in range(9):
            if flip_status_list[num] == False:
                print(str(num + 1), end = " ")
            else:
                print("_", end=" ")

    print("\n~~ Your Dice Roll ~~")
    dice1 = Dice.roll()
    dice2 = Dice.roll()
    total = dice1 + dice2

    print("First dice is " + str(dice1))
    print("Second dice is " + str(dice2))
    print("Total is " + str(total))

    print("~~ Choose Number to Flip ~~")

    if check_addition_possibilities(total):
          while total > 0:
               total = check_for_input(total, total_flips)
               if total != 0:
                    print("Please flip another number")
    else:
         print("addition not possible")
         break

    game_active = False


