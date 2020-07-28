import random


def main():
    dice_rolls = 2
    dice_sum = 0  # Value begins at zero
    for i in range(0, dice_rolls):
        roll = random.randint(1, 6)  # Function performed twice
        dice_sum += roll  # Value of dice_sum is revised?
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
    main()
