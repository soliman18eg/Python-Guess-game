#
#
# import random
# def guess_number():
#     # Get the number of tries and range from the user
#     num_tries = int(input("Enter the number of tries: "))
#     start = int(input("Enter the start of the range: "))
#     stop = int(input("Enter the end of the range: "))
#     # Choose the search method
#     search_method = input("Choose a search method (random/linear/binary): ")
#
#     # Generate a random target number within the given range
#     target = random.randint(start, stop)
#     low = start
#     high = stop
#
#
#
#
#
#     if search_method == "random" or "Random":
#         while num_tries != 0:
#             guess = random.randint(start, stop)
#             while True:
#                 num = input("Please enter a gussing number ")
#                 try:
#                     val = int(num)
#                     print("your Input is an integer number.")
#                     print("your Input number is: ", val)
#                     break
#                 except ValueError:
#                     try:
#                         val = float(num)
#                         print("your Input is an float number.")
#                         print("Your Input number is: ", val)
#                         break
#                     except ValueError:
#                         print("This is not a number. Please enter a valid number")
#
#             print(f'Number of tries remaining: {num_tries}')
#
#             guess = int(input('Enter your guess: '))
#
#             if guess == target:
#                 print("you guessed the correct number")
#                 return
#             elif guess < target:
#                 print("guess higher")
#             else:
#                 print("guess lower")
#             num_tries -= 1
#         print("you have failed to guess the number:")
#
#
#     elif search_method == "Linear" or "linear":
#         for i in range(start, stop + 1):
#
#             # decrement tries
#             num_tries -= 1
#
#             if i == target:
#                 # print success message
#                 print("The computer guessed the number correctly!")
#                 # print number of tries left
#                 print("The computer had", num_tries, "tries left.")
#                 # return
#                 return
#
#             else:
#                 # print guess message
#                 print("The computer guessed", i)
#                 # if tries is equal to 0
#                 if num_tries == 0:
#                     # print failure message
#                     print("The computer failed to guess the number.")
#                     # return
#                     return
#
#
#     elif search_method == "binary" or "Benary":
#         for i in range(num_tries):
#             # Check if the low index is greater than the high index, which means the randum_num number is not within the range
#             if low > high:
#                 print("The number could not be found within the given range.")
#                 return
#
#             # Calculate the midpoint of the current range
#             mid = (low + high) // 2
#             # Check if the randum_num number is the midpoint
#             if target == mid:
#                 print("The number was found after {} tries.".format(i + 1))
#                 return
#             # If the randum_num number is less than the midpoint, update the high index to be the midpoint - 1
#             elif target < mid:
#                 high = mid - 1
#                 print("guess higher")
#
#
#             # If the randum_num number is greater than the midpoint, update the low index to be the midpoint + 1
#             else:
#                 low = mid + 1
#                 print("guess lower")
#
#             # If the number of tries has been exceeded, print an appropriate failure message
#         print("The number could not be found within {} tries.".format(num_tries))
#
#     else:
#         print("invalid Methods")
# guess_number()
####################################################################
##### HI Andrew I am was trying to compain the mehods toagther but
# chose one method over theother is not woking i keeep picking up the random method over the others


### if i separat each method it work

import random
def guess_number():


  # Get the number of tries and range from the user
  num_tries = int(input("Enter the number of tries: "))
  start = int(input("Enter the start of the range: "))
  stop = int(input("Enter the end of the range: "))
  # Choose the search method
  search_method = input("Choose a search method (random/linear/binary): ")

  # Generate a random target number within the given range
  target = random.randint(start, stop)

  low = start
  high = stop
  # if search_method == "random" or "Random":
  #     while num_tries != 0:
  #
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
  #         print(f'Number of tries remaining: {num_tries}')
  #
  #         guess = int(input('Enter your guess: '))
  #
  #         if guess == target:
  #             print("you guessed the correct number")
  #             return
  #         elif guess < target:
  #             print("guess higher")
  #         else:
  #             print("guess lower")
  #         num_tries -= 1
  #     print("you have failed to guess the number:")

  elif search_method == "binary" or "Benary":
      for i in range(num_tries):
          # Check if the low index is greater than the high index, which means the randum_num number is not within the range
          if low > high:
              print("The number could not be found within the given range.")
              return

          # Calculate the midpoint of the current range
          mid = (low + high) // 2
          # Check if the randum_num number is the midpoint
          if target == mid:
              print("The number was found after {} tries.".format(i + 1))
              return
          # If the randum_num number is less than the midpoint, update the high index to be the midpoint - 1
          elif target < mid:
              high = mid - 1
              print("guess higher")


          # If the randum_num number is greater than the midpoint, update the low index to be the midpoint + 1
          else:
              low = mid + 1
              print("guess lower")

          # If the number of tries has been exceeded, print an appropriate failure message
      print("The number could not be found within {} tries.".format(num_tries))

  elif search_method == "Linear" or "linear":
      for i in range(start, stop + 1):

          # decrement tries
          num_tries -= 1

          if i == target:
              # print success message
              print("The computer guessed the number correctly!")
              # print number of tries left
              print("The computer had", num_tries, "tries left.")
              # return
              return

          else:
              # print guess message
              print("The computer guessed", i)
              # if tries is equal to 0
              if num_tries == 0:
                  # print failure message
                  print("The computer failed to guess the number.")
                  # return
                  return



guess_number()




