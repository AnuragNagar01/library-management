
# sum = 0
#
# while True:
#     userInput = input("Enter The price of The Item: \n")
#     if (userInput!='q'):
#         sum = sum + int(userInput)
#         print(f"Your Item Total Price : {sum}\n")
#     else:
#         print(f"Total Price Of Your Item : {sum}. Thanks For Shopping With Us")
#         break

class Library():
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Availabe Books in Our Library :{self.name}")
        for books in self.booklist:
            print(books)

    def LendBook(self, user, book):
        if book not in self.lendDict.keys():
            if book not in self.booklist:
                print("Book is not Available in the Library, Please Try Another Book!")
            else:
                print("Lending-Book is Return by Lender. You Can Take The Book Now")
                self.lendDict.update({book:user})
                print(self.lendDict)
        else:
            print(f"Book is Already Being Used by {self.lendDict[book]}")

    def addBook(self, user, book):
        if user == "AnuragNagar":
            self.booklist.append(book)
            print(f"Book has been added to the Booklist : ", book)
        else:
            print("You are not Authorized to Add this Book.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.update({})
            print("Thanks for Returning our Book, Please visit again.")
        else:
            print(f"Sorry we are not found any -[ {book} ] Book.")

if __name__ == '__main__':
    PeaceLibrary = Library(["Rich Dad Poor Dad",
                            "7 Habits of Highly Effective People",
                            "The Courage to Create",
                            "The Power Of Now",
                            "The Power Of Positive Thinking",
                            "The Defining Decades",
                            "Complete Work of Swami Vivekananda",
                            "The Power Of Subconcious Mind",
                            "7 Law Of Human Nature"], "PeaceLibrary\n")

    while True:
        print("Welcome to the PeaceLibrary. Enter your choice to Continue:")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")

        user_choise = input("Enter : ")

        print(f"Your Choice is : {user_choise}")

        if user_choise == "1":
            Library.displayBooks(PeaceLibrary)

        elif user_choise == "2":
            book = input("Enter the Book you want to lend : ")
            user = input("Enter Your Name : ")
            PeaceLibrary.LendBook(user, book)

        elif user_choise == "3":
            user = input("Please Enter Username : ")
            book = input("Enter the Book you want to Add : \n")
            PeaceLibrary.addBook(user,book)
            display = Library.displayBooks(PeaceLibrary)

        elif user_choise == "4":
            book = input("Enter the name of the Book you want to return : ")
            PeaceLibrary.returnBook(book)

        else:
            print("Please Enter a Valid Option\n")
            break




        print("Press 'q' to quit and 'c' to continue")
        user_choise2 = input()
        if user_choise2 == "q":
            print("Thanks For Visit!")
            exit()
        elif user_choise2 == "c":
            continue
