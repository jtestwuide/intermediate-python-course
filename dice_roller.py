import random


def main():
    dice_rolls = int(input('How many die would you like to roll?: '))
    dice_size = int(input('How many sides are the dice?: '))
    dice_sum = 0  # Value begins at zero
    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)  # Function instances depending on usr input
        dice_sum += roll  # Value of dice_sum is revised?
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success!')
        else:
            print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
    main()
