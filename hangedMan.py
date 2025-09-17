begin = input("Вітаю в грі повішений. Бажаєте почати? якщо так напишіть 'yes' ")

wrondAnswer = []
word = ['w','o','r','d']
userWord = ['_', '_', '_', '_']
stages = [
    [
        "+---+",
        " |  |",
        "    |",
        "    |",
        "    |",
        "    |",
        "========="
    ],
    [
        "+---+",
        " |  |",
        " O  |",
        "    |",
        "    |",
        "    |",
        "========="
    ],
    [
        "+---+",
        " |  |",
        " O  |",
        "|   |",
        "    |",
        "    |",
        "========="
    ],
    [
        "+---+",
        " |  |",
        " O  |",
        "/|  |",
        "    |",
        "    |",
        "========="
    ],
    [
        "+---+",
        " |  |",
        " O  |",
        "/|\\ |",
        "    |",
        "    |",
        "========="
    ],
    [
        "+---+",
        " |  |",
        " O  |",
        "/|\\ |",
        "/   |",
        "    |",
        "========="
    ],
    [
        "+---+",
        " |  |",
        " O  |",
        "/|\\ |",
        "/ \\ |",
        "    |",
        "========="
    ]
]


mistakes = -1

if begin == 'yes':
    while True:
        if mistakes+1 == len(stages):
            print('Ви програли :(')
            quit()
        if '_' not in userWord:
            print('Ви виграли!, Ваше слово ' + ''.join(userWord))
            quit()
        userInput = input('Введіть літеру, яка на вашу думку може бути: ')
        if userInput == 'quit':
            quit()
        if len(userInput) > 1 or len(userInput) == '':
            print('Введіть будь ласка тільки одну літеру')
            continue
        if userInput in wrondAnswer:
            print('Ви вже вводили цю літеру')
            continue
        if userInput not in word:
            mistakes+=1
            for line in stages[mistakes]:
                print(line)
            wrondAnswer.append(userInput)
        else:
            if userInput in word:
                print('Гарна робота, ви вгадали літету ' + userInput)
                indexRemove = word.index(userInput)
                userWord.pop(indexRemove)
                userWord.insert(word.index(userInput),userInput)
                print(''.join(userWord))
                # print(userWord)