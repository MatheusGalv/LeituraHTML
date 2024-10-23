from bs4 import BeautifulSoup
from unidecode import unidecode
import re
import pandas as pd
import os
from urllib.parse import urlparse, parse_qs


def processar_arquivo(arquivo_html):
    try:
        # Tentar abrir o arquivo com a codificação 'latin-1' (ISO-8859-1)
        with open(arquivo_html, 'r', encoding='ISO-8859-1') as file:
            content = file.read().encode('latin-1').decode('utf-8')

        # Criando o objeto BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Extraindo o texto da tag h2 com a classe 'nome'
        nome_completo = soup.find('h2', class_='nome').text if soup.find('h2', class_='nome') else None
        print(nome_completo)



        inst_back_list = soup.find_all('div', class_='inst_back')

        Resultados_Participacao_evento = []
        Resultados_organizacao_evento = []


         ######################################### Participação em eventos, congressos, exposições e feiras 
        for inst_back in inst_back_list:
            tag_b = inst_back.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Participação em eventos, congressos, exposições e feiras' in tag_b.get_text(strip=True):
                #print("Texto encontrado:", tag_b.get_text(strip=True))

                # Encontrar todos os 'layout-cell-11' após a div atual, antes da próxima 'cita-artigos'
                proximo_inst_back = inst_back.find_next('div', class_='cita-artigos')
                
                # Loop por todos os 'layout-cell-11' até encontrar a próxima div 'cita-artigos'
                layout = inst_back.find_next('div', class_='layout-cell-11')
                while layout and (proximo_inst_back is None or layout.sourceline < proximo_inst_back.sourceline):
                    span_transform = layout.find('span', class_='transform')
                    if span_transform:
                        texto_span = span_transform.get_text(strip=True)

                        # Verifica se há um ano no texto
                        for ano in range(1900, 2100):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    Resultados_Participacao_evento.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        ######################################### Organização de eventos, congressos, exposições e feiras 
        for inst_back in inst_back_list:
            tag_b = inst_back.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Organização de eventos, congressos, exposições e feiras' in tag_b.get_text(strip=True):
                #print("Texto encontrado:", tag_b.get_text(strip=True))

                # Encontrar todos os 'layout-cell-11' após a div atual, antes da próxima 'cita-artigos'
                proximo_inst_back = inst_back.find_next('div', class_='cita-artigos')
                
                # Loop por todos os 'layout-cell-11' até encontrar a próxima div 'cita-artigos'
                layout = inst_back.find_next('div', class_='layout-cell-11')
                while layout and (proximo_inst_back is None or layout.sourceline < proximo_inst_back.sourceline):
                    span_transform = layout.find('span', class_='transform')
                    if span_transform:
                        texto_span = span_transform.get_text(strip=True)

                        # Verifica se há um ano no texto
                        for ano in range(1900, 2100):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    Resultados_organizacao_evento.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        return Resultados_organizacao_evento,Resultados_Participacao_evento
    
    except FileNotFoundError:
        print(f"O arquivo {arquivo_html} não foi encontrado.")
    except ValueError:
        print(f"Erro ao converter o ano para inteiro no arquivo {arquivo_html}.")
    except Exception as e:
        print(f"Ocorreu um erro no arquivo {arquivo_html}: {e}")
        return [], [], [], [], [], [], [], []
    
# Definindo listas para armazenar resultados
todos_resultados_organizacao_evento = []
todos_resultados_participacao_evento = []

# Processando arquivos HTML
for html_file in os.listdir("data"):
    if html_file.endswith(".html"):
        html_path = os.path.join("data", html_file)

        # Chamando a função para obter os resultados
        resultados_organizacao_evento, resultados_participacao_evento = processar_arquivo(html_path)

        # Adicionando resultados às listas
        todos_resultados_organizacao_evento.extend(resultados_organizacao_evento)
        todos_resultados_participacao_evento.extend(resultados_participacao_evento)

# Criando DataFrames
df_organizacao_evento = pd.DataFrame(todos_resultados_organizacao_evento, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_participacao_evento = pd.DataFrame(todos_resultados_participacao_evento, columns=["Nome Completo", "Ano", "Informações Gerais"])

# Removendo duplicatas
df_organizacao_evento = df_organizacao_evento.drop_duplicates()
df_participacao_evento = df_participacao_evento.drop_duplicates()

# Salvando em um arquivo Excel
with pd.ExcelWriter('Eventos.xlsx') as writer:
    df_organizacao_evento.to_excel(writer, sheet_name='Organização de Eventos', index=False)
    df_participacao_evento.to_excel(writer, sheet_name='Participação em Eventos', index=False)
