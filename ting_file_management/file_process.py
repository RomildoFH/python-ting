import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # print(instance)
    if instance.item_exists(path_file):
        print("arquivo já existente")
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
    if not instance.is_empty():
        item = instance.search(0)
        instance.dequeue()
        path_file = item.get("nome_do_arquivo")
        print(f"Arquivo {path_file} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        print(item)
    except IndexError:
        error_message = "Posição inválida"
        print(error_message, file=sys.stderr)


# myQueue = Queue()
# myQueue.enqueue({
#         "nome_do_arquivo": "test_name",
#         "qtd_linhas": 2,
#         "linhas_do_arquivo": ["linha 1", "linha 2"]
#         })
# process("statics/arquivo_teste.txt", myQueue)
# process("statics/arquivo_teste.txt", myQueue)
# myQueue.enqueue({
#         "nome_do_arquivo": "test_name_2",
#         "qtd_linhas": 3,
#         "linhas_do_arquivo": ["linha 1", "linha 2", "linha 3"]
#         })
# print(f"imprimindo fila: {myQueue}")
# remove(myQueue)
# remove(myQueue)
# remove(myQueue)
# remove(myQueue)
# file_metadata(myQueue, 2)

