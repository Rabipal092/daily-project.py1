def create_file(filename):
    with open(filename, 'w') as file:
        file.write('')  # Create an empty file

def view_all_files():
    import os
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            print(filename)

def delete_file(filename):
    import os
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f'The file {filename} does not exist')

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'The file {filename} does not exist')

def edit_file(filename):
    try:
        with open(filename, 'a') as file:
            content = input('Enter content to add: ')
            file.write(content + '\n')
    except FileNotFoundError:
        print(f'The file {filename} does not exist')

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: Create file')
        print('2: View all files')
        print('3: Delete file')
        print('4: Read file')
        print('5: Edit file')
        print('6: Exit')

        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            filename = input('Enter the file name to create: ')
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input('Enter the name of the file you want to delete: ')
            delete_file(filename)

        elif choice == '4':
            filename = input('Enter the file name to read: ')
            read_file(filename)

        elif choice == '5':
            filename = input('Enter the file name to edit: ')
            edit_file(filename)

        elif choice == '6':
            print('Closing the app...')
            break

        else:
            print('Invalid choice, please try again.')

if __name__ == "__main__":
    main()

