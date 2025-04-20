# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jiayi Zhu
# jzhu42@uci.edu
# 94623196

import command_parser
import notebook
from pathlib import Path

def create_notebook(path, diary_name):
    path = Path(path) / f"{diary_name}.json"

    username = input()
    password = input()
    bio = input()
    new_notebook = notebook.Notebook(username, password, bio)
    
    if path.exists() or not path.parent.exists():
        print('ERROR')
        return None, None
    
    else:
        new_notebook.save(path)
        print(f'{path.resolve()} CREATED')
        return new_notebook, path

def delete_notebook(path):
    path = Path(path)
    if not path.exists() or path.suffix != '.json':
        print('ERROR')
    else:
        path.unlink()
        print(f"{path.resolve()} DELETED")
        
def load_notebook(path):
    path = Path(path)
    if path.exists() and path.suffix == '.json':
        username = input()
        password = input()
        loaded_notebook = notebook.Notebook("","","")
        loaded_notebook.load(path)
        if loaded_notebook.username == username and loaded_notebook.password == password:
            print("Notebook loaded.")
            print(loaded_notebook.username)
            print(loaded_notebook.bio)
            return loaded_notebook, path
        else:
            print("ERROR")
            return None, None
    else:
        print("ERROR")
        return None, None

def edit_notebook(notebook_obj, notebook_path, option_lst):
    for i in range(len(option_lst)):
        
        if i % 2 == 0:
            if i + 1 >= len(option_lst) or option_lst[i + 1].startswith('-'):
                print("ERROR")
                return
            
            option = option_lst[i]
            content = option_lst[i + 1]

            if option == '-usr':
                notebook_obj.username = content
                notebook_obj.save(notebook_path)

            elif option == '-pwd':
                notebook_obj.password = content
                notebook_obj.save(notebook_path)

            elif option == '-bio':
                notebook_obj.bio = content
                notebook_obj.save(notebook_path)

            elif option == '-add':
                diary = notebook.Diary(content)
                notebook_obj.add_diary(diary)
                notebook_obj.save(notebook_path)

            elif option == '-del':
                try:
                    index = int(content)
                    success = notebook_obj.del_diary(index)
                    if not success:
                        print("ERROR")
                        return
                    notebook_obj.save(notebook_path)

                except:
                    print("ERROR")
                    return
                
            else:
                print("ERROR")
                return

def print_notebook(notebook_obj, notebook_path, option_lst):
    i = 0
    while i < len(option_lst):
        option = option_lst[i]
        if option == '-usr':
            print(notebook_obj.username)
            i += 1

        elif option == '-pwd':
            print(notebook_obj.password)
            i += 1

        elif option == '-bio':
            print(notebook_obj.bio)
            i += 1

        elif option == '-diaries':
            diaries = notebook_obj.get_diaries()
            for j, diary in enumerate(diaries):
                print(f'{j}: {diary.get_entry()}')
            i += 1

        elif option == '-diary':
            try:
                index = int(option_lst[i + 1])
                diaries = notebook_obj.get_diaries()
                print(diaries[index].get_entry())
                i += 2

            except:
                print("ERROR")
                return     

        elif option == '-all':
            print(notebook_obj.username)
            print(notebook_obj.password)
            print(notebook_obj.bio)
            diaries = notebook_obj.get_diaries()
            for j, diary in enumerate(diaries):
                print(f'{j}: {diary.get_entry()}')
            i += 1

        else:
            print('ERROR')
            return          

            
if __name__=="__main__":
    notebook_obj = None
    notebook_path = None

    while True:
        command_lst = command_parser.user_input()

        if not command_lst:
            continue
        
        command = command_lst[0]

        if command == 'Q':
            break

        if command == 'C':
            if len(command_lst) != 4 or command_lst[2] != '-n':
                print("ERROR")
            else:
                path = command_lst[1]
                diary_name = command_lst[3]
                notebook_obj, notebook_path = create_notebook(path, diary_name)

        elif command == 'D':
            if len(command_lst) != 2:
                print("ERROR")
            else:
                delete_notebook(command_lst[1])

        elif command == 'O':
            if len(command_lst) != 2:
                print("ERROR")
            else:
                notebook_obj, notebook_path = load_notebook(command_lst[1])
        
        elif command == 'E':
            if len(command_lst) < 3:
                print("ERROR")
            elif notebook_obj == None or notebook_path == None:
                print('ERROR')
            else:
                option_lst = command_lst[1:]
                edit_notebook(notebook_obj, notebook_path, option_lst)
                
        elif command == 'P':
            if len(command_lst) < 2:
                print("ERROR")
            elif notebook_obj == None or notebook_path == None:
                print('ERROR')
            else:
                option_lst = command_lst[1:]
                print_notebook(notebook_obj, notebook_path, option_lst)
        else:
            print("ERROR")
