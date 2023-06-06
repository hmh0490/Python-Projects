FILEPATH = "todos.txt"

# filepath is called a parameter here
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    # create a new file
    """ Write the to-do item list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

# print(__name__)
if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())