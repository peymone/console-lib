from app import CRUD


class CLI:
    def __init__(self, crud_object: CRUD) -> None:
        self.crud = crud_object
        self.commands_description = {
            "add [title] [author] [year]": "add book to library with specific title, author and year",
            "del [id]": "delete book from library by id",
            "find -a [author]": "find books by author",
            "find -t [title]": "find books by title",
            "find -y [year]": "find books by year",
            "show": "show all books in library",
            "status [id] [new_status]": "change book status"
        }

        # Show commands description on start
        print("Available commands:\n")
        for command, description in self.commands_description.items():
            print(f"{command}: {description}")

        print('\nEnter Ctrl + C to exit\n')

    def commands_handler(self):
        """Input command and call specific CRUD function
        """

        try:  # Handle keyboard interrupt

            while True:

                command = input("Enter command: ")

                # Parse input
                cmd: str = command.split()[0]
                args: list[str] = command.split()[1:]

                # Handle commands
                match cmd:
                    case 'add':
                        if len(args) < 3:
                            print("add method must contain following arguments: [title], [author], [year]")
                        else:
                            self.crud.add(title=args[0], author=args[1], year=args[2])
                    case 'del':
                        try:
                            if args[0].isdigit():
                                self.crud.remove(id=int(args[0]))
                        except IndexError:
                            print("del method must contain [id] argument")
                    case 'find':
                        pass
                    case 'show':
                        books = self.crud.show()
                        for book in books:
                            print(book)
                    case 'status':
                        try:
                            if args[0].isdigit():
                                self.crud.status(id=int(args[0]), status=args[1])
                        except IndexError:
                            print("status method must contain [id] [new_status] arguments")

        except KeyboardInterrupt:
            pass
