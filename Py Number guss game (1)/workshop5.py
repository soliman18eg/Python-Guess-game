# import random
#
# def guess_random_number(tries, start, stop):
#     target_number = random.randint(start, stop)
#     while tries != 0:
#         while True:
#             num = input("Please enter a gussing number ")
#             try:
#                 val = int(num)
#                 print("your Input is an integer number.")
#                 print("your Input number is: ", val)
#                 break
#             except ValueError:
#                 try:
#                     val = float(num)
#                     print("your Input is an float number.")
#                     print("Your Input number is: ", val)
#                     break
#                 except ValueError:
#                     print("This is not a number. Please enter a valid number")
#
#         print(f'Number of tries remaining: {tries}')
#
#         guess = int(input('Enter your guess: '))
#
#
#         if guess == target_number:
#             print("you guessed the correct number")
#             return
#         elif guess < target_number:
#             print("guess higher")
#         else:
#             print("guess lower")
#         tries -= 1
#     print("you have failed to guess the number:")
# guess_random_number(5, 0, 10)

#################################################################################
#Task 2

# import random
#
# #define function guess_random_num_linear
# def guess_random_num_linear(tries, start, stop):
#     # generate random number between start and stop
#     random_num = random.randint(start, stop)
#     # print random number
#     print("The random number is:", random_num)
#     # loop through the range of start and stop
#     for i in range(start, stop + 1):
#         # decrement tries
#         tries -= 1
#         # if i is equal to random number
#         if i == random_num:
#             # print success message
#             print("The computer guessed the number correctly!")
#             # print number of tries left
#             print("The computer had", tries, "tries left.")
#             # return
#             return
#
#         else:
#             # print guess message
#             print("The computer guessed", i)
#             # if tries is equal to 0
#             if tries == 0:
#                 # print failure message
#                 print("The computer failed to guess the number.")
#                 # return
#                 return
#
# # call function guess_random_num_linear
# guess_random_num_linear(5, 0, 10)



################################################

# #task 3
import random


def guess_random_num_binary(tries, start, stop):
    # Generate a random number between start and stop, inclusive
    randum_num = random.randint(start, stop)
    print("The random number to find is:", randum_num)

    # Initialize the low and high indices for the binary search
    low = start
    high = stop

    # Implement the binary search algorithm
    for i in range(tries):
        # Check if the low index is greater than the high index, which means the randum_num number is not within the range
        if low > high:
            print("The number could not be found within the given range.")
            return

        # Calculate the midpoint of the current range
        mid = (low + high) // 2
        # Check if the randum_num number is the midpoint
        if randum_num == mid:
            print("The number was found after {} tries.".format(i + 1))
            return
        # If the randum_num number is less than the midpoint, update the high index to be the midpoint - 1
        elif randum_num < mid:
            high = mid - 1
            print("guess higher")


        # If the randum_num number is greater than the midpoint, update the low index to be the midpoint + 1
        else:
            low = mid + 1
            print("guess lower")

    # If the number of tries has been exceeded, print an appropriate failure message
    print("The number could not be found within {} tries.".format(tries))
guess_random_num_binary(10, 0, 100)
guess_random_num_binary(5, 0, 100)
guess_random_num_binary(5, 0, 1000)
guess_random_num_binary(6, 0, 50)
guess_random_num_binary(6, 0, 100)
guess_random_num_binary(12, 0, 10000)