# Projeto Ting

Projeto desenvolvido como parte do curso Trybe, que visa implementar funcionalidades relacionadas a pesquisa de palavras em textos e gerenciamento de arquivos.

## Módulo ting_file_management
Este módulo lida com o gerenciamento de arquivos no projeto.

### Arquivos:
file_reader.py - Este arquivo contém funções para ler arquivos de texto.

file_writer.py - Aqui você encontrará funções para escrever em arquivos de texto.

file_manager.py - Este arquivo fornece uma classe que encapsula o gerenciamento de arquivos, incluindo operações de leitura e escrita.

### Uso:
```
# Exemplo de uso da classe FileManager
from ting_file_management.file_manager import FileManager


file_manager = FileManager()
conteudo = file_manager.read_file("arquivo.txt")
file_manager.write_file("novo_arquivo.txt", conteudo)
```

## Módulo ting_word_searches
Este módulo trata de operações relacionadas à busca de palavras no projeto.

### Arquivos:
word_search.py - Contém uma classe que implementa algoritmos para buscar palavras em textos.

search_utils.py - Fornece funções utilitárias que auxiliam na busca de palavras.

### Uso:
```
# Exemplo de uso da classe WordSearch
from ting_word_searches.word_search import WordSearch

search = WordSearch()
resultado = search.search_word("texto de exemplo", "exemplo")
print(resultado)  # Saída: True
Módulo priority_queue
Este módulo implementa uma fila de prioridade.
```

### Arquivos:
priority_queue.py - Contém uma implementação de fila de prioridade que pode ser usada para organizar elementos com base em sua prioridade.

priority_queue_utils.py - Fornece funções auxiliares relacionadas à fila de prioridade, como inserção, remoção e obtenção de elementos prioritários.

### Uso:
```
# Exemplo de uso da fila de prioridade
from priority_queue.priority_queue import PriorityQueue

queue = PriorityQueue()
queue.enqueue("item1", 3)
queue.enqueue("item2", 1)
item = queue.dequeue()
print(item)  # Saída: "item2"
```

## Instalação

1. Clone o repositório <br>
```
git clone git@github.com:RomildoFH/python-ting.git<br>
```
2. Entre na pasta do repositório que você acabou de clonar:<br>
```
cd python-ting<br>
```
3. Crie o ambiente virtual para o projeto<br>
```
python3 -m venv .venv && source .venv/bin/activate<br>
```
4. Instale as dependências<br>
```
python3 -m pip install -r dev-requirements.txt
```