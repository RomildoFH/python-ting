from pytest import raises
from ting_file_management.priority_queue import PriorityQueue

mock_arquivo_prioritario_1 = {
        "nome_do_arquivo": "test_name_1",
        "qtd_linhas": 1,
        "linhas_do_arquivo": ["linha 1"]
        }

mock_arquivo_prioritario_2 = {
        "nome_do_arquivo": "test_name_2",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ["linha 1", "linha 2"]
        }

mock_not_arquivo_prioritario_1 = {
        "nome_do_arquivo": "test_name_3",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "linha 1",
            "linha 2",
            "linha 3",
            "linha 4",
            "linha 5",
            "linha 6"]
        }

mock_not_arquivo_prioritario_2 = {
        "nome_do_arquivo": "test_name_4",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "linha 1",
            "linha 2",
            "linha 3",
            "linha 4",
            "linha 5",
            "linha 6"]
        }


def test_basic_priority_queueing():
    # instanciando PriorityQueue
    myqueue = PriorityQueue()
    # inserindo arquivo na fila de prioridade e validando
    myqueue.enqueue(mock_arquivo_prioritario_1)
    assert len(myqueue) == 1
    assert myqueue.high_priority.get_data() == [mock_arquivo_prioritario_1]
    # inserindo arquivo na fila regular e validando
    myqueue.enqueue(mock_not_arquivo_prioritario_1)
    print(f'aqui é o print: {myqueue.high_priority.get_data()}')
    assert len(myqueue) == 2
    assert myqueue.regular_priority.get_data() == [
        mock_not_arquivo_prioritario_1,
        ]
    # removendo um arquivo da fila, quando há prioridade
    myqueue.dequeue()
    assert len(myqueue) == 1
    assert myqueue.high_priority.get_data() == []
    # removendo um arquivo da fila, quando NÃO há prioridade
    myqueue.dequeue()
    assert len(myqueue) == 0
    assert myqueue.regular_priority.get_data() == []
    # testa busca por indice de uma prioridade
    myqueue.enqueue(mock_arquivo_prioritario_1)
    myqueue.enqueue(mock_not_arquivo_prioritario_1)
    assert myqueue.search(1) == mock_not_arquivo_prioritario_1
    assert myqueue.search(0) == mock_arquivo_prioritario_1
    with raises(IndexError, match="Índice Inválido ou Inexistente"):
        myqueue.search(10)
