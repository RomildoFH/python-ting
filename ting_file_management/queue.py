from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []
    
    def __str__(self):
        str_queue = ""
        for index in range(0, len(self._data)):
            value = self._data[index]
            str_queue += str(value)
            if index + 1 < len(self._data):
                str_queue += " <- "

        return "FILA: |" + str_queue + "|"

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")

    def is_empty(self):
        return len(self._data) == 0

    def item_exists(self, file_name):
        for item in self._data:
            if item.get("nome_do_arquivo") == file_name:
                return True
        return False
