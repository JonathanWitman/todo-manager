#Each class should be in its own module which you will need to import accordingly

#how to store data in the file

#Look up the datetime module

class Item(object):
    pass
    #1) A timestamp of when they were created.
    #2) A boolean marking the item as completed or not.
    #3) And the text of the actual to-do item.

class Manager(object):

    def print():
        pass

    def add(input):
        a = open("todos.txt","a")
        a.write(input + "\n")
        a.close()

    def done():
        pass
    #1) Print all of the to-do items in the list.
    #2) Add a new item to the list.
    #3) Mark an item as completed.

lines = []

def yo():
    in_file = open("todos.txt", "rt")
    for line in in_file:
        lines.append(line)
yo()
print(lines)

#lines = []

#Manager.add('zero')
#print(lines[1])
