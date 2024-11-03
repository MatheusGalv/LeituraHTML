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

        resultados_trabalho = []
        resultados_acessoria = []
        resultados_programa = []
        resultados_midia = []
        resultados_outra = []
        resultados_demais_trabalho = []
        resultados_computador = []
        resultados_produto_tecnologico= []


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Trabalhos técnicos' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_trabalho.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


    ############################### Entrevistas, mesas redondas, programas e comentários na mídia


            # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Entrevistas, mesas redondas, programas e comentários na mídia' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_programa.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')
    

    ############################### Redes sociais, websites e blogs


            # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Redes sociais, websites e blogs' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_midia.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


        ############################### Demais tipos de produção técnica


            # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Demais tipos de produção técnica' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_outra.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


        ############################### Assessoria e consultoria


            # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Assessoria e consultoria' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_acessoria.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

    ############################### Demais trabalhos


            # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Demais trabalhos' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_demais_trabalho.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        ############################### Programas de computador sem registro


            # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Programas de computador sem registro' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_computador.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        
        ############################### Produtos tecnológicos


            # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Produtos tecnológicos' in tag_b.get_text(strip=True):
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
                        for ano in range(1900, 2026):  # Anos de 1900 a 2099
                            if str(ano) in texto_span:
                                if ano >= 2021:  # Verifica se o ano é >= 2021
                                    # Armazena o ano e o texto_span como tupla
                                    resultados_produto_tecnologico.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        return resultados_trabalho , resultados_acessoria, resultados_computador, resultados_demais_trabalho, resultados_midia, resultados_outra, resultados_programa ,resultados_produto_tecnologico      

    except FileNotFoundError:
        print(f"O arquivo {arquivo_html} não foi encontrado.")
    except ValueError:
        print(f"Erro ao converter o ano para inteiro no arquivo {arquivo_html}.")
    except Exception as e:
        print(f"Ocorreu um erro no arquivo {arquivo_html}: {e}")
        return [], [], [], [], [], [], [], []




todos_resultados_trabalho = []
todos_resultados_acessoria = []
todos_resultados_computador = []
todos_resultados_demais_trabalho = []
todos_resultados_midia = []
todos_resultados_outra = []
todos_resultados_programa = []
todos_resultados_produto_tecnologico = []


for html_file in os.listdir("data"):
    if html_file.endswith(".html"):
        html_path = os.path.join("data", html_file)
        resultados_trabalho, resultados_acessoria, resultados_computador, resultados_demais_trabalho, resultados_midia, resultados_outra, resultados_programa,resultados_produto_tecnologico = processar_arquivo(html_path)
        todos_resultados_trabalho.extend(resultados_trabalho)
        todos_resultados_acessoria.extend(resultados_acessoria)
        todos_resultados_computador.extend(resultados_computador)
        todos_resultados_demais_trabalho.extend(resultados_demais_trabalho)
        todos_resultados_midia.extend(resultados_midia)
        todos_resultados_outra.extend(resultados_outra)
        todos_resultados_programa.extend(resultados_programa)
        todos_resultados_produto_tecnologico.extend(resultados_produto_tecnologico)


df_trabalho = pd.DataFrame(todos_resultados_trabalho, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_acessoria = pd.DataFrame(todos_resultados_acessoria, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_computador = pd.DataFrame(todos_resultados_computador, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_demais_trabalho = pd.DataFrame(todos_resultados_demais_trabalho, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_midia = pd.DataFrame(todos_resultados_midia, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_outra = pd.DataFrame(todos_resultados_outra, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_programa = pd.DataFrame(todos_resultados_programa, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_produto_tecnologico= pd.DataFrame(todos_resultados_produto_tecnologico, columns=["Nome Completo", "Ano", "Informações Gerais"])

df_trabalho = df_trabalho.drop_duplicates()
df_acessoria = df_acessoria.drop_duplicates()
df_computador = df_computador.drop_duplicates()
df_demais_trabalho = df_demais_trabalho.drop_duplicates()
df_midia = df_midia.drop_duplicates()
df_outra = df_outra.drop_duplicates()
df_programa = df_programa.drop_duplicates()
df_produto_tecnologico = df_produto_tecnologico.drop_duplicates()


with pd.ExcelWriter('Producao_tecnica.xlsx') as writer:
    df_trabalho.to_excel(writer, sheet_name='Trabalhos tecnicos', index=False)
    df_acessoria.to_excel(writer, sheet_name='Acessoria', index=False)
    df_computador.to_excel(writer, sheet_name='Programas de computador sem registro', index=False)
    df_demais_trabalho.to_excel(writer, sheet_name='Demais Trabalhos', index=False)
    df_midia.to_excel(writer, sheet_name='Mídia', index=False)
    df_outra.to_excel(writer, sheet_name='Outras Produções', index=False)
    df_programa.to_excel(writer, sheet_name='Programas', index=False)
    df_produto_tecnologico.to_excel(writer,sheet_name='Produto tecnologico')