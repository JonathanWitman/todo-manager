import datetime
#Each class should be in its own module which you will need to import accordingly

#how to store data in the file

#Look up the datetime module


#lines = ['1','2','3']
lines = []
time = str(datetime.datetime.now())

class Manager(object):

    def print():
        for i in range(0,len(lines)):
            print(lines[i])

    def clear():
        open('todos.txt', 'w').close()


    def update():
        a = open("todos.txt", "rt")
        for line in a:
            lines.append(line)

    def write():
        Manager.clear()
        a = open("todos.txt", "w")
        for item in lines:
            a.write(item)


    def done(input):
        current = lines[input - 1]
        lines.insert(input - 1, "DONE!! " + current)
        lines.remove(current)
        Manager.write()

    #1$) Print all of the to-do items in the list.
    #2$) Add a new item to the list.
    #3) Mark an item as completed.

class Item(object):
    pass
    #1$) A timestamp of when they were created.
    #2) A boolean marking the item as completed or not.
    #3$) And the text of the actual to-do item.
    def add(input):
        a = open("todos.txt","a")
        a.write(f"{len(lines) + 1}. [ ] " + input + " started @ "+ time + "\n")
        a.close()

Manager.update()
Manager.done(1)
Manager.print()
#Manager.write()
#Manager.clear()
#Item.add('yo dude')
