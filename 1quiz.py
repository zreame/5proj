print('\nWelcome to my computer quiz!\n')
playing = input('Wanna play? ')

if playing != 'yes' :
    quit()

print('\nOk lets go..')

score = 0
total = 0

total += 1
answer = input('\nWhat does CPU stand for? \n')
if answer.lower() == 'central processing unit' :
    print('\nCorrect!')
    score += 1
else :
    print('\nIncorrect')

total += 1
answer = input('\nWhat does GPU stand for? \n')
if answer.lower() == 'graphics processing unit' :
    print('\nCorrect!')
    score += 1
else :
    print('\nIncorrect')

total += 1
answer = input('\nWhat does PSU stand for? \n')
if answer.lower() == 'power supply unit' :
    print('\nCorrect!')
    score += 1
else :
    print('\nIncorrect')

total += 1
answer = input('\nWhat does RAM stand for? \n')
if answer.lower() == 'random access memory' :
    print('\nCorrect!')
    score += 1
else :
    print('\nIncorrect')

print(f'\n%-------------%\n\nYour total score is {score}!')

percent = score/total*100

if percent == int(percent) :
    print(f'You got {int(percent)}%!')
else :
    print(f'You got {percent:.1f}%!')

print('\n%--------------%\n')
