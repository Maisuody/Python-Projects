import random
PlayGame = 'R'
while(PlayGame == 'R'):
    TheAnswer = random.randint(1, 50)
    TheInput = input('Please, Enter you random number between 1 to 50: ')
    TheInput = int(TheInput)
    count = 1

    while TheInput != TheAnswer:
        if TheInput < TheAnswer:
            print('your number is small')
        elif TheInput > TheAnswer:
            print('your number is large')
        TheInput = int(input('Please, Enter you random number between 1 to 50: '))
        count = count+1
    print('yes, you do it! after ' + str(count) + ' times')
    playGame = input('continue?')


