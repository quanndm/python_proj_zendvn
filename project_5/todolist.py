from enum import Enum
import os
Status = Enum('Status', ['DOING', 'FINISHED'])

class TodoItem:
    id: int
    task: str
    status: type[Status]

    def __init__(self, id: int, task: str):
        self.id = id
        self.task = task
        self.status = Status.DOING

def print_menu():
    print('Menu:')
    print('1. Add item')
    print('2. Mark as done')
    print('3. View list')
    print('4. Delete item')
    print('5. Exit')
    print('6. Clear Console')

def add_todo(todos: list[TodoItem]):
    task = input('Enter task: ')

    id = len(todos) + 1
    todo = TodoItem(id, task)
    todos.append(todo)

    print(f'Task \"{task}\" added.')
    

def show_todos(todos: list[TodoItem]):
    print('================Todo list================')
    for todo in todos:
        print(f'{todo.id} - {todo.task} - {todo.status.name}')
    print('================Todo list================')

def mark_as_done(todos: list[TodoItem]):
    id = int(input('Enter task id: '))
    todo = next((todo for todo in todos if todo.id == id), None)
    if todo is None:
        print(f'Task with id {id} not found.')
        return
    todo.status = Status.FINISHED

    print(f'Task \"{todo.task}\" marked as done.')

def delete_todo(todos: list[TodoItem]):
    id = int(input('Enter task id: '))
    todo = next((todo for todo in todos if todo.id == id), None)
    if todo is None:
        print(f'Task with id {id} not found.')
        return
    print(f'Task \"{todo.task}\" deleted.')
    todos.remove(todo)
    

def main():
    todos: list[TodoItem] = []
    

    while True:
        print_menu()
        choice = int(input('Enter your choice: '))
        match choice:
            case 1:
                add_todo(todos)
            case 2:
                mark_as_done(todos)
            case 3:
                show_todos(todos)
            case 4:
                delete_todo(todos)
            case 5:
                print('Bye!')
                break
            case 6:
                os.system('cls')
            case _:
                print('Invalid choice')



if __name__ == '__main__':
    main()