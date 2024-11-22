from os.path import exists
import json


class CRUD:
    """Class for library opearations"""

    def __init__(self, save_file_path: str) -> None:
        """Create save file for library in json format

        Args:
            save_file_path (str): safe file path
        """

        self.save_file = save_file_path

        # Create save file if not exist
        if exists(self.save_file):
            pass
        else:
            with open(self.save_file, 'w') as file:
                # create file structure
                json.dump({'books': []}, file)

    def __get_lib(self):
        """Get library and last book id from save file"""

        with open(self.save_file, 'r') as file:

            # Load data from save file
            library: dict[str, list[dict]] = json.load(file)

            # Get last book id
            if len(library['books']) == 0:
                last_id: int = 0
            else:
                last_id: int = library['books'][-1]['id']

            return library, last_id

    def __save_lib(self, library: dict) -> None:
        """Save library to save file"""

        with open(self.save_file, 'w') as file:
            json.dump(library, file, indent=4)

    def show(self) -> list[dict]:
        """Get dict of all books in library

        Returns:
            list[dict]: books data
        """

        # Get library from save file
        library, _ = self.__get_lib()

        return library['books']

    def add(self, title: str, author: str, year: str) -> None:
        """Add new book to library

        Args:
            title (str): book's title
            author (str): book's author
            year (str): book's year
        """

        # Get library and last id from save file
        library, last_id = self.__get_lib()

        # Create book object
        book = {
            'id': last_id + 1,
            'title': title,
            'author': author,
            'year': year,
            'status': "in stock"
        }

        # Add new book to library
        library['books'].append(book)

        # Save changes to save file
        self.__save_lib(library)

    def remove(self, id: int) -> None:
        """Remove book from library by it's id

        Args:
            id (int): book's id (index = id - 1)
        """

        try:  # Handle index error

            # Get library from save file
            library, _ = self.__get_lib()

            # Delete book at given id
            del library['books'][id-1]

            # Change id for books after deleted
            for i in range(id-1, len(library['books'])):
                library['books'][i]['id'] = i + 1

            # Save changes to save file
            self.__save_lib(library)

        except IndexError:
            print("Library have no book with id ", id)

    def find(self, title: str = None, author: str = None, year: str = None) -> list[dict]:
        """Get dict of books by title OR author OR year

        Args:
            title (str, optional): book's title. Defaults to None.
            author (str, optional): book's author. Defaults to None.
            year (str, optional): book's year. Defaults to None.

        Returns:
            list (dict): books data
        """

        # Get library from save file
        library, _ = self.__get_lib()

        # Handle search by specific argument
        books = list()
        if title is not None:
            for book in (library['books']):
                if title == book['title']:
                    books.append(book)
        if author is not None:
            for book in (library['books']):
                if author == book['author']:
                    books.append(book)
        if year is not None:
            for book in (library['books']):
                if year == book['year']:
                    books.append(book)

        return books

    def status(self, id: int) -> None:
        """Change status of book by id

        Args:
            id (int): book's id
        """

        try:  # Handle index error

            # Get library from save file
            library, _ = self.__get_lib()

            # Switch status for book with given id
            status = library['books'][id-1]['status']
            if status == 'in stock':
                library['books'][id-1]['status'] = 'taken'
            else:
                library['books'][id-1]['status'] = 'in stock'

            # Save changes to save file
            self.__save_lib(library)

        except IndexError:
            print("Library have no book with id ", id)
