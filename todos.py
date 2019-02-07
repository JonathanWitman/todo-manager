import datetime
#Each class should be in its own module which you will need to import accordingly

#how to store data in the file

#Look up the datetime module

class Item(object):
    pass
    #1$) A timestamp of when they were created.
    #2) A boolean marking the item as completed or not.
    #3$) And the text of the actual to-do item.
    def add(input):
        a = open("todos.txt","a")
        a.write(f"{length}. " + input + " started @ "+ time + "\n")
        a.close()

class Manager(object):

    def print():
        for i in range(0,len(lines)):
            print(lines[i])

    def update():
        a = open("todos.txt", "rt")
        for line in a:
            lines.append(line)

    def done():
        pass
    #1) Print all of the to-do items in the list.
    #2) Add a new item to the list.
    #3) Mark an item as completed.

lines = []

time = str(datetime.datetime.now())
length = len(lines)

Item.add('yo dude')
Manager.update()
#Manager.print()

#print(lines[1])
