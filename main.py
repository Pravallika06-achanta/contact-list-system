contacts = []

while True:

    file = open("contacts.txt", "a")
    file.close()

    file = open("contacts.txt", "r")
    count = len(file.readlines())
    file.close()

    print(f"\nTotal Contacts: {count}")
    print("===== Contact List Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Delete All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Contact Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        if name == "" or phone == "":
            print("Name and Phone cannot be empty.")
            continue

        duplicate = False

        file = open("contacts.txt", "r")

        for line in file:
            contact = line.strip().split(",")

            if contact[0].lower() == name.lower():
                duplicate = True
                break

        file.close()

        if duplicate:
            print("Contact already exists!")
            continue

        contacts.append([name, phone])

        file = open("contacts.txt", "a")
        file.write(name + "," + phone + "\n")
        file.close()

        print(name, "has been saved successfully!")

    elif choice == "2":

        file = open("contacts.txt", "r")
        lines = file.readlines()
        file.close()

        if lines == []:
            print("No contacts found.")
        else:
            for line in lines:
                contact = line.strip().split(",")

                print("Name :", contact[0])
                print("Phone:", contact[1])
                print()

    elif choice == "3":

        search = input("Enter Contact Name: ").strip()

        file = open("contacts.txt", "r")

        found = False

        for line in file:
            contact = line.strip().split(",")

            if contact[0].lower() == search.lower():
                print("Name :", contact[0])
                print("Phone:", contact[1])
                print()
                found = True

        file.close()

        if not found:
            print("Contact not found.")

    elif choice == "4":

        delete_name = input("Enter Contact Name to Delete: ").strip()

        file = open("contacts.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("contacts.txt", "w")

        found = False

        for line in lines:
            contact = line.strip().split(",")

            if contact[0].lower() != delete_name.lower():
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":

        confirm = input("Are you sure? (yes/no): ").strip()

        if confirm.lower() == "yes":
            file = open("contacts.txt", "w")
            file.close()

            contacts = []

            print("All contacts deleted successfully!")
        else:
            print("Cancelled.")

    elif choice == "6":
        print("Thank You! Goodbye!")
        break

    else:
        print("Invalid Choice")