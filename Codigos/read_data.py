import os
import csv
import pandas as pd
import logging
import time
import matplotlib
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    if os.path.isfile(file_name) and nome_arquivo.endswith(".txt"):
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
    ...

# Dictionary_0
dict0 = "Armazem_de_Dados"


# Dictionary_1
#   Tabela 1686 -
#   Consumo mensal de energia eletrica,
#   segundo classe de serviço - Municipio do Rio de Janeiro -
dict00 = "Consumo_mensal_de_energia_eletrica"
dict01 = {
        "Jan": [1097945.505, 350121.439, 261649.757, 355558.115, 170.447, 70121.584, 0.129, 55546.687, 4777.347],
        "Fev": [1145556.844, 360354.173, 269338.115, 375847.478, 241.6, 77655.906, 0.349, 57304.179, 4815.044],
        "Mar": [1073210.613, 329053.693, 252751.696, 353384.172, 233.437, 78999.931, 0.25, 53876.033, 4911.401],
        "Abr": [1270539.403, 460983.039, 286647.461, 377707.96, 243.25, 84441.032, 0.246, 55484.77, 5031.645],
        "Mai": [1236394.662, 403608.164, 300751.107, 380131.273, 233.992, 87859.374, 0.255, 58826.79, 4983.707],
        "Jun": [1145248.96, 362071.84, 293927.364, 347477.148, 230.245, 77165.339, 0.245, 59699.127, 4677.652],
        "Jul": [1011691.705, 346843.06, 234177.068, 304202.722, 145.143, 67550.182, 0.237, 53795.16, 4978.133],
        "Ago": [1082118.1, 359412.252, 250921.868, 334906.852, 148.211, 72509.623, 0.277, 60062.657, 4156.36],
        "Set": [1117000.741, 353521.288, 250542.428, 333853.216, 188.184, 76339.927, 38899.029, 59482],
        "Oct": [1112291.484, 383440.107, 240119.437, 348996.064, 154.319, 78084.225, 0.341, 57223.396, 4273.595],
        "Nov": [1219597.741, 431789.763, 255830.832, 379143.649, 178.124, 87588.153, 0.396, 60780.389, 4286.435]}

d1 = {
     "Data.Rio": {
         "Unnamed 1": 1,
         "Unnamed 2": 2,
         "Unnamed 3": 3,
         "Unnamed 4": 4,
         "Unnamed 5": None,
         "Unnamed 6": None,
         "Unnamed 7": None,
         "Unnamed 8": None,
         "Unnamed 9": None
     },
     "NaN": [None, None, None, None, None, None, None, None, None],
     "Tabela": [
         1686, "-", "Consumo", "mensal", "de", "energia", "elétrica,",
         "segundo", "classe", "de", "serviço", "-", "Municipio", "do", "Rio",
         "de", "Janeiro", "-", 2002, None, None, None, None, None, None, None, None
     ],
     "Mês": ["Consumo (MWh)", None, None, None, None, None, None, None, None],
     "Jan": [1097945.505, 350121.439, 261649.757, 355558.115, 170.447, 70121.584, 0.129, 55546.687,
             4777.347],
     "Fev": [1145556.844, 360354.173, 269338.115, 375847.478, 241.6, 77655.906, 0.349, 57304.179, 4815.044],
     "Mar": [1073210.613, 329053.693, 252751.696, 353384.172, 233.437, 78999.931, 0.25, 53876.033,
             4911.401],
     "Abr": [1270539.403, 460983.039, 286647.461, 377707.96, 243.25, 84441.032, 0.246, 55484.77, 5031.645],
     "Mai": [1236394.662, 403608.164, 300751.107, 380131.273, 233.992, 87859.374, 0.255, 58826.79,
             4983.707],
     "Jun": [1145248.96, 362071.84, 293927.364, 347477.148, 230.245, 77165.339, 0.245, 59699.127, 4677.652],
     "Jul": [1011691.705, 346843.06, 234177.068, 304202.722, 145.143, 67550.182, 0.237, 53795.16, 4978.133],
     "Ago": [1082118.1, 359412.252, 250921.868, 334906.852, 148.211, 72509.623, 0.277, 60062.657, 4156.36],
     "Set": [1117000.741, 353521.288, 250542.428, 333853.216, 188.184, 76339.927, 38899.029, 59482],
     "Oct": [1112291.484, 383440.107, 240119.437, 348996.064, 154.319, 78084.225, 0.341, 57223.396, 4273.595],
     "Nov": [1219597.741, 431789.763, 255830.832, 379143.649, 178.124, 87588.153, 0.396, 60780.389, 4286.435]}

# Dictionary_02
# Tabela: 1687
# Total, mensal, de, unidades, consumidoras, de, energia, elétrica,
# por classe de consumo no
# Município do Rio de Janeiro
dict2 = {
        "Data.Rio": "Unnamed:, 1, Unnamed:, 2, Unnamed:, 3, Unnamed:, 4, Unnamed:, 5, Unnamed:, 6, Unnamed:, 7, Unnamed:, 8, Unnamed:, 9",
        "NaN": "NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN",
        "Tabela": "1687, -, Total, mensal, de, unidades, consumidoras, de, energia, elétrica,, por, classe, de, consumo,, no, Município, do, Rio, de, Janeiro, em, 2002, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN",
        "Mês": "Unidade, consumidora, NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN",
        "Número": "Médio, 2143514.5, 1947923.333333, 10775.833333, 176498.583333, 290, 7432.166667, 47.083333, 387.333333, 160.166667",
        "Jan": "2153359, 1931107, 11185, 202261, 296, 7962, 40, 360, 148",
        "Fev": "2151995, 1930115, 11162, 201902, 295, 7964, 44, 365, 148",
        "Mar": "1842790, 1652107, 9941, 171870, 281, 7932, 22, 346, 291",
        "Abr": "2164270, 1972468, 10890, 172782, 295, 7205, 50, 444, 136",
        "Mai": "2166719, 1976220, 10951, 170963, 294, 7727, 26, 387, 151",
        "Jun": "2169812, 1977948, 10956, 172309, 294, 7747, 20, 387, 151",
        "Jul": "2171634, 1980108, 10948, 171997, 289, 7689, 65, 387, 151",
        "Ago": "2165473, 1982156, 9911, 168929, 284, 3804, 31, 209, 149",
        "Set": "2179116, 1987355, 10867, 172208, 286, 7767, 58, 428, 147",
        "Out": "2182025, 1991528, 10834, 170886, 291, 7824, 76, 436, 150",
        "Nov": "2183617, 1993845, 10749, 170359, 288, 7729, 57, 440, 150",
        "Dez": "2191364, 2000123, 10916, 171517, 287, 7836, 76, 459, 150",
        "Fonte": "Light, Serviços, de, Eletricidade, S.A., NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN"}


data = {
    "Jan": "2153359, 1931107, 11185, 202261, 296, 7962, 40, 360, 148",
    "Fev": "2151995, 1930115, 11162, 201902, 295, 7964, 44, 365, 148",
    "Mar": "1842790, 1652107, 9941, 171870, 281, 7932, 22, 346, 291",
    "Abr": "2164270, 1972468, 10890, 172782, 295, 7205, 50, 444, 136",
    "Mai": "2166719, 1976220, 10951, 170963, 294, 7727, 26, 387, 151",
    "Jun": "2169812, 1977948, 10956, 172309, 294, 7747, 20, 387, 151",
    "Jul": "2171634, 1980108, 10948, 171997, 289, 7689, 65, 387, 151",
    "Ago": "2165473, 1982156, 9911, 168929, 284, 3804, 31, 209, 149",
    "Set": "2179116, 1987355, 10867, 172208, 286, 7767, 58, 428, 147",
    "Out": "2182025, 1991528, 10834, 170886, 291, 7824, 76, 436, 150",
    "Nov": "2183617, 1993845, 10749, 170359, 288, 7729, 57, 440, 150",
    "Dez": "2191364, 2000123, 10916, 171517, 287, 7836, 76, 459, 150"
}

months = []
totals = []

for month, values in data.items():
    month_total = sum([int(val) for val in values.split(',')])
    months.append(month)
    totals.append(month_total)

plt.bar(months, totals)
plt.title('Total Units of Electricity Consumed by Month')
plt.xlabel('Month')
plt.ylabel('Total Units Consumed')
plt.show()

# Dictionary_03
dict3 = {
'DATA.RIO': ['Unnamed:', 1, 'Unnamed:', 2, 'Unnamed:', 3, 'Unnamed:', 4, 'Unnamed:', 5],
'NaN': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'Tabela': ['1816', '-', 'Educação', 'infantil', '-', 'Número', 'de', 'escolas', 'com', 'abastecimento', 'de', 'água,', 'de', 'energia', 'elétrica,', 'e', 'esgoto', 'sanitário,', 'segundo', 'a', 'dependência', 'administrativa', 'e', 'modalidade', '-', 'Município', 'do', 'Rio', 'de', 'Janeiro', '-', '2000', '-', '2006', float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'Dependência': ['Administrativa', 'Modalidade', 'Total', 'de', 'Escolas', 'Escolas', 'com', 'Água', 'Escolas', 'com', 'Energia', 'Elétrica', 'Escolas', 'com', 'Esgoto'],
'2000': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'Federal': ['Creche', 2, 2, 2, 2],
'Estadual': ['Creche', 4, 4, 4, 4],
'Municipal': ['Creche', 226, 225, 226, 226],
'Particular': ['Creche', 966, 965, 966, 965],
'2001': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'2002': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'2003': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'2004': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'2005': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'2006': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'Fonte': ['Instituto', 'Nacional', 'de', 'Estudos', 'e', 'Pesquisas', 'Educacionais', '-', 'INEP,', 'EDUDATABRASIL,', 'www.edudatabrasil.inep.gov.br,', 'em', 'novembro', 'de', '2007.', float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'Nota': [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')],
'(...)': ['dado', 'numérico', 'não', 'disponível', float('nan'), float('nan'), float('nan'), float('nan'), float('nan')]
}


# Dictionary_04
dict4 =  {
            "DATA.RIO": ["Unnamed:", 1, "Unnamed:", 2, "Unnamed:", 3, "Unnamed:", 4],
            "NaN": [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            "Tabela": [1817, "-", "Ensino", "fundamental", "-", "Número", "de", "escolas", "com", "abastecimento", "de", "água,", "de", "energia", "elétrica", "e", "esgoto", "sanitário,", "segundo", "a", "dependência", "administrativa", "-", "Município", "do", "Rio", "de", "Janeiro", "-", 2000, "-", 2006, float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            "Dependência": ["Administrativa", "Total", "de", "Escolas", "Escolas", "com", "Água", "Escolas", "com", "Energia", "Elétrica", "Escolas", "com", "Esgoto"],
            2000: [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            "Federal": [13, 13, 13, 13],
            "Estadual": [99, 99, 99, 99],
            "Municipal": [980, 978, 980, 980],
            "Particular": [1009, 1007, 1009, 1008],
            2001: [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            2002: [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            2003: [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            2004: [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            2005: [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            2006: [float("NaN"), float("NaN"), float("NaN"), float("NaN")],
            "Fonte": ["Instituto", "Nacional", "de", "Estudos", "e", "Pesquisas", "Educacionais", "-", "INEP,", "EDUDATABRASIL", "-", "www.edudatabrasil.inep.gov.br", "-", "em", "novembro", "de", "2007.", float("NaN"), float("NaN"), float("NaN"), float("NaN")]
            }


# Dictionary_05
dict5 = {
    2004: [331952, 34628],
    2005: [360534, 39765],
    2006: [364208, 34269],
    2007: [364554.04, 37044.84],
    2008: [744400, 38932.4],
    2009: [359328, 45039],
    2010: [363120, 47175],
    2011: [640985, 46132],
    2012: [645047, 45737],
    2013: [636799, 48680.79],
    2014: [659372.15, 49487.34],
    2015: [650319.41, 46947.9],
    2016: [661256.46, 52057.64],
    2017: [666600, 53546.14],
    2018: [273922.91, 48280.85],
    2019: [278688.34, 51650.49],
    2020: [621269.27, 56105.99]
}


# Dictionary_06
"""Tabela: 2178 - Ensino médio -
   Número de escolas com abastecimento de água,
   de energia elétrica, esgoto e sanitário,
   segundo a dependência administrativa
- Município do Rio de Janeiro"""
dict6 = {
            "2000": [None, None, None, None],
            "Federal": [13, 13, 13, 13],
            "Estadual": [293, 293, 293, 293],
            "Particular": [379, 377, 379, 379],
            "2001": [None, None, None, None],
            "2002": [None, None, None, None],
            "2003": [None, None, None, None],
            "2004": [None, None, None, None],
            "2005": [None, None, None, None],
            "2006": [None, None, None, None]
}


# Dictionary_07
"""
Tabela: 2257 - Consumo total médio anual, mensal e diário de energia elétrica por habitante no Município do Rio de Janeiro.

+---------------+---------------+---------------+---------------+---------------+
|    Ano        |   Consumo     |   Consumo     |   Consumo     |   Consumo     |
|               |    total      |    médio      |    médio      |    médio      |
|               |    (MWh)      |  anual (kWh)  | mensal (kWh)  |  diário (kWh) |
+===============+===============+===============+===============+===============+"""
dict7 = data = {
1980: [8871979, 1.742751, 145.229244, 4.77466, 5090790],
1981: [8884447, 1.733528, 144.460694, 4.749393, 5125065.942624],
1982: [9594291, 1.859513, 154.959393, 5.094555, 5159572.662837],
1983: [10902884, 2.099005, 174.917047, 5.750697, 5194311.714448],
1984: [11622014, 2.222486, 185.207199, 6.089004, 5229284.66173],
1985: [11765155, 2.234813, 186.234376, 6.122774, 5264493.079486],
1986: [12446331, 2.348392, 195.699297, 6.433949, 5299938.553123],
1987: [12475527, 2.338158, 194.846471, 6.405911, 5335622.678722],
1988: [12652650, 2.355495, 196.291215, 6.45341, 5371547.06311],
1989: [13101033, 2.422657, 201.88806, 6.637416, 5407713.323933],
1990: [13381590, 2.457988, 204.832345, 6.734214, 5444123.089729],
1991: [13227294, 2.413397, 201.116429, 6.612047, 5480778.0],
1992: [13124963, 2.377085, 198.090439, 6.512562, 5521452.32596],
1993: [13106850, 2.356318, 196.359827, 6.455666, 5562428.50702],
1994: [13386636, 2.388889, 199.07405, 6.5449, 5603708.783328],
1995: [14240773, 2.522591, 210.21594, 6.911209, 5645295.411657],
1996: [14542926, 2.557137, 213.094755, 7.005855, 5687190.665526],
1997: [15319686, 2.673874, 222.822844, 7.325683, 5729396.83533],
1998: [16067326, 2.783707, 231.975618, 7.626596, 5771916.228459],
1999: [16197358.8285, 2.785564, 232.130295, 7.631681, 5814751.169427],
2000: [16570295.876, 2.828707, 235.725609, 7.749883, 5857904],
2001: [15027501.406, 2.54812, 212.343361, 6.981152, 5897485],
2002: [13739063.105, 2.314044, 192.836978, 6.339846, 5937253],
2003: [13868520.334, 2.321448, 193.454027, 6.360132, 5974081],
2004: [13671031.567, 2.259152, 188.262686, 6.189458, 6051399],
2005: [14341920.37, 2.353379, 196.11489, 6.447613, 6094183],
2006: [14768793.382, 2.406653, 200.554436, 6.593571, 6136652],
2007: [16520491.3006, 2.693994, 224.499499, 7.380805, 6132341.549447],
2008: [16596539.1103, 2.693786, 224.482125, 7.380234, 6161047],
2009: [16130144.516, 2.607225, 217.268744, 7.143082, 6186710],
2010: [16935390.673, 2.679461, 223.288445, 7.34099, 6320446],
2011: [16901704.3574, 2.659194, 221.599538, 7.285464, 6355949],
2012: [17108243.045, 2.677225, 223.102069, 7.334863, 6390290],
2013: [17476913.4244, 2.71806, 226.50496, 7.446738, 6429923],
2014: [18096223.833961, 2.804015, 233.667952, 7.682234, 6453682],
2015: [17661297.714224, 2.726927, 227.243888, 7.471032, 6476631],
2016: [17341174.634, 2.66835, 222.362538, 7.310549, 6498837],
2017: [17170484.229827, 2.633402, 219.450201, 7.214801, 6520266],
2018: [16732525.617581, 2.501526, 208.46051, 6.853496, 6688927],
2019: [16899915.836673, 2.515279, 209.606586, 6.891175, 6718903]
}



# Dictionary_08
"""
Tabela: 2501 - Consumo anual de energia elétrica segundo classe de consumo por Áreas de Planejamento (AP), Regiões de Planejamento (RP), Regiões Administrativas (RA) NaN NaN NaN NaN NaN NaN NaN NaN NaN
e atribuída a uma única unidade consumidora, razão pela qual os valores são nulos em diversos bairros. Na cidade do Rio de Janeiro a Iluminação pública é de responsabilidade NaN NaN NaN NaN NaN NaN NaN NaN NaN
Áreas de Planejamento, Regiões de Planejamento, Regiões Administrativas e bairros Consumo de energia elétrica (MWh)
"""

dict0 = {
'I': {
    'Portuária': [203197.42, 19820.859, 57178.887, 89194.177, 0, 27813.492, 0, 8393.531, 796.474],
    'Caju': [75959.987, 7793.311, 27173.098, 32209.315, 0, 4089.735, 0, 4690.054, 4.474],
    'Gamboa': [24705.203, 4433.087, 2043.672, 13619.638, 0, 4607.606, 0, 1.2, 0],
    'Santo Cristo': [34219.933, 6022.045, 4533.591, 16281.781, 0, 3681.439, 0, 3701.077, 0],
    'Saúde': [68312.297, 1572.416, 23428.526, 27083.443, 0, 15434.712, 0, 1.2, 792],
},
'II': {
    'Centro': [1150446.099, 39050.746, 17581.202, 848203.731, 0, 205381.498, 0, 395.798, 39833.124],
    'Lapa': [0, 0, 0, 0, 0, 0, 0, 0, 0],
},
'III': {
    'Rio Comprido': [302582.299, 49782.382, 6205.775, 65004.104, 0, 33511.329, 0, 142592.614, 5486.095],
    'Catumbi': [26373.206, 7861.268, 196.538, 13532.063, 0, 157.77, 0, 260.632, 4364.935],
    'Cidade de Deus': [49644.965, 16786.357, 15820.983, 16344.028, 0, 689.397, 0, 4.2, 0],
    'Estácio': [24231.702, 9598.16, 890.105, 5328.126, 0, 7337.224, 0, 214.027, 864.06],
},
'VII': {
    'neighborhood': 'São Cristóvão',
    'area': 338935.474,
    'pop_density': 46166.292,
    'avg_income': 149101.323,
    'avg_age': 112600.165,
    'pct_private_residences': 0,
    'avg_monthly_income': 28725.478,
    'pct_bachelors_degree': 0,
    'pct_graduate_degree': 2204.966,
    'pct_elderly': 137.25
},
'Benfica': {
    'area': 121140.681,
    'pop_density': 12742.405,
    'avg_income': 70697.296,
    'avg_age': 25998.398,
    'pct_private_residences': 0,
    'avg_monthly_income': 11230.683,
    'pct_bachelors_degree': 0,
    'pct_graduate_degree': 471.899,
    'pct_elderly': 0
},
'Imperial': {
    'neighborhood': 'São Cristóvão',
    'area': 201702.588,
    'pop_density': 23153.795,
    'avg_income': 77453.849,
    'avg_age': 83745.257,
    'pct_private_residences': 0,
    'avg_monthly_income': 16179.788,
    'pct_bachelors_degree': 0,
    'pct_graduate_degree': 1032.649,
    'pct_elderly': 137.25
},
'Mangueira': {
    'area': 7022.285,
    'pop_density': 4061.72,
    'avg_income': 357.093,
    'avg_age': 693.027,
    'pct_private_residences': 0,
    'avg_monthly_income': 1315.007,
    'pct_bachelors_degree': 0,
    'pct_graduate_degree': 595.438,
    'pct_elderly': 0
},
'Vasco': {
    'neighborhood': 'Gama',
    'area': 9069.92,
    'pop_density': 6208.372,
    'avg_income': 593.085,
    'avg_age': 2163.483,
    'pct_private_residences': 0,
    'avg_monthly_income': 0,
    'pct_bachelors_degree': 104.98,
    'pct_graduate_degree': 0,
    'pct_elderly': 0
},
'XXI': {
    'neighborhood': 'Paquetá',
    'area': 13998.134,
    'pop_density': 4063.388,
    'avg_income': 62.994,
    'avg_age': 9222.856,
    'pct_private_residences': 0,
    'avg_monthly_income': 371.114,
    'pct_bachelors_degree': 0,
    'pct_graduate_degree': 267.715,
    'pct_elderly': 10.067
},
'Paquetá': [13998.134, 4063.388, 62.994, 9222.856, 0, 371.114, 0, 267.715, 10.067],
'XXIII: Santa Teresa': [37740.406, 27505.894, 776.373, 6785.732, 0, 1643.607, 0, 1028.8, 0],
'Santa Cruz': [1880404.35, 80820.636, 1751126.911, 36766.215, 349.029, 10796.204, 0, 333.569, 211.786],
'IV: Botafogo': [830004.111, 321482.014, 12856.851, 447080.71, 0, 42730.968, 18.69, 3223.48, 2611.398],
'Botafogo': [392334.829, 105324.878, 6722.081, 270428.229, 0, 9198.791, 0, 164.57, 496.28],
'Catete': [34772.464, 13342.024, 828.875, 20081.6, 0, 518.855, 0.75, 0.36, 0],
'Cosme Velho': [22784.928, 8153.452, 138.961, 11800.843, 0, 2028.885, 0, 662.787, 0],
'Flamengo': [140687.909, 83550.725, 1279.837, 51142.168, 0, 2767.523, 0, 145.538, 1802.118],
'Glória': [53031.95, 12645.714, 794.192, 35466.171, 0, 3356.567, 8.8, 760.506, 0],
'Humaitá': [49711.206, 23284.937, 1359.562, 23508.365, 0, 1401.998, 0, 156.344, 0],
'Laranjeiras': [103338.855, 65675.271, 1610.383, 25966.599, 0, 9445.182, 3.19, 325.23, 313],
'Urca': [33341.97, 9505.013, 122.96, 8686.735, 0, 14013.167, 5.95, 1008.145, 0],
'V: Copacabana': [515440.015, 253163.465, 6709.39, 242103.766, 0, 3810.45, 0.283, 9425.595, 227.066],
'Copacabana': [475993.106, 233098.898, 6348.39, 223855.224, 0, 3212.469, 0.283, 9250.776],
'Leme': [39446.909, 20064.567, 361, 18248.542, 0, 597.981, 0, 174.819, 0],
'VI': ['Lagoa', 687132.791, 355061.695, 7819.16, 291542.941, 0, 20703.142, 0, 11785.156, 220.697],
'Gávea': [80955.937, 35718.825, 981.826, 39255.445, 0, 2448.116, 0, 2542.527, 9.198],
'Ipanema': [206083.777, 96852.622, 4585.477, 100581.93, 0, 3441.549, 0, 621.97, 0.229],
'Jardim Sulacap': [34403.446, 12539.915, 617.999, 12043.56, 0, 9200.54, 0, 1.432, 0],
'Lagoa': [65603.513, 49841.182, 471.733, 13737.388, 0, 763.653, 0, 789.557, 0],
'Leblon': [187065.899, 104049.958, 719.372, 74808.55, 0, 6414.389, 0, 1054.388, 19.242],
'São Francisco Xavier': [20936.723, 8282.055, 4056.197, 6290.854, 0, 2215.717, 0, 91.9, 0],
'Vidigal': [19264.242, 6121.259, 46.081, 11191.729, 0, 120.973, 0, 1784.2, 0],
'Rocinha': [25404.6, 20672.504, 113.691, 3224.579, 0, 243.481, 0, 1073.515, 76.83],
'VIII: Tijuca': [480517.354, 219876.686, 6279.022, 201427.791, 0, 10474.485, 38157.564, 4220.222, 81.584],
'Alto da Boa Vista': [23748.082, 8966.898, 251.147, 12537.991, 0, 615.658, 0, 1333.09, 43.298],
'Praça Seca': [51756.413, 36892.694, 1131.245, 11636.106, 0, 1558.71, 0, 537.658, 0],
'Tijuca': [428233.333, 199051.135, 5535.678, 175339.369, 0, 7257.579, 38157.564, 2853.722, 38.286],
'IX: Vila Isabel': [425496.482, 204523.568, 5370.492, 159686.113, 0, 50332.979, 0, 5243.949, 339.381],
'Andaraí': [89603.401, 35312.277, 666.159, 47830.551, 0, 5468.068, 0, 289.85, 36.496],
'Grajaú': [65935.546, 49055.548, 856.685, 14677.137, 0, 472.176, 0, 582.587, 291.413],
'Maracanã': [125242.518, 37238.84, 520.452, 57610.567, 0, 29656.564, 0, 216.095, 0],
'Vila Militar': [7595.095, 2301.58, 0.1, 634.124, 0, 4500.768, 0, 157.931, 0.592],
'X: Ramos': [374635.164, 147183.506, 52442.696, 110057.38, 5.352, 56318.373, 0.666, 8523.196, 103.995],
'Bonsucesso': [172232.93, 42214.465, 22122.115, 57846.056, 5.202, 49477.03, 0.666, 541.481, 25.915],
'Manguinhos': [40221.497, 22515.633, 13636.818, 3617.009, 0.15, 389.781, 0, 62.106, 0],
'Olaria': [78898.098, 43604.602, 5489.343, 24927.325, 0, 4531.976, 0, 301.65, 43.202],
"Ramos": [83282.639, 38848.806, 11194.42, 23666.99, 0, 1919.586, 0, 7617.959, 34.878],
"XXX": ["Maré", None, None, None, None, None, None, None, None],
"Maré": [None, None, None, None, None, None, None, None, None],
"XIII": ["Méier", 730930.09, 352416.846, 127249.004, 210571.995, 14.947, 33948.908, 0, 5197.957, 1530.433],
"Abolição": [20224.411, 11478.576, 510.429, 7562.136, 0, 137.8, 0, 375.179, 160.291],
"Água": ["Santa", 7703.048, 2390.418, 108.392, 4057.155, 11.457, 604.586, 0, 0, 531.04],
"Cachambi": [93058.594, 40122.687, 10713.127, 41860.389, 0, 293.454, 0, 68.937, 0],
"Encantado": [19580.984, 11544.724, 763.239, 7169.221, 0, 103.8, 0, 0, 0],
"Engenho da Rainha": [26689.854, 17167.365, 3339.395, 5549.057, 0, 364.062, 0, 269.975, 0],
"Jacaré": [88478.267, 11674.312, 71088.446, 5397.6, 0, 144.723, 0, 172.394, 0.792],
"Lins de Vasconcelos": [35571.717, 20427.121, 334.781, 3179.151, 0.03, 10355.666, 0, 733.156, 541.812],
"Méier": [130044.761, 72050.041, 1644.902, 47429.675, 0, 8754.839, 0, 165.304, 0],
"Piedade": [64755.508, 34558.678, 13506.912, 13562.151, 3.46, 2172.699, 0, 933.36, 18.248],
"Pilares": [42110.616, 19459.228, 13145.539, 8629.927, 0, 349.438, 0, 525.996, 0.488],
"Riachuelo": [20891.306, 13007.546, 1099.081, 6156.949, 0, 582.109, 0, 45.621, 0],
"Rocha": [37116.407, 24559.254, 983.69, 8668.493, 5.063, 1155.39, 0, 7.188, 1737.329],
"Sampaio": [17043.647, 5353.882, 1141.818, 10194.223, 0, 96.256, 0, 5.228, 252.24],
"Todos os Santos": [28651.45, 21057.027, 3669.567, 3693.481, 0, 140.557, 0, 90.818, 0],
"XXVIII": [7265.051, 681.854, 5024.625, 1375.664, 0, 91.61, 0, 3.086, 88.212],
"Jacarezinho": [7265.051, 681.854, 5024.625, 1375.664, 0, 91.61, 0, 3.086, 88.212],
"XIV": [356479.254, 165340.034, 66418.718, 103659.524, 24.333, 4954.89, 0, 16081.755, 0],
"Colégio": [68491.908, 13813.029, 46348.05, 7096.213, 9.436, 311.152, 0, 914.028, 0],
"Irajá": [134278.775, 76470.218, 1642.146, 51514.098, 4.667, 3946.589, 0, 701.057, 0],
"Vicente de Carvalho": [34906.557, 13003.245, 1603.16, 18861.569, 0, 77.21, 0, 1361.373, 0],
"Vista Alegre": [17434.072, 11345.711, 211.89, 5677.413, 5.303, 193.755, 0, 0, 0],
 'XV: Madureira': [560147.985, 238124.286, 148515.134, 152596.217, 141.494, 16674.141, 0, 2290.198, 1806.515],
'Bento: Ribeiro': [46162.551, 32299.142, 1298.889, 12369.523, 0, 165.78, 0, 12.297, 16.92],
'Campinho': [12263.094, 10318.507, 83.971, 1581.307, 0, 242.643, 0, 0, 36.666],
'Cascadura': [36535.567, 20655.979, 1402.856, 12557.746, 22.696, 1209.597, 0, 686.693, 0],
'Cavalcanti': [14047.392, 9506.499, 1997.659, 1800.051, 0, 329.885, 0, 413.298, 0],
'Engenheiro: Leal': [3387.894, 2643.459, 467.005, 207.292, 0, 43.948, 0, 10.59, 15.6],
'Honório: Gurgel': [121035.235, 11800.421, 107619.06, 1541.03, 0.52, 74.004, 0, 0.2, 0],
'Madureira': [121140.812, 36822.511, 1941.255, 79364.142, 37.016, 2594.193, 0, 381.695, 0],
'Marechal: Hermes': [47902.246, 26627.455, 1598.958, 12586.606, 17.569, 7066.381, 0, 5.277, 0],
'Oswaldo: Cruz': [37050.883, 24472.964, 2432.074, 9281.025, 0, 446.487, 0, 418.333, 0],
'Quintino: Bocaiúva': [27441.86, 19235.693, 923.051, 4000.561, 2.429, 3173.52, 0, 106.606, 0],
'Turiaçu': [38925.987, 8447.559, 27629.143, 2607.306, 56.201, 107.963, 0, 77.815, 0],
'Vaz: Lobo': [17138.057, 10734.843, 137.523, 6031.135, 0, 64.35, 0, 170.206, 0],
'XII: Inhaúma': [257634.178, 95612.246, 84047.13, 69392.306, 3.792, 5281.476, 3.792, 3057.731, 235.705],
"Maria": ["da", "Graça", 38046.76, 7416.029, 28479.802, 1848.455, 0, 252.666, 0, 49.808, 0],
"Tomás": ["Coelho", 14968.675, 12248.46, 992.173, 1339.955, 0, 78.063, 0, 253.74, 56.284],
"XXIX": ["Complexo", "do", "Alemão", "...", "...", "...", "...", "...", "...", "...", "..."],
"Complexo": ["do", "Alemão", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
"XI": ["Penha", 243023.003, 113387.918, 29819.104, 79603.477, 31.515, 12407.074, 0, 7474.83, 299.085],
"Brás": ["de", "Pina", 47748.518, 36076.768, 1719.091, 9251.409, 11.891, 626.031, 0, 63.328, 0],
"Penha": ["Circular", 96830.782, 29377.853, 23297.034, 33242.704, 19.624, 9731.552, 0, 919.25, 242.765],
"XXXI": ["Vigário", "Geral", 166141.057, 68049.443, 55082.41, 32599.615, 10.72, 8631.022, 0, 1767.847, 0],
"Cordovil": [53478.412, 25329.021, 19284.386, 8113.108, 1.262, 702.257, 0, 48.378, 0],
"Parada": ["de", "Lucas", 25675.441, 9971.844, 6344.332, 5192.677, 0, 3079.254, 0, 1087.334, 0],
"Vigário": ["Geral", 52370.268, 13974.962, 24206.152, 11097.152, 0, 2479.492, 0, 612.51, 0],
"XXII": ["Anchieta", 150224.631, 92859.804, 25891.637, 26254.366, 3.304, 3371.28, 0, 1820.138, 24.102],
"Anchieta": [43582.493, 32568.129, 1915.362, 7788.594, 0.849, 549.51, 0, 760.049, 0],
"Guadalupe": [70401.454, 29660.447, 23445.074, 15686.157, 2.455, 1081.05, 0, 526.271, 0],
'Parque': ['Colúmbia', 3761.138, 3231.181, 170.829, 359.128, 0, 0, 0, 0, 0],
'Ricardo': ['de', 'Albuquerque', 17490.183, 14234.629, 435.396, 1482.079, 0, 927.657, 0, 386.32, 24.102],
'XXV': ['Pavuna', 233220.257, 82518.429, 83276.318, 49987.203, 7.754, 3108.769, 300.7, 13898.884, 122.2],
'Acari': [5809.161, 3661.834, 1152.247, 508.606, 0, 232.056, 0, 238.578, 15.84],
'Barros': ['Filho', 19890.35, 6830.517, 10013.403, 2863.987, 7.754, 173.589, 0, 1.1, 0],
'Coelho': ['Neto', 45278.662, 18466.353, 17798.026, 7767.169, 0, 849.176, 0, 291.578, 106.36],
'Costa': ['Barros', 13443.155, 11650.002, 421.601, 777.284, 0, 403.384, 0, 190.884, 0],
'Pavuna': [145037.791, 38678.542, 53720.212, 37711.029, 0, 1450.564, 300.7, 13176.744, 0],
'XX': ['Ilha', 'do', 'Governador', 574750.206, 177512.78, 49179.231, 88285.844, 0, 250808.993, 419.54, 8369.894,
       173.924],
'Bancários': [61672.058, 9102.397, 452.445, 1096.413, 0, 50595.402, 0, 425.401, 0],
'Cacuia': [15015.185, 6010.166, 400.006, 7444.423, 0, 827.54, 0, 333.05, 0],
'Cocotá': [9858.175, 5270.323, 456.057, 3199.182, 0, 343.688, 0, 588.925, 0],
'Freguesia': ['(Jacarepaguá)', 110928.608, 57290.759, 17068.833, 35430.94, 0, 595.241, 0, 434.735, 108.1],
'Galeão': [159177.733, 11389.3, 218.056, 8090.024, 0, 138856.359, 9.349, 469.107, 145.538],
'Moneró': [14146.093, 7418.085, 81.853, 6457.569, 0, 183.406, 0, 5.18, 0],
'Pitangueiras': [9145.061, 8209.188, 117.803, 409.04, 0, 281.087, 0, 127.943, 0],
'Portuguesa': [50255.908, 21206.991, 284.582, 27757.874, 0, 979.096, 0, 27.365, 0],
'Praia da Bandeira': [5734.701, 5356.118, 61.265, 260.838, 0, 56.48, 0, 0, 0],
'Ribeira': [23264.746, 3815.876, 14808.134, 4581.317, 0, 31.84, 0, 27.579, 0],
'Tauá': [31822.147, 16217.348, 6213.319, 6425.165, 0, 200.228, 0, 2766.087, 0],
'Zumbi': [2674.496, 1762.596, 111.441, 505.774, 0, 71.21, 0, 223.475, 0],
'XVI Jacarepaguá': [689888.833, 349597.089, 155981.07, 154803.83, 473.467, 25302.485, 0, 2527.008, 1203.884],
'Anil': [55723.26, 25750.636, 16721.493, 12864.125, 0, 317.804, 0, 69.202, 0],
'Curicica': [74620.105, 30085.083, 20333.286, 15707.276, 0, 8225.406, 0, 33.537, 235.517],
'Gardênia Azul': [14282.979, 8638.217, 3148.374, 2023.003, 411.417, 61.968, 0, 0, 0],
'Jacarepaguá': [23384.832, 14393.971, 2806.303, 2279.284, 9.171, 3670.275, 0, 225.828, 0],
'Pechincha': [57534.316, 37947.775, 3348.068, 14124.898, 16.95, 1037.721, 0, 299.204, 759.7],
'Tanque': [43463.019, 25559.604, 730.434, 13284.234, 0, 3088.603, 0, 723.519, 76.625],
'Taquara': [216275.696, 79391.162, 89965.129, 40407.16, 35.929, 6443.644, 0, 32.24, 0.432],
'XXXIV: Cidade, de, Deus': [49644.965, 16786.357, 15820.983, 16344.028, 0, 689.397, 0, 4.2, 0],
'XXIV: Barra, da, Tijuca': [823572.498, 369256.639, 36182.039, 403086.788, 301.571, 11992.68, 1.2, 2234.979, 516.602],
'Barra: de, Guaratiba': [6232.542, 3760.105, 68.557, 1131.783, 18.6, 922.229, 0, 331.268, 0],
'Camorim': [27496.644, 6277.254, 13011.427, 8093.403, 0, 114.56, 0, 0, 0],
'Grumari': [113.238, 51.269, 0, 61.969, 0, 0, 0, 0, 0],
'Itanhangá': [37265.585, 28036.866, 853.865, 7758.124, 0, 497.33, 0, 112.17, 7.23],
'Joá': [11355.453, 3267.309, 190.216, 7896.538, 0, 1.39, 0, 0, 0],
'Recreio: dos, Bandeirantes': [78538.68, 65125.977, 2910.6, 10462.849, 41.064, 0, 0, 1.81, 0],
'Vargem: Pequena': [16403.704, 7902.357, 3972.913, 3839.721, 151.211, 158.447, 0, 379.055, 0],
'XVII': ['Bangu', 298167.893, 193330.408, 14238.442, 73580.505, 52.678, 16292.179, 0, 344.113, 329.568],
 'Bangu': [187964.326, 118150.479, 9031.253, 47396.757, 52.678, 12684.236, 0, 319.355, 329.568],
'Gericinó': [..., ..., ..., ..., ..., ..., ..., ..., ...],
'Padre Miguel': [57163.387, 36366.479, 1943.87, 17598.918, 0, 1231.012, 0, 23.108, 0],
'Senador Vasconcelos': [287580.33, 14374.323, 1602.225, 2763.67, 1.408, 3103.541, 0, 265735.163, 0],
'XXXIII': ['Realengo', 368986.33, 129262.818, 7106.44, 46767.711, 2.22, 27249.805, 0, 158564.358, 32.978],
'Campo Grande': [430151.736, 179319.273, 132032.534, 103336.377, 444.714, 14230.489, 0.16, 258.871, 529.318],
'Deodoro': [173361.14, 6190.579, 604.646, 2441.674, 2.22, 6124.089, 0, 157993.932, 4],
'Magalhães Bastos': [20118.532, 17103.541, 182.071, 1213.33, 0, 1417.952, 0, 201.638, 0],
'Realengo': [133068.335, 90720.02, 5701.824, 30402.224, 0, 6006.456, 0, 209.425, 28.386],
'XVIII': ['Campo Grande', 813068.679, 265724.802, 142792.348, 117871.746, 511.539, 19377.363, 0.16, 266182.585, 608.136],
'Cosmos': [29471.571, 25811.438, 697.001, 2426.84, 0, 482.664, 0, 19.46, 34.168],
'Inhoaíba': [26362.043, 21495.503, 1869.323, 1722.258, 9.723, 1265.236, 0, 0, 0],
'Santíssimo': [39502.999, 24724.265, 6591.265, 7622.601, 55.694, 295.433, 0, 169.091, 44.65],
"XIX: Santa Cruz": [1956712.185, 137134.29, 1757953.13, 46843.03, 356.42, 13162.143, 0, 1051.162, 212.01],
"Paciência": [51944.449, 36464.094, 6580.499, 7249.111, 7.391, 1563.299, 0, 80.055, 0],
"Sepetiba": [24363.386, 19849.56, 245.72, 2827.704, 0, 802.64, 0, 637.538, 0.224],
"XXVI: Guaratiba": [73675.661, 47245.342, 6378.408, 12757.024, 402.533, 6500.482, 0, 376.392, 15.48],
"Guaratiba": [48993.51, 33701.982, 5890.042, 3981.232, 377.874, 5013.377, 0, 13.523, 15.48],
"Pedra de Guaratiba": [18449.609, 9783.255, 419.809, 7644.009, 6.059, 564.876, 0, 31.601, 0]
}

# Dictionary_09
dict0 = ""



# Dictionary_10
"""
Ano: Total residencial (MWh) Consumo residencial por unidade consumidora NaN NaN Total de unidades consumidoras residenciais (1)
"""
dict10 = {
'1990': [4067251, 2.609943, 217.495215, 7.249841, 1558368],
'1991': [4076534, 2.545503, 212.125252, 7.070842, 1601465],
'1992': [4094761, 2.535194, 211.266131, 7.042204, 1615167],
'1993': [0, 0, 0, 0, 1783805],
'1994': [0, 0, 0, 0, 1801172],
'1995': [5672014, 3.154696, 262.89133, 8.763044, 1797959],
'1996': [4781250.47, 2.722412, 226.867704, 7.562257, 1756255],
'1997': [5110170.354, 2.84553, 237.127486, 7.90425, 1795859],
'1998': [5520551.814, 2.998722, 249.893526, 8.329784, 1840968],
'1999': [5672014, 2.873698, 239.474869, 7.982496, 1973768],
'2000': [5720372, 2.864206, 238.683826, 7.956128, 1997193],
'2001': [4788217, 2.461682, 205.140138, 6.838005, 1945100],
'2002': [4603194.384, 2.301456, 191.787971, 6.392932, 2000123],
'2003': [4887462.045, 2.405248, 200.437354, 6.681245, 2031999],
'2004': [4840609.046, 2.336871, 194.739268, 6.491309, 2071406],
'2005': [5264761.083, 2.500209, 208.350789, 6.945026, 2105728],
'2006': [5286605.181, 2.312877, 192.739742, 6.424658, 2285727],
'2007': [5392563.6376, 2.358056, 196.504697, 6.550157, 2286868],
'2008': [5383557.3004, 2.325411, 193.784272, 6.459476, 2315099],
'2009': [5759226.624, 2.439101, 203.258383, 6.775279, 2361209.142857],
'2010': [5988844, 2.492083, 207.673574, 6.922452, 2403148],
'2011': [6018866.577, 2.472655, 206.054549, 6.868485, 2434172],
'2012': [5716652.172, 2.488978, 207.414828, 6.913828, 2296787],
'2013': [5757301.519, 2.450374, 204.197861, 6.806595, 2349560],
'2014': [6154636.363861, 2.565875, 213.822927, 7.127431, 2398650],
'2015': [5999339.641401, 2.465254, 205.437869, 6.754122, 2433558],
'2016': [5899648.858, 2.360585, 196.715393, 6.467355, 2499232],
'2017': [6071649.0542, 2.360264, 196.688658, 6.466476, 2572445],
'2018': [5798436.087546, 2.277667, 189.805559, 6.240183, 2545779],
'2019': [5839173.962018, 2.192046, 182.670489, 6.005605, 2663801]


}




# Análise Exploratória dos Dados
def data_exploratory():
    ...


# Data Visualization
def data_visualization():
    ...

# DICT 1:

def generate_chart(data):
    months = list(data.keys())
    values = [sum(data[month]) for month in months]

    fig, ax = plt.subplots()

    ax.bar(months, values)
    ax.set_xlabel("Month")
    ax.set_ylabel("Value")
    ax.set_title("Monthly Values")

    plt.show()



if __name__ == '__main__':

    # # First Step: xls_to_txt
    # # logger.info('Starting Step 1: xls_to_txt')
    # # folder_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Arquivos"
    # # xls_to_txt(folder_path)
    # # logger.info('Finished Step 1: xls_to_txt')
    #
    #
    # # time.sleep(2)
    #
    #
    # # Second Step: convert_files_to_csv
    # logger.info('Starting Step 2: convert_files_to_csv')
    # input_folder_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Arquivos"
    # output_file_path = r"output"
    # convert_files_to_csv(input_folder_path, output_file_path)
    # logger.info('Finished Step 2: convert_files_to_csv')
    #
    # # output_file_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Codigos\output"
    # # Third Step:
    # logger.info('Starting Step 3: Split CSV')
    # folder_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Arquivos"
    # dict_list = each_txt_line_to_dict(folder_path)
    # print(dict_list)
    # dict_to_txt(dict_list, output_file_path)
    print("generate_chart")
    generate_chart(dict01)
    pass