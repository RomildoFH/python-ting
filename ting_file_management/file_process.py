import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    lines = txt_importer(path_file)
    return lines


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


print(process("statics/arquivo_teste.txt", 'xablau'))