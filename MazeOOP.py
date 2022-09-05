import json
import os

class Maze:
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


class VerifyChek:
    def chek(self):
        try:
            self.save = open('save.json')
            if self.save:
                if input('Do you want load save? (y) or (n):') == 'n':
                    i = 1
                    j = 0
                    self.save = {
                        'first': i,
                        'second': j
                    }
                    with open('save.json', 'w'):
                        json.dump(self.save, fp=open('save.json', 'w'))
        except FileNotFoundError:
            print('Not saves')
            i = 1
            j = 0
            self.save = {
                'first': i,
                'second': j
            }
            with open('save.json', 'w'):
                json.dump(self.save, fp=open('save.json', 'w'))

class QuestGo:
    def quest(self):
        self.value = input('Up, Right, Down, Left or End:')
        self.value = self.value[0].upper() + self.value[1:-1].lower() + self.value[-1].lower()

        if self.value != 'Up' and self.value != 'Left' and self.value != 'Down' and self.value != 'Right' and self.value != 'End':
            raise TypeError('Incorrect')

class SaveIt:
    def save(self):
        try:
            savestep = input('Do you want save step? (y) or (n)')
            if savestep == 'y':
                with open('save.json', 'w'):
                    json.dump(self.save, fp=open('save.json', 'w'))
            else:
                del self.save
        except ValueError:
            print('Incorrect value')

class Game(QuestGo, Maze, SaveIt, VerifyChek):
    def games(self):
        for k in range(0, len(Maze.maze)):
            self.save = json.load(open('save.json'))
            i = self.save['first']
            j = self.save['second']
            self.step = self.maze[i][j]

            if self.value == 'Down':
                self.step = self.maze[i + 1][j]
                if self.step != 0:
                    print(f'{self.name} Wall, you are back')
                else:
                    self.save = {
                        'first': i + 1,
                        'second': j
                    }
                    print(self.save)
                    with open('save.json', 'w'):
                        json.dump(self.save, fp=open('save.json', 'w'))
                    print(f'{self.name} Right way')

            elif self.value == 'Left':
                self.step = self.maze[i][j - 1]
                if self.step != 0:
                    print(f'{self.name} Wall, you are back')
                else:
                    self.save = {
                        'first': i,
                        'second': j - 1
                    }
                    with open('save.json', 'w'):
                        json.dump(self.save, fp=open('save.json', 'w'))
                    print(f'{self.name} Right way')

            elif self.value == 'Up':
                self.step = self.maze[i - 1][j]
                if self.step != 0:
                    print(f'{self.name}, Wall, you are back')
                else:
                    self.save = {
                        'first': i - 1,
                        'second': j
                    }
                    with open('save.json', 'w'):
                        json.dump(self.save, fp=open('save.json', 'w'))
                    print(f'{self.name} Right way')

            elif self.value == 'Right':
                self.step = self.maze[i][j + 1]
                if self.step != 0:
                    print(f'{self.name} Wall, you are back')
                else:
                    self.save = {
                        'first': i,
                        'second': j + 1
                    }
                    with open('save.json', 'w'):
                        json.dump(self.save, fp=open('save.json', 'w'))
                    print(f'{self.name} Right way')

            else:
                pass

            print(self.save)
            QuestGo.quest(QuestGo)
            k += 1

if __name__ == '__main__':
    x = Game('Dima')
    x.chek()
    x.quest()
    x.games()