import json
import unittest
from os import remove

from app import CRUD


class TestCRUD(unittest.TestCase):
    def setUp(self) -> None:
        # Create CRUD object with test file path
        self.test_file_path = './tests/lib.json'
        self.crud = CRUD(self.test_file_path)

    def tearDown(self) -> None:
        # remove test save file
        remove(self.test_file_path)

    def __add_books(self) -> list[dict]:
        """Add five books to test save file and return filled books list"""

        # Add 5 books to save file
        test_books_list = list()
        for i in range(1, 6):
            str_i = str(i)

            # Create book object for test list
            book = {
                'id': i,
                'title': 'title' + str_i,
                'author': 'author' + str_i,
                'year': 'year' + str_i,
                'status': "in stock"
            }

            # Fill test list
            test_books_list.append(book)

            # Fill test save file through crud function
            self.crud.add('title' + str_i, 'author' + str_i, 'year' + str_i)

        return test_books_list

    def __get_books(self) -> list[dict]:
        """Read and return books in test save file"""

        with open(self.test_file_path, 'r') as file:
            library = json.load(file)
            return library['books']

    def test_show(self):
        # Fill save file with 5 books and get local books list
        test_books_list = self.__add_books()

        # Compare books list in save file with local books list
        self.assertEqual(self.crud.show(), test_books_list)

    def test_add(self):
        # Fill save file with 5 books and get local books list
        test_books_list = self.__add_books()

        # Compare books list in save file with local books list
        library = self.__get_books()
        self.assertEqual(library, test_books_list)

    def test_remove(self):
        # Fill save file with 5 books and get local books list
        local_books_list = self.__add_books()
        test_id = 1

        # Remove book by test id in local books list
        del local_books_list[test_id-1]
        # Change id for books after deleted
        for i in range(test_id-1, len(local_books_list)):
            local_books_list[i]['id'] = i + 1

        # Remove book by test id in save file
        self.crud.remove(id=test_id)

        # Compare books in save file with local books list
        library = self.__get_books()
        self.assertEqual(library, local_books_list)

    def test_remove_index_error(self):
        # Fill save file with 5 books and get local books list
        _ = self.__add_books()

        # Save file contain only five books
        for i in [0, 6, 10]:
            self.assertIsNone(self.crud.remove(id=i))

    def test_find(self):
        # Fill save file with 5 books and get local books list
        local_books_list = self.__add_books()

        self.assertEquals(self.crud.find(year='year1'), [local_books_list[0],])
        self.assertEquals(self.crud.find(title='title2'),  [local_books_list[1],])
        self.assertEquals(self.crud.find(author='author5'), [local_books_list[4],])

    def test_status(self):
        # Fill save file with 5 books and get local books list
        local_books_list = self.__add_books()
        save_books_list = self.__get_books()

        self.assertEqual(local_books_list[0]['status'], save_books_list[0]['status'])

        self.crud.status(id=1)
        save_books_list = self.__get_books()

        self.assertNotEqual(local_books_list[0]['status'], save_books_list[0]['status'])


if __name__ == '__main__':
    unittest.main()
