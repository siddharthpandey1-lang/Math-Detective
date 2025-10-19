print("You have reached the second level")
print("Here are your next puzzles:")
print("which Number has a different property?")
print("4, 6, 8, 9, 10")
answer = input("Your answer: ")
if answer == "9":
    print("Correct! 9 is the only odd number in the list.")
else:
    print("Incorrect. The correct answer is 9, as it is the only odd number in the list.")
print("Here is your next puzzle:")
print("What is the next number in the sequence?")
print("2, 4, 8, 16, ?")
answer = input("Your answer: ")
if answer == "32":
    print("Correct! The next number is 32, as each number is multiplied by 2.")
else:
    print("Incorrect. The correct answer is 32, as each number is multiplied by 2.")
print("find out the wrong number in the series")   
print("5, 10, 15, 22, 25")
answer = input("Your answer: ")
if answer == "22":
    print("Correct! 22 does not fit the pattern of multiples of 5.")
else:
    print("Incorrect. The correct answer is 22, as it does not fit the pattern of multiples of 5.")
print("Well done on completing Level 2 puzzles!")
