from translate import Translator

# Função para dividir o texto em partes menores
def split_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# Função para traduzir o conteúdo do arquivo e escrever a tradução em outro arquivo
def translate_and_save(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        try:
            # Divide o texto em partes menores
            text_chunks = split_text(content)
            # Inicializa o tradutor
            translator = Translator(to_lang="pt")
            translated_content = ""
            # Traduz cada parte do texto e concatena as traduções
            for chunk in text_chunks:
                translated_chunk = translator.translate(chunk)
                translated_content += translated_chunk + "\n"
            # Escreve o conteúdo traduzido em um novo arquivo
            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(translated_content)
            print("Conteúdo traduzido foi salvo em 'pronto.txt'.")
        except Exception as e:
            print(f"Erro ao traduzir: {e}")

# Caminho do arquivo de texto em inglês
file_path = 'talvez.txt'

# Chama a função para traduzir o conteúdo do arquivo 'talvez.txt' e escrever no 'pronto.txt' traduzido
translate_and_save(file_path, 'pronto.txt')
