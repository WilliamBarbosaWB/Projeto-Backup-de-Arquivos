#janela para selecionar a pasta do nosso computador 

import os
from tkinter.filedialog import askdirectory
import shutil
import datetime



nome_pasta_selecionada = askdirectory()

print(nome_pasta_selecionada)


lista_arquivos = os.listdir(nome_pasta_selecionada) #serve para listar o que tem dentro de um diretório
print(lista_arquivos)


#fazer o backup dos arquivos que estão nessa pasta 

nome_pasta_backup = "backup"
nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"

if not os.path.exists(nome_completo_pasta_backup): #se não existe o nome da pasta crie
    os.mkdir(nome_completo_pasta_backup) #criando uma pasta de backup dentro da pasta dos arquivos

data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S") #pegar o dia e a hora de rodar o codigo


for arquivo in lista_arquivos:
    print(arquivo)
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"

    nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"

    if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"): #se não existe o nome da pasta crie
        os.mkdir(f"{nome_completo_pasta_backup}/{data_atual}")

    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif "backup" != arquivo: #se o nome do arquivo for diferente de backup ele deve copiar. 
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)#copiar a arvore de arquivos
    