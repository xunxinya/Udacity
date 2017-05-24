import string

#test and answers for different levels
quiz_data = {
'easy':
{
    'text':
        '''
        ___1___ is the most basic building block of the Web.\n
        It describes and defines the content and structure of a webpage.\n
        ___2___ is generally used to describe a webpage's appearance and style.\n
        Individual components of an ___1___ document are called ___3___s,\n
        which are generally positioned as spanning from a start ___4___,\n
        and is terminated by an end ___4___.\n
        ''',
    'answer':
        ['HTML','CSS','element','tag']
},
'medium':
{
    'text':
        '''
        A ___1___ is a sequence of instructions that is continually repeated until a certain condition is reached.\n
        A ___2___ ___1___ is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.\n
        A ___1___ becomes ___3___ if a condition never becomes False.\n
        Another control flow tool is ___4___ statement, which is used to check a condition:\n
        ___4___ the statement is true, we run a block of statements,\n
        ___5___ we process another block of statements. \n
        The ___5___ clause is optional.\n
        ''',
    'answer':
        ['loop','while','infinite','if','else']
},
'hard':
{
    'text':
        '''
        A ___1___ definition is created with the def keyword.\n
        You specify the inputs a ___1___ takes by adding parameters or ___2___s separated by commas between the parentheses.\n
        Function can return a value, and the return statement ___3___s a function.\n
        ___1___s by default return ___4___ if you don't specify the value to return.\n
        ___2___ can be standard data types such as string, number, dictionary, tuple, and ___5___ or more complicated such as objects.\n
        The ___1___ definition does not execute the ___1___ body, it gets executed only when the ___1___ is ___6___ed.\n
        ''',
    'answer':
        ['function','argument','exit','None','list','call']
}
}

validLevel = ['1', '2', '3']

#prompt user to choose difficulty level
def chooseLevel():

    level_number = input('''
    Let's select the difficulty level first!\n
    1 - easy level\n
    2 - midium level\n
    3 - hard level\n
    Please enter the level number:
    ''')

    while level_number not in validLevel:
        level_number = input('''That choice is not available with us! please choose again:''')

    if level_number == '1':
        level = 'easy'
    elif level_number == '2':
        level = 'medium'
    elif level_number == '3':
        level = 'hard'

    return level

#prompt user to choose max number of trial
def chooseAttempts():

    attempts = int(input('''
    You may decide on your chance of winning!\n
    Please enter the max number of attempts you'd like:
    '''))

    while attempts < 1:
        attempts = input('''Give yourself more chance! Enter again:''')

    return attempts

#print out paragraph according to choice of difficulty level
def printTest(level):

    print('''
    Let's take a look at your paragraph!\n
    Try your best to think of the possible solutions to fill in the blanks!\n''')

    print(quiz_data[level]['text'])

#print out paragraph with certain blank(s) filled
def printFilled(level, i):

    print('''
    Let's take a look at your next challenge!
    ''')

    filledPara = quiz_data[level]['text']

    for i in range(1, i+1):
        filledPara = filledPara.replace(str(i), quiz_data[level]['answer'][i-1])

    print(filledPara)


#prompt user to attempt guess of a certain blank
def runTrial(level, attempts, i):

    if i!= 0:
        printFilled(level, i)

    answer = quiz_data[level]['answer'][i]
    trial = 1
    blank = str(i+1)

    guess = input('Please enter your answer of blank number ' + blank + ': ')

    while guess != answer:
        guess = input('''That's not quite it... Guess again: ''')
        trial += 1
        if trial == attempts:
            print('''Your chance is over!''')
            return False

    print('Yeah you got it! \nThe correct answer of blank number ' + blank + ' is: ' + answer)
    return True

#iterate test on each blank
def runTest(level, attempts):

    for i in range(len(quiz_data[level]['answer'])):
        result = runTrial(level, attempts, i)
        if not result:
            return False

    return True

#main
print('''Let's start the quiz and have some fun!\n''')
level = chooseLevel()
attempts = chooseAttempts()
printTest(level)
Pass = runTest(level, attempts)
if Pass:
    print('''Congratulations! You have passed the quiz!\n''')
else:
    print('''What a pity that you didn't pass! You can try again!''')
