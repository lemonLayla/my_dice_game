from random import randint
random_num = randint(1,6)
#print(random_num)



#for i in range(1):
your_guess= int(input('guess here '))
print(your_guess)


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

if your_guess ==random_num:
 print('correct! you win  :)')
else:
    print('maybe next time loser ;)')