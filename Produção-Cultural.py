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



        cita_artigos_list = soup.find_all('div', class_='cita-artigos')

        resultados_Cultural = []
        resultados_Artes_Visuais = []
        resultados_outras = []
        resultados_musica = []
        resultados_Artes_Cênicas = []


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Outras produções artísticas/culturais' in tag_b.get_text(strip=True):
                #print("Texto encontrado:", tag_b.get_text(strip=True))

                # Encontrar todos os 'layout-cell-11' após a div atual, antes da próxima 'cita-artigos'
                proximo_cita_artigos = cita_artigos.find_next('div', class_='cita-artigos')
                
                # Loop por todos os 'layout-cell-11' até encontrar a próxima div 'cita-artigos'
                layout = cita_artigos.find_next('div', class_='layout-cell-11')
                while layout and (proximo_cita_artigos is None or layout.sourceline < proximo_cita_artigos.sourceline):
                    span_transform = layout.find('span', class_='transform')
                    if span_transform:
                        texto_span = span_transform.get_text(strip=True)

                        # Verifica se há um ano no texto
                        for ano in range(1900, 2100):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_Cultural.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


        
        #####################################   Artes Visuais
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Artes Visuais' in tag_b.get_text(strip=True):
                #print("Texto encontrado:", tag_b.get_text(strip=True))

                # Encontrar todos os 'layout-cell-11' após a div atual, antes da próxima 'cita-artigos'
                proximo_cita_artigos = cita_artigos.find_next('div', class_='cita-artigos')
                
                # Loop por todos os 'layout-cell-11' até encontrar a próxima div 'cita-artigos'
                layout = cita_artigos.find_next('div', class_='layout-cell-11')
                while layout and (proximo_cita_artigos is None or layout.sourceline < proximo_cita_artigos.sourceline):
                    span_transform = layout.find('span', class_='transform')
                    if span_transform:
                        texto_span = span_transform.get_text(strip=True)

                        # Verifica se há um ano no texto
                        for ano in range(1900, 2100):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_Artes_Visuais.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        #####################################   Outras produções artísticas/culturais
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Outras produções artísticas/culturais' in tag_b.get_text(strip=True):
                #print("Texto encontrado:", tag_b.get_text(strip=True))

                # Encontrar todos os 'layout-cell-11' após a div atual, antes da próxima 'cita-artigos'
                proximo_cita_artigos = cita_artigos.find_next('div', class_='cita-artigos')
                
                # Loop por todos os 'layout-cell-11' até encontrar a próxima div 'cita-artigos'
                layout = cita_artigos.find_next('div', class_='layout-cell-11')
                while layout and (proximo_cita_artigos is None or layout.sourceline < proximo_cita_artigos.sourceline):
                    span_transform = layout.find('span', class_='transform')
                    if span_transform:
                        texto_span = span_transform.get_text(strip=True)

                        # Verifica se há um ano no texto
                        for ano in range(1900, 2100):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_outras.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        #####################################   Música
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Música' in tag_b.get_text(strip=True):
                #print("Texto encontrado:", tag_b.get_text(strip=True))

                # Encontrar todos os 'layout-cell-11' após a div atual, antes da próxima 'cita-artigos'
                proximo_cita_artigos = cita_artigos.find_next('div', class_='cita-artigos')
                
                # Loop por todos os 'layout-cell-11' até encontrar a próxima div 'cita-artigos'
                layout = cita_artigos.find_next('div', class_='layout-cell-11')
                while layout and (proximo_cita_artigos is None or layout.sourceline < proximo_cita_artigos.sourceline):
                    span_transform = layout.find('span', class_='transform')
                    if span_transform:
                        texto_span = span_transform.get_text(strip=True)

                        # Verifica se há um ano no texto
                        for ano in range(1900, 2100):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_musica.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        #####################################   Música
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Artes Cênicas' in tag_b.get_text(strip=True):
                #print("Texto encontrado:", tag_b.get_text(strip=True))

                # Encontrar todos os 'layout-cell-11' após a div atual, antes da próxima 'cita-artigos'
                proximo_cita_artigos = cita_artigos.find_next('div', class_='cita-artigos')
                
                # Loop por todos os 'layout-cell-11' até encontrar a próxima div 'cita-artigos'
                layout = cita_artigos.find_next('div', class_='layout-cell-11')
                while layout and (proximo_cita_artigos is None or layout.sourceline < proximo_cita_artigos.sourceline):
                    span_transform = layout.find('span', class_='transform')
                    if span_transform:
                        texto_span = span_transform.get_text(strip=True)

                        # Verifica se há um ano no texto
                        for ano in range(1900, 2100):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_Artes_Cênicas.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')
    
        return resultados_Artes_Visuais, resultados_Cultural, resultados_musica, resultados_outras,resultados_Artes_Cênicas
    
    except FileNotFoundError:
        print(f"O arquivo {arquivo_html} não foi encontrado.")
    except ValueError:
        print(f"Erro ao converter o ano para inteiro no arquivo {arquivo_html}.")
    except Exception as e:
        print(f"Ocorreu um erro no arquivo {arquivo_html}: {e}")
        return [], [], [], [], [], [], [], []




todos_resultados_Artes_Visuais = []
todos_resultados_Cultural = []
todos_resultados_musica = []
todos_resultados_outras = []
todos_resultados_Artes_Cênicas =[]


for html_file in os.listdir("data"):
    if html_file.endswith(".html"):
        html_path = os.path.join("data", html_file)
        # Separando os resultados relacionados a Artes e Cultura
        resultados_Artes_Visuais, resultados_Cultural, resultados_musica, resultados_outras, resultados_Artes_Cênicas = processar_arquivo(html_path)
        todos_resultados_Artes_Visuais.extend(resultados_Artes_Visuais)
        todos_resultados_Cultural.extend(resultados_Cultural)
        todos_resultados_musica.extend(resultados_musica)
        todos_resultados_outras.extend(resultados_outras)
        todos_resultados_Artes_Cênicas.extend(resultados_Artes_Cênicas)


df_Artes_Visuais = pd.DataFrame(todos_resultados_Artes_Visuais, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Cultural = pd.DataFrame(todos_resultados_Cultural, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_musica = pd.DataFrame(todos_resultados_musica, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_outras = pd.DataFrame(todos_resultados_outras, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Artes_Cênicas = pd.DataFrame(todos_resultados_Artes_Cênicas, columns=["Nome Completo", "Ano", "Informações Gerais"])


df_Artes_Visuais = df_Artes_Visuais.drop_duplicates()
df_Cultural = df_Cultural.drop_duplicates()
df_musica = df_musica.drop_duplicates()
df_outras = df_outras.drop_duplicates()
df_Artes_Cênicas= df_Artes_Cênicas.drop_duplicates()

with pd.ExcelWriter('Producao_cultural.xlsx') as writer:
    df_Artes_Visuais.to_excel(writer, sheet_name='Artes Visuais', index=False)
    df_Cultural.to_excel(writer, sheet_name='Cultura', index=False)
    df_musica.to_excel(writer, sheet_name='Música', index=False)
    df_outras.to_excel(writer, sheet_name='Outras', index=False)
    df_Artes_Cênicas.to_excel(writer, sheet_name='Artes Cênicas', index=False)