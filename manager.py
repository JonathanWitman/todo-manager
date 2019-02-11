import datetime

class Var(object):
    lines = []
    time = str(datetime.datetime.now())

class Manager(object):

    def print():
        for i in range(0,len(Var.lines)):
            print(Var.lines[i])

    def clear():
        open('todos.txt', 'w').close()

    def update():
        a = open("todos.txt", "rt")
        for line in a:
            Var.lines.append(line)

    def write():
        Manager.clear()
        a = open("todos.txt", "w")
        for item in lines:
            a.write(item)

    def done(input):
        current = Var.lines[input - 1]
        if current.startswith("DONE!!"):
            print('this item is already completed')
        else:
            Var.lines.insert(input - 1, "DONE!! " + current)
            Var.lines.remove(current)
            Manager.write()
