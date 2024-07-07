
print("Hello")

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flip_status_list = [False, False, False, False, False, False, False, False, False]

for num in range(9):
        if flip_status_list[num] == False:
            print(str(num + 1), end = " ")
        else:
            print("_", end=" ")
