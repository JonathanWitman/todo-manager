import manager

class Item(object):
    def check(input):
        value = manager.Var.lines[input - 1]
        if value.startswith("DONE!!"):
            print("this item is done")
        else:
            print("this item isn't finished quite yet")

    def add():
        print("What are you adding to the list?")
        inp = input("> ")
        a = open("todos.txt","a")
        print(manager.Var.lines)
        a.write(f"{len(manager.Var.lines) + 1}. " + inp + " started @ "+ manager.Var.time + "\n")
        a.close()
