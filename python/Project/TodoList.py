# To-Do List App

Choice = {
    "1": "Add a new item","2": "List all items", "3": "Update a item","4": "Delete a item","5": "Quit"
}

def add():
    new = input("Enter a new item: ")
    with open("todo.txt", "a") as f:
        f.write(new + "\n")
    print(f"{new} has been added to the list.")

def list():
    with open("todo.txt", "r") as f:
        todos = f.readlines()
    if todos:
        print("List:")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo.strip()}")
    else:
        print("The list is empty.")

def update():
    with open("todo.txt", "r") as f:
        item=input("enter the item to update:")
        todos = f.read()
    if todos:
         update = input("Enter Item:")
         newContent = todos.replace(item,update)
         print("Update Successfull\nUpdated List:\n")
         print(newContent)
         with open("todo.txt",'w') as file:
            file.write(newContent) 
    else:
        print("Item not Present in list")
    

def delete():
    delete=input("enter the item to delete:")
    with open("todo.txt", "r") as f:
        todos = f.read()
    if todos:
        newContent = todos.replace(delete,'')
        print("Deletion Successfull\nUpdated List:")
        print(newContent.strip())
        with open('todo.txt','w') as file:
            file.write(newContent.strip()) 
    else:
        print("Item not Present in list")

def main():
    
    while True:
        print("\nList of Choice:")
        for option, description in Choice.items():
            print(f"{option}. {description}")
        choice = input("Enter your choice: ")
        if choice == "1":
            add()
        elif choice == "2":
            list()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

        if choice == "5":
            break


main()


