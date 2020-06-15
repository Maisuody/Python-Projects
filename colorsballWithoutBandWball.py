nonDesireditem = ['black', 'white']
numOFballs = int(input('Enter the number of balls: '))
ballsList = []
Finalball = []
for balls in range(numOFballs):
    temp = input('enter the name: ')
    while temp == '': #you already have to used to handel all cases in you code dude!
        temp = input('you are not enter the name: ')
    ballsList.append(temp)
for balls in ballsList:
    if balls not in nonDesireditem:
        Finalball.append(balls)
print('There is' + str(len(Finalball)) + 'in you list')
print(*sorted(Finalball), sep='\n')

