# Command Line Interface for Todo App
# from functions import get_todos, write_todos
# or import the module - functions: local module (written by us)
# time: global module
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]
        todo = todo.title()
        # filepath is called an argument here, todos.txt is the argument value
        todos = functions.get_todos()
        # get_todos is a function of the functions module

        todos.append(todo + "\n")

        functions.write_todos(todos)
        # write_todos(filepath="todos.txt", todos_arg=todos) -> if you do not follow the order of arguments, specify them

    elif user_action.startswith("show"):

        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        # with context manager, we do not need close the file, so if the program is interrupted for some reasons,
        # the file will not stay open
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            item = f"{index + 1}-{item}"
            print(item)
    elif user_action.startswith("exit"):
        break
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo.title() + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue # runs another cycle of whole loop

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todo_to_remove = todos[number].strip("\n")

            todos = functions.get_todos()

            todos.pop(number)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    else:
        print("Hey, you used an unknown command")

print("Bye!")
'''

user_prompt = "Enter a title: "
title = input(user_prompt)

print("The number of characters in the title is:", len(title))
'''
