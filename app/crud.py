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
                json.dump({'books': []}, file)

    def __get_lib(self, file):
        """Get list of books in library and last book id"""

        # Load data from save file
        library: dict[str, list[dict]] = json.load(file)

        # Get last book id
        if len(library['books']) == 0:
            last_id: int = 0
        else:
            last_id: int = library['books'][-1]['id']

        return library, last_id

    def add(self, title: str, author: str, year: str) -> None:
        """Add new book to library

        Args:
            title (str): book's title
            author (str): book's author
            year (str): book's year
        """

        with open(self.save_file, 'r+') as file:

            # Get library and last id from save file
            library, last_id = self.__get_lib(file)

            # Create book object
            book = {
                'id': last_id + 1,
                'title': title,
                'author': author,
                'year': year,
                'status': "obtain"
            }

            # Append new book to save file
            library['books'].append(book)
            file.seek(0)
            json.dump(library, file, indent=4)

    def remove(self, id: int) -> None:
        """Remove book from library by id

        Args:
            id (int): book's id
        """

        with open(self.save_file, 'r+') as file:

            # Get library and last id from save file
            library, last_id = self.__get_lib(file)

            # Find book index
            for index, book in enumerate(library['books']):
                if book['id'] == id:
                    break

            # Remove book from library by index
            del library['books'][index]

            # Save changes to save file
            file.seek(0)
            json.dump(library, file, indent=4)

    def find(self, title: str = None, author: str = None, year: str = None) -> list[dict]:
        """Get dict of books by title OR author OR year

        Args:
            title (str, optional): book's title. Defaults to None.
            author (str, optional): book's author. Defaults to None.
            year (str, optional): book's year. Defaults to None.

        Returns:
            list (dict): books data
        """

        pass

    def show(self) -> list[dict]:
        """Get dict of all books in library

        Returns:
            list[dict]: books data
        """

        with open(self.save_file, 'r') as file:

            # Get library and last id from save file
            library, last_id = self.__get_lib(file)

            return library['books']

    def status(self, id: int, status: str) -> None:
        """Change status of book by id

        Args:
            id (int): book's id
        """

        with open(self.save_file, 'r') as file:

            # Get library and last id from save file
            library, last_id = self.__get_lib(file)

            # Find book index
            for index, book in enumerate(library['books']):
                if book['id'] == id:
                    break

            # Remove book from library by index
            library['books'][index]['status'] = status

            # Save changes to save file
            file.seek(0)
            json.dump(library, file, indent=4)
