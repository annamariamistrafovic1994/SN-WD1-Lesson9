secret = 2
guess = 0
cnt = 0

while guess != secret:
    if cnt >= 3:
        print("Game over")
        break

    guess = int(input("Pogodi broj između 1 i 30: "))

    if guess == secret:
        print("Bravo, broj je 2!")
    else:
        cnt = cnt + 1
        print("Sorry, fulo si.")
    print(cnt)


