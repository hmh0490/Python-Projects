import functions
import PySimpleGUI as sg
import time
import os

# if program needs to run on any computer, make sure to generate a todo.txt
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
# add_button = sg.Button("Add", size=10) # height is by default = 1
add_button = sg.Button("Add", size=2, image_source="add.png",
                       mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
# png should be in the same folder as the code
# mouseover_color -> so the button does not disappear when we hover over our mouse
# experiment with different colors, it does not work with all colors
# if tooltip is added, also use key, otherwise event will be = tooltip
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
# complete_button = sg.Button("Complete", size=[5,2], image_source="complete.png", mouseover_colors="LightBlue2",
#                      tooltip="Complete", key="Complete")
exit_button = sg.Button("Exit")

# layout argument has to have widgets inside, eg. label = sg.Text
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
# displays a window
while True:
    event, values = window.read(
        timeout=200)  # exact time is updated every millisec.
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, event) # the event is pushing the "Add" button - print(event) = "Add"
    # print(2, values) # the value is the value we entered
    # print(3, values["todos"])
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos"].update(
            values=todos)  # update listbox on the spot with the new todo
    elif event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(
                values=todos)  # update listbox on the spot with the new todo
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))
    elif event == "Complete":
        try:
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))
    elif event == "Exit":
        break
    elif event == "todos":
        window["todo"].update(value=values["todos"][
            0])  # the item selected in the listbox appears in the inputbox
    elif event == sg.WINDOW_CLOSED:
        break

window.close()

"""
# For more structured layouts, we can use sg.Column to create column instances

import PySimpleGUI as sg

# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1')],
                       [sg.Text('Left 2')]]

# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Text('Right 2')]]

# Construct the Column widgets
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

# Construct the layout
layout = [[left_column, right_column]]

# Construct and display the window
window = sg.Window('Columns', layout)
window.read()
window.close()

# For multiple columns 

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [extract_button]])

# For multiple choice, we can use sg.Radio
import PySimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                           [option2],
                           [option3],
                           [option4]])

window.read()
window.close()
"""