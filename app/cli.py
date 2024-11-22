from app import CRUD


class CLI:
    """Command line interface for library"""

    def __init__(self, crud_object: CRUD) -> None:
        self.crud = crud_object
        self.commands_description = {
            "help": "show all available commands",
            "show": "show all books in library",
            "add [title] [author] [year]": "add book to library",
            "remove [id]": "remove book from library by it's id",
            "find -a [author]": "find books by author",
            "find -t [title]": "find books by title",
            "find -y [year]": "find books by year",
            "status [id]": "switch book status ('in stock' or 'taken')"
        }

        self.show_commands()
        print('\nEnter Ctrl + C to exit\n')

    def show_commands(self) -> None:
        """Show all available commands"""

        print("\nAvailable commands:\n")
        for command, description in self.commands_description.items():
            print(f"{command}: {description}")

    def commands_handler(self):
        """Input command and call specific CRUD function"""

        try:  # Handle keyboard interruption
            while True:
                command = input("Enter command: ")

                # Parse input
                cmd: str = command.split()[0]
                args: list[str] = command.split()[1:]

                # Handle commands and call CRUD functions
                match cmd:

                    case 'help':
                        self.show_commands()
                        print('\n')

                    case 'show':
                        books: list[dict] = self.crud.show()

                        print("Books currently in library: ", len(books), '\n')
                        for book in books:
                            print(
                                f"ID: {book['id']}, title: {book['title']}, author: {book['author']}, year: {book['author']}, status: {book['status']}")
                        print('\n')

                    case 'add':
                        # Check if arguments was entered and call crud function
                        if len(args) < 3:
                            print("add command must contain 3 arguments: title, author, year")
                        else:
                            self.crud.add(title=args[0], author=args[1], year=args[2])

                    case 'remove':
                        # Check if book's id was entered
                        if (args) < 1:
                            print("remove command must contain 1 argument: book's id")
                        else:
                            # Check if book's id is number and call crud function
                            if args[0].isdigit():
                                self.crud.remove(id=int(args[0]))
                            else:
                                print("book's id has to be a number: 1, 2, etc..")

                    case 'find':
                        # Check if arguments was entered
                        if len(args) < 2:
                            print("find command must contain 2 arguments: mode (-a, -t, -y) and data (author, year or title)")
                        else:  # Find and get books by filter and call crud function
                            if args[0] == '-a':
                                books = self.crud.find(author=args[1])
                            if args[0] == '-t':
                                books = self.crud.find(title=args[1])
                            if args[0] == '-y':
                                books = self.crud.find(year=args[1])

                            # Show finded books
                            print(len(books), "books was founded:\n")
                            for book in books:
                                print(
                                    f"ID: {book['id']}, title: {book['title']}, author: {book['author']}, year: {book['author']}, status: {book['status']}")
                            print('\n')

                    case 'status':
                        # Check if book's id was entered
                        if len(args) < 1:
                            print("remove command must contain 1 argument: book's id")
                        else:
                            # Check if book's id is number and call crud function
                            if args[0].isdigit():
                                self.crud.status(id=int(args[0]))
                            else:
                                print("book's id has to be a number: 1, 2, etc..")

                    case _:
                        print(f"'{cmd}' command not regognized. Check the list of available by enter: help")

        except KeyboardInterrupt:
            pass
