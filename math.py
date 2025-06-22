import random
play_again = "y"
while True:
    if play_again == "n":
        break
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number3 = random.randint(1, 5)
    result = number1 + number2 * number3
    while True:
        try:
            player_answer = int(input(f"How much is {number1} + {number2} * {number3}? "))
        except ValueError:
            print("You have to input a normal number!")
            continue
        if player_answer == result:
            print("Good job!")
        else:
            print(f"Wrong. The answer is {result}.")
        while True:
          play_again = input("Wanna play again? Y/N ").lower()
          if play_again == "y":
              break
          elif play_again == "n":
              break
          else:
            print("You have to type 'Y' or 'N'!")
            continue
        break
