import random


END = 0


counter = 10

while counter >= END:
    print(counter)
    counter -= 1


def guess_number():
    return int(input("Please guess number between 1 and 10: "))


def computer_guess():
    return random.randint(1, 10)


def start_play():
    computer_number = computer_guess()
    user_number = guess_number()

    while computer_number != user_number:
        user_number = guess_number()


def counter(start, end, is_down=False):
    step = 1
    stop = 1

    if is_down:
        start, end = end, start
        step = -1
        stop = -1

    for number in range(start, end + stop, step):
        print(number, end=" ")

    print()


# start_play()

# from 10 to 0


print("#" * 100)

for i in range(10, 0, -1):
    print(i)


print("#" * 100)
counter(10, 20)
print("#" * 100)
counter(10, 20, is_down=True)

print("Well Done")
