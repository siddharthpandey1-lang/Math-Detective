print("you have reached the third level")
print("Here are your next puzzles:")
print("Identify the wrong number in the series?")
print("3, 6, 9, 12, 15, 18, 20")
answer = input("Your answer: ")
if answer == "20":
    print("Correct! 20 does not fit the pattern of multiples of 3.")
else:
    print("Incorrect. The correct answer is 20 because it does not fit the pattern of multiples of 3.")
print("Here is your next puzzle:")  
print("What is the next number in the sequence?")
print("5, 10, 20, 40, ?")
answer = input("Your answer: ")
if answer == "80":
    print("Correct! The next number is 80, as each number is multiplied by 2.")
else:
    print("Incorrect. The correct answer is 80, as each number is multiplied by 2.")
print("Find the odd one out in the series")
print("7, 14, 21, 28, 36, 42")
answer = input("Your answer: ")
if answer == "36":
    print("Correct! 36 is not a multiple of 7.")
else:
    print("Incorrect. The correct answer is 36 because it is not a multiple of 7.")