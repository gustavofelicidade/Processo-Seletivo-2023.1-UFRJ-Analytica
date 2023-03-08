import os
import csv
import pandas as pd
import logging
import time
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Análise do consumo de Energia elétrica no Munícipio do Rio de Janeiro

# Processo Seletivo UFRJ Analytica

# Gustavo Felicidade da Costa
# BCMT DRE 118171109

#======================================
#  Origem dos dados:
#
#  Datario.com
#
#  Tabela
#
#  Tabela
#
#  Tabela
#
#  Tabela
#
#  Tabela
#
#======================================


# Introdução


# Método


# Conclusão


# Convert XLS to CSV
def convert_files_to_csv(input_folder_path, output_file_path):
    logger.info('Starting convert_files_to_csv function')

    # cria a pasta de saída se ela não existir
    if not os.path.exists(output_file_path):
        os.mkdir(output_file_path)

    # Obtém uma lista de todos os arquivos na pasta de entrada
    files = os.listdir(input_folder_path)

    # Loop através de cada arquivo
    for file_name in files:
        file_path = os.path.join(input_folder_path, file_name)
        # Verifica se o arquivo é um arquivo Excel (.xls)
        if os.path.isfile(file_path) and file_name.endswith(".xls"):
            logger.info(f'Converting Excel file {file_name} to text file')
            xls_to_txt(input_folder_path)   # converte o arquivo Excel em arquivo de texto
            file_name = os.path.splitext(file_name)[0] + '.txt'  # atualiza o nome do arquivo para usar o arquivo de texto convertido
            file_path = os.path.join(input_folder_path, file_name)   # atualiza o caminho do arquivo para usar o arquivo de texto convertido
    # Verifica se o arquivo é um arquivo de texto
    if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith(".txt"):
        logger.info(f'Processando o arquivo {nome_arquivo}')
        # cria um novo arquivo CSV com o mesmo nome do arquivo TXT
        # Check if the file is a text file
        if os.path.isfile(file_path) and file_name.endswith(".txt"):
            logger.info(f'Processing file {file_name}')
            # create a new CSV file with the same name as the TXT file
            csv_path = os.path.join(output_file_path, os.path.splitext(file_name)[0] + '.csv')
            with open(csv_path, 'w', newline='', encoding='utf-8') as output_file:
                csv_writer = csv.writer(output_file)
                with open(file_path, 'r', encoding='utf-8') as input_file:
                    for line in input_file:
                        # Remove caracteres de espaço em branco no final da linha, incluindo o caractere de nova linha
                        line = line.rstrip()
                        # Escreve a linha em uma nova linha no arquivo CSV
                        csv_writer.writerow([line])
    logger.info('Finished convert_files_to_csv function')


# Convert CSV to TXT
def xls_to_txt(folder_path):
    """
    Transforma cada arquivo .xls em um arquivo .txt na pasta especificada.

    Argumentos:
    folder_path -- caminho para a pasta onde os arquivos estão localizados

    Retorna:
    Nada.
    """
    logger.info('Starting xls_to_txt function')
    # Loop pelos arquivos na pasta
    for filename in os.listdir(folder_path):
        # Verifica se o arquivo é um .xls
        if filename.endswith('.xls'):
            # Carrega o arquivo com o Pandas
            filepath = os.path.join(folder_path, filename)
            df = pd.read_excel(filepath)
            # Cria um novo caminho com a extensão .txt
            txt_path = os.path.splitext(filepath)[0] + '.txt'
            # Escreve o arquivo .txt
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(df.to_string(index=False))
            # Remove o arquivo .xls original
            os.remove(filepath)
    logger.info('Finished xls_to_txt function')


# Convert TXT to dict
def each_txt_line_to_dict(folder_path):
    """
    Reads each line of a .txt file in the specified folder and converts them to a dictionary with the first
    word of each line as the key and the rest of the words as values. Returns a list of dictionaries, one for
    each file processed.

    Arguments:
    folder_path -- path to the folder where the .txt files are located

    Returns:
    A list of dictionaries, one for each file processed.
    """
    logger.info('Starting each_txt_line_to_dict function')
    dict_list = []  # list to store the dictionaries for each file processed
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            # Open the file and read each line
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Create a dictionary to store the key-value pairs
            dict_data = {}

            # Loop through each line and split it into words
            for line in lines:
                words = line.split()

                # Use the first word as the key and the rest of the words as the value
                key = words[0]
                values = words[1:]

                # Add the key-value pair to the dictionary
                dict_data[key] = values

            # Append the resulting dictionary to the list
            dict_list.append(dict_data)

    logger.info(f'Finished each_txt_line_to_dict function{dict_list}')

    return dict_list


# Convert dict to TXT
def dict_to_txt(dict_list, output_folder):
    """
    Creates a .txt file for each dictionary in the dict_list, with each line of the file containing the
    key-value pairs of the corresponding dictionary.

    Arguments:
    dict_list -- list of dictionaries to be converted to .txt files
    output_folder -- path to the folder where the .txt files should be created

    Returns:
    None
    """
    logger.info('Starting dict_to_txt function')

    for n, dict_data in enumerate(dict_list):
        # Create a file name for the current dictionary
        file_name = f"dictionary{n}.txt"
        file_path = os.path.join(output_folder, file_name)

        # Write the dictionary to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            for key, values in dict_data.items():
                line = f"{key}: {', '.join(values)}\n"
                f.write(line)

            # Add a blank line after the dictionary
            f.write("\n")

        logger.info(f"Finished writing dictionary {n} to file {file_path}")

    logger.info(f'Finished dict_to_txt function')


# Clean up the dictionaries
def data_cleanup():
    # Dictionary_0
    dict0 = "Armazem_de_Dados"

    # Dictionary_1
    #   Tabela 1686 -
    #   Consumo mensal de energia eletrica,
    #   segundo classe de serviço - Municipio do Rio de Janeiro -
    dict01 = "Consumo_mensal_de_energia_eletrica"

    # Dictionary_02
    # Tabela: 1687
    # Total, mensal, de, unidades, consumidoras, de, energia, elétrica,
    # por classe de consumo no
    # Município do Rio de Janeiro
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""

    # Dictionary
    dict0 = ""


    ...


# Análise Exploratória dos Dados
def data_exploratory():
    ...


# Data Visualization
def data_visualization():
    ...




if __name__ == '__main__':

    # First Step: xls_to_txt
    # logger.info('Starting Step 1: xls_to_txt')
    # folder_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Arquivos"
    # xls_to_txt(folder_path)
    # logger.info('Finished Step 1: xls_to_txt')
    #
    #
    # time.sleep(2)
    #
    #
    # # Second Step: convert_files_to_csv
    # logger.info('Starting Step 2: convert_files_to_csv')
    # input_folder_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Arquivos"
    # output_file_path = r"output"
    # convert_files_to_csv(input_folder_path, output_file_path)
    # logger.info('Finished Step 2: convert_files_to_csv')
    #
    output_file_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Codigos\output"
    # Third Step:
    logger.info('Starting Step 3: Split CSV')
    folder_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Arquivos"
    dict_list = each_txt_line_to_dict(folder_path)
    print(dict_list)
    dict_to_txt(dict_list, output_file_path)