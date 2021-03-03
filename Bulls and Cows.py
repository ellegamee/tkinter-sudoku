#Bulls and Cows
import random
code = []
player = []
output = ['_', '_', '_', '_']
guess = 0
guesses = 0
maxvalue = 9
minvalue = 0
bulls = 0
cows = 0
goats = 0

# Random code
for i in range(0, 4):
    code.append(random.randint(0, 9))
print(code)

while guesses < 11:
    # Player guess list
    player = []

    # Players input
    for i in range(0, 4):
        while True:
            try:
                guess = int(
                    input('Skriv in ett tal mellan {} och {}: '.format(minvalue, maxvalue)))

            except:
                print('Skriv in ett tal mellan {} och {}\n '.format(
                    minvalue, maxvalue))
                continue

            if guess < minvalue or guess > maxvalue:
                print('Skriv in ett tal mellan {} och {}\n '.format(
                    minvalue, maxvalue))
                continue

            else:
                player.append(guess)
                break

    # Debug
    print(code)
    print(player)

    # Compare
    bulls = 0
    cows = 0
    goats = 0

    # If they are same
    for j in range(0, len(player)):

        # Bull
        if player[j] == code[j]:
            output.pop(j)
            output.insert(j, 'B')
            bulls += 1

        # Cow
        elif player[j] in code:
            output.pop(j)
            output.insert(j, 'C')
            cows += 1

        # Goat
        else:
            output.pop(j)
            output.insert(j, 'G')
            goats += 1

    print(output, '\nAntal Bulls {}, Antal Cows {}, Antal Goats {}\n'.format(
        bulls, cows, goats))
    guesses += 1
