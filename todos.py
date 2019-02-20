import manager
import item

#Each class should be in its own module which you will need to import accordingly

#how to store data in the file

#Look up the datetime module

def begin():
    print("What's up?")
    print("type 'help' for help")
    inp = input("> ")

    if inp == "help":
        print(" - 'add' to add an item to your task list\n - 'all' to see what's all on your task list\n - 'check' to see if an item is done or not\n - 'done' to mark an item as complete\n - 'quit' to give me 100 dollars")
        begin()
    elif inp == "add":
        item.Item.add()
        print("Done! you're welcome")
        input('')
        begin()
    elif inp == "all":
        manager.Manager.update()
        manager.Manager.print()
        input('')
        begin()
    elif inp == "done":
        manager.Manager.done()
        begin()
    elif inp == "check":
        item.Item.check()
        begin()
    elif inp == "quit":
        print("Bye my guy \n")
    else:
        print("huh?? I don't know what you're saying. \n")
        begin()

begin()

#**update moves items from txt into list
#Manager.update()

#**done marks an item as complete
#manager.Manager.done(1)

#**print prints all of the items on the list
#Manager.print()

#**write writes the list to the txt file
#Manager.write()

#**clear clears the current txt file oooooooooh
#Manager.clear()

#**add adds an item to the list
#item.Item.add()

#**check checks if an item is done or not
#Item.check(2)
