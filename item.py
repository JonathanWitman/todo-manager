import manager


class Item(object):
    def check(input):
        value = manager.lines[input - 1]
        if value.startswith("DONE!!"):
            print("this item is done")
        else:
            print("this item isn't finished quite yet")

    def add():
        print("What are you adding to the list?")
        inp = input("> ")
        a = open("todos.txt","a")
        a.write(f"{len(manager.lines) + 1}. " + inp + " started @ "+ manager.time + "\n")
        a.close()

#{len(manager.lines) + 1}.
