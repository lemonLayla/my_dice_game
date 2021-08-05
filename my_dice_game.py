from random import randint
random_num = randint(1,6)
#print(random_num)

print('Hello and welcome to layla','s dice game this game is fun an simple as 1-2-3')
print('all you have to do is guess the number the six sided dice is going to land on. ')
print('     ')
print('but you only git 2 guesss')
print('     ')
your_guess=0

for i in range(2):
    if your_guess != random_num:
        your_guess= int(input('1-6 now take your pick and guess here : '))
        print('     ')
        if your_guess ==random_num:
            print('correct! you win  :)')
        else:
            print('maybe next time loser ;)')

if random_num == 1:

    for m in range(1, 2):
        print('     .-------. ' )
        print('    /       / | ')
        print('   /_______/  |' )
        print('   |       |  /' )
        print('   |   o   | /'  )
        print('   |_______|/ '  )


if random_num == 2:

    for y in range(1, 2):
        print('     .-------. ' )
        print('    /       / | ')
        print('   /_______/  |' )
        print('   | o     |  /' )
        print('   |    o  | /'  )
        print('   |_______|/ '  )


if random_num == 3:

    for d in range(1, 2):
        print('     .-------. ' )
        print('    /       / | ')
        print('   /_______/  |' )
        print('   |       |  /' )
        print('   | o o o | /'  )
        print('   |_______|/ '  )


if random_num == 4:

    for i in range(1, 2):
        print('     .-------. ' )
        print('    /       / | ')
        print('   /_______/  |' )
        print('   | o   o |  /' )
        print('   | o   o | /'  )
        print('   |_______|/ '  )


if random_num == 5:

    for c in range(1, 2):
        print('     .---------. ' )
        print('    /        / | ')
        print('   /________/  |' )
        print('  | o    o |   /' )
        print('  |   o    |  /'  )
        print('  | o    o | / '  )
        print('  |________|/  ')


if random_num == 6:

    for e in range(1, 2):
        print('     .-------. ' )
        print('    /       / | ')
        print('   /_______/  |' )
        print('   | o o o |  /' )
        print('   | o o o | /'  )
        print('   |_______|/ '  )

