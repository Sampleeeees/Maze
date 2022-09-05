import json
import os
class MazeLevel():
    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def __init__(self, name):
        self.name = name

    def cheksave(self):
        k = 0
        i = 1
        j = 0
        global walk
        try:
            walk = json.load(open('save.json'))
            if walk:
                if input('Load your save?(y) or (n):') == 'n':
                    os.remove('save.json')
                else:
                    #print(walk)
                    i = walk['first']
                    j = walk['second']
                    #print(i, j)
                    step = self.maze[i][j]
                    #print(step)

        except FileNotFoundError:
            print('No saves available')
            step = self.maze[i][j]
            print(step, i, j)
                # print(step)

    def moves(self):
        global walk
        correct_step = ['Right', 'Right', 'Down', 'Down', 'Left', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right', 'Right', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right', 'Down', 'Down', 'Left', 'Down', 'Down', 'Left', 'Down', 'Down', 'Right', 'Down', 'Right', 'Right']
        k = 0
        i = 1
        j = 0
        for k in range(0, len(correct_step)):
            try:
                walk = json.load(open('save.json'))
                print(walk)
                i = walk['first']
                j = walk['second']
                print(i, j)
                step = self.maze[i][j]
                print(step)
            except FileNotFoundError:
                pass
            #Введення кроку та форматування слова у випадку не правильного розміру
            value = input('Up, Right, Down, Left or End:')
            value = value[0].upper() + value[1:-1].lower() + value[-1].lower()

            #Перевірка корекності введених данних
            if value != 'Up' and value != 'Left' and value != 'Down' and value != 'Right' and value != 'End':
                raise TypeError('Incorrect')

            #Код з кроками після введеня
            if value == 'Up':
                step = self.maze[i-1][j]
                if step != 0:
                    print(f'{self.name} Wall, you are back')
                else:
                    save = {
                        'first': i - 1,
                        'second': j
                    }
                    print(save)
                    with open('save.json', 'w') as outfile:
                        json.dump(save, outfile)
                    print(f'{self.name} Right way')

            if value == 'Left':
                step = self.maze[i][j-1]
                if step != 0:
                    print(f'{self.name} Wall, you are back')
                else:
                    save = {
                        'first': i,
                        'second': j - 1
                    }
                    with open('save.json', 'w') as outfile:
                        json.dump(save, outfile)
                    print(f'{self.name} Right way')

            if value == 'Right':
                step = self.maze[i][j+1]
                #Останній вірний крок вправо тому перевірка знаходиться тут
                if i == 14 and j == 10:
                    print(f'{self.name}, welcome')
                    break
                if step != 0:
                    print(f'{self.name} Wall, you are back')
                else:
                    save = {
                        'first': i,
                        'second': j + 1
                    }
                    #print(save)
                    with open('save.json', 'w') as outfile:
                        json.dump(save, outfile)
                    print(f'{self.name} Right way')

            if value == 'Down':
                step = self.maze[i + 1][j]
                if step != 0:
                    print(f'{self.name} Wall, you are back')
                else:
                    save = {
                        'first': i + 1,
                        'second': j
                    }
                    with open('save.json', 'w'):
                        json.dump(save, fp=open('save.json', 'w'))
                    print(f'{self.name} Right way')
            #Якщо гравець хоче закінчити гру
            if value == 'End':
                if input('Do you have save? (y) or (no):') == 'y':
                    with open('save.json', 'w'):
                        json.dump(save, fp=open('save.json', 'w'))
                        break
                else:
                    del save
                    break

            k += 1
            #with open('save.json', 'w') as outfile:
            #   json.dump(step, outfile)



x = MazeLevel('Niko')
x.cheksave()
x.moves()