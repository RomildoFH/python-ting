import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError("Formato inválido")

        with open(path_file, "r") as file:
            return file.read().split("\n")

    except FileNotFoundError:
        error_message = f"Arquivo {path_file} não encontrado"
        print(error_message, file=sys.stderr)
    except ValueError as e:
        error_message = str(e)
        print(error_message, file=sys.stderr)
