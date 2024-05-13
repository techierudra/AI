import random


def monty_hall(simulations=1000):
    switch_wins = 0
    stay_wins = 0


    for _ in range(simulations):
        doors = [0, 0, 1]  # 0 represents a goat, 1 represents a car
        random.shuffle(doors)  # The prizes behind the doors are randomized


        # The player makes a choice
        choice = random.randint(0, 2)


        # Monty opens a door
        monty_opens = [i for i in range(3) if doors[i] == 0 and i != choice][0]


        # The player switches their choice
        switch_choice = [i for i in range(3) if i != choice and i != monty_opens][0]


        # Check if the player would win by switching or staying
        if doors[choice] == 1:
            stay_wins += 1
        if doors[switch_choice] == 1:
            switch_wins += 1


    print(f"Winning by staying with original door: {stay_wins/simulations}")
    print(f"Winning by switching doors: {switch_wins/simulations}")


monty_hall()
