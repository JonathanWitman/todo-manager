import item

class Manager(object):

    def print():
        for i in range(0,len(item.lines)):
            print(item.lines[i])

    def clear():
        open('todos.txt', 'w').close()

    def update():
        a = open("todos.txt", "rt")
        for line in a:
            item.lines.append(line)

    def write():
        Manager.clear()
        a = open("todos.txt", "w")
        for item in lines:
            a.write(item)

    def done(input):
        current = item.lines[input - 1]
        if current.startswith("DONE!!"):
            print('this item is already completed')
        else:
            item.lines.insert(input - 1, "DONE!! " + current)
            item.lines.remove(current)
            Manager.write()

    def clearlist():
        lines = []
