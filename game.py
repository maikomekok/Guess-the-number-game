import random

number = random.randint(1, 100)

steps = 0
warm = number + 5
warm_second = number - 5
cold= number+10
cold_second=number-10

while True:


    answer = input("Enter the number(0-100) or 'exit/გამოსვლა': ")
    if answer == "exit" or answer == "გამოსვლა":
        print("Bye bye! :)")
        break


    if not answer.isdigit():
        print("Please enter the digit!")
        continue


    answer = int(answer)

    if answer < 1 or answer > 100:
        print("Please enter the number inside 1-100 range!")
        continue

    steps += 1

    if answer == number:
        print("Congratulations, you won!", number)
        print(f"Amount of steps: {steps}")
        break

    elif answer==warm or answer==warm_second:
        print("WARM")
    elif answer==cold or answer==cold_second:
        print("COLD")

    elif answer > number:
        print("Your number is higher, try again!")
        continue


    else:
        print("Your number is lower, try again!")
        continue
