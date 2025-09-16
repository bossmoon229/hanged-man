begin = input("Вітаю в грі повішений. Бажаєте почати? якщо так напишіть 'yes' ")

countChar = 0

word = ['w','o','r','d']
userWord = ['_', '_', '_', '_']
hangedMan =[
'+---+',
'|   |',
'    |',
'    |',
'    |',
'    |',
'=========',
]

# print(word.index('w'))
print(word)
# print(userWord)
# for line in hangedMan:
#     print(line)

if begin == 'yes':
    while True:
        if countChar == len(userWord):
            print('Ви виграли!')
            quit()

        userInput = input('Введіть літеру, яка на вашу думку може бути: ')
        if(userInput == 'quit'):
            quit()
        if(len(userInput) > 1 or len(userInput) == ''):
            print('Введіть будь ласка тільки одну літеру')
            continue

        else:
            if userInput in word:

                countChar += 1
                print('Гарна робота, ви вгадали літету' + userInput)
                indexRemove = word.index(userInput)
                userWord.pop(indexRemove)
                print(userWord)
                userWord.insert(word.index(userInput),userInput)
                print(userWord)


        # if userInput != chr(userInput)