# import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # print(instance)
    if instance.item_exists(path_file):
        return None
    lines = txt_importer(path_file)
    file_name = path_file
    result = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
        }
    instance.enqueue(result)
    print(result)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# myQueue = Queue()
# myQueue.enqueue({
#         "nome_do_arquivo": "test_name",
#         "qtd_linhas": 2,
#         "linhas_do_arquivo": ["linha 1", "linha 2"]
#         })
# print(myQueue)
# print(process("statics/arquivo_teste.txt", myQueue))
# print(process("statics/arquivo_teste.txt", myQueue))
