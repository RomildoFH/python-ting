def exists_word(word, instance):
    new_list = []

    for archive in instance.get_data():
        path_name = archive.get("nome_do_arquivo")
        archive_lines = archive.get("linhas_do_arquivo")
        ocorrencias = []

        for number, line in enumerate(archive_lines, start=1):
            if word.lower() in line.lower():
                current = {
                    "linha": number
                }
                ocorrencias.append(current)
        new_list.append({
            "palavra": word,
            "arquivo": path_name,
            "ocorrencias": ocorrencias
        })
    return (new_list)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
