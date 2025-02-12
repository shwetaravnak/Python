#librarymanagement

availablebooks = ["Python", "DSA", "COA", "C++", "Java"]
borrowedbooks = []
print("LIBRARY MANAGEMENT SYSTEM")

while (True):
    print("""Menu:
             1.Available books
             2.Borrow a book
             3.Return a book
             4.Exit""")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(f"Available books are:{availablebooks}")
            
    elif choice == 2:
        borrow_book = str(input("Enter the book you want to borrow:"))
        if borrow_book in availablebooks:
            availablebooks.remove(borrow_book)
            borrowedbooks.append(borrow_book)
            print(f"You have borrowed {borrow_book}")
        else:
            print(f"Sorry, {borrow_book} is not available")

    elif choice == 3:
        returnbook = str(input("Enter the book you want to return:"))
        if returnbook in borrowedbooks:
            availablebooks.append(returnbook)
            borrowedbooks.remove(returnbook)
            print(f"You have successfully returned {returnbook}!")
        else:
            print(f"Sorry, you didn't borrow {returnbook}.")

    elif choice == 4:
        print("Exiting...")
        break;
                    
    else:
        print("Wrong choice")
