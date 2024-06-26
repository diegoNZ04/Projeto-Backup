
# janela para selecionar a pasta do computador

import os  # listar os arquivos que estão dentro da pasta

from tkinter.filedialog import askdirectory  # selecionar pasta do computador

import shutil  # copiar e colar arquivos

import datetime

nome_pasta_selecionada = askdirectory()  # receber nome da pasta

# listar o que tem dentro de um diretório
lista_arquivos = os.listdir(nome_pasta_selecionada)

# fazer o backup dos arquivos que estão na pasta
nome_pasta_backup = 'backup'
nome_completo_pasta_backup = f'{nome_pasta_selecionada}/{nome_pasta_backup}'
# verificação se existe pasta backup
if not os.path.exists(nome_completo_pasta_backup):
    os.makedirs(nome_completo_pasta_backup)  # criar a pasta backup


data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")


for arquivo in lista_arquivos:
    nome_completo_arquivo = f'{nome_pasta_selecionada}/{arquivo}'
    nome_final_arquivo = f'{nome_completo_pasta_backup}/{data_atual}/{arquivo}'

    if not os.path.exists(f'{nome_completo_pasta_backup}/{data_atual}'):
        os.makedirs(f'{nome_completo_pasta_backup}/{data_atual}')

    if '.' in arquivo:  # verificação se é um arquivo
        # apenas copia arquivos
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif 'backup' != arquivo:  # não copiar novamente a pasta backup
        # apenas copia pastas
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)
