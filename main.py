from file_manager import FileManager

manager = FileManager()

while True:

    print("\n============================")
    print("      FILE MANAGER")
    print("============================")
    print("1. List Files")
    print("2. Create File")
    print("3. Delete File")
    print("4. Rename File")
    print("5. Copy File")
    print("6. Move File")
    print("7. Create Folder")
    print("8. Delete Folder")
    print("9. Search File")
    print("10. File Information")
    print("11. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        manager.directory.list_contents()

    elif choice == "2":
        name = input("Filename: ")
        manager.file.create(name)

    elif choice == "3":
        name = input("Filename: ")
        manager.file.delete(name)

    elif choice == "4":
        old = input("Old name: ")
        new = input("New name: ")
        manager.file.rename(old, new)

    elif choice == "5":
        source = input("Source: ")
        destination = input("Destination: ")
        manager.file.copy(source, destination)

    elif choice == "6":
        source = input("Source: ")
        destination = input("Destination: ")
        manager.file.move(source, destination)

    elif choice == "7":
        folder = input("Folder name: ")
        manager.directory.create(folder)

    elif choice == "8":
        folder = input("Folder name: ")
        manager.directory.delete(folder)

    elif choice == "9":
        filename = input("Filename: ")
        manager.search.search(filename)

    elif choice == "10":
        filename = input("Filename: ")
        manager.info.display(filename)

    elif choice == "11":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")