import manager
import datetime

lines = []
time = str(datetime.datetime.now())

class Item(object):
    def check(input):
        value = lines[input - 1]
        if value.startswith("DONE!!"):
            print("this item is done")
        else:
            print("this item isn't finished quite yet")

    def add():
        print("What are you adding to the list?")
        inp = input("> ")
        manager.Manager.update()
        a = open("todos.txt","a")
        a.write(f"{len(lines) + 1}. " + inp + " started @ "+ time + "\n")
        manager.Manager.update()
        print(lines)
        a.close()
