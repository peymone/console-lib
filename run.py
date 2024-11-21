from app import CRUD, CLI

if __name__ == '__main__':

    library_file_path = './app/lib.json'

    # Create CRUD object for work with data
    crud = CRUD(library_file_path)

    # Create CLI object and run commands handler
    cli = CLI(crud_object=crud)
    cli.commands_handler()
