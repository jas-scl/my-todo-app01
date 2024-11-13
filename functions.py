FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):        # default argument
    """ Read a text file and return a list  # doc-string
        of to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):       # default argument has to be placed last
    """ Write a to-do items into the text file """      # doc-string
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
