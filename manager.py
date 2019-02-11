import item

class Manager(object):

    def print():
        Manager.update()
        for i in range(0,len(item.lines)):
            print(item.lines[i])

    def clear():
        open('todos.txt', 'w').close()

    def update():
        item.lines = []
        a = open("todos.txt", "rt")
        for line in a:
            item.lines.append(line)
        a.close()

    def write():
        Manager.clear()
        a = open("todos.txt", "w")
        for item in item.lines:
            a.write(item)

    def done():
        print("Which item do you want to mark completed? Please use the numerical value to select an item.")
        Manager.print()
        inp = int(input("> "))
        current = item.lines[inp - 1]
        if current.startswith("DONE!!"):
            print('this item is already completed')
        else:
            item.lines.insert(inp - 1, "DONE!! " + current)
            item.lines.remove(current)
            Manager.write()
