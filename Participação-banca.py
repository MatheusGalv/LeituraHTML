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

        Resultados_Banca_Conclusão_Mestrado = []
        Resultados_Banca_Conclusão_Teses_de_doutorado = []
        Resultados_Banca_Conclusão_Qualificações_de_Doutorado = []
        Resultados_Banca_Conclusão_Qualificações_de_Mestrado = []
        Resultados_Banca_Conclusão_Trabalho_graduacao = []
        Resultados_Banca_Conclusão_Outros_tipos = []
        Resultados_Banca_Julgadora_concurso = []
        Resultados_Banca_Julgadora_Outras_participacoes = []
        Resultados_Banca_Julgadora_Professor_titular = []
        Resultados_Banca_Julgadora_Livre_docência = []
        
        


        ######################################### Mestrado 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Mestrado' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Conclusão_Mestrado.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        

        ######################################### Teses de doutorado 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Teses de doutorado' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Conclusão_Teses_de_doutorado.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')
        


        ######################################### Qualificações de Doutorado 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Qualificações de Doutorado' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Conclusão_Qualificações_de_Doutorado.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        ######################################### Qualificações de Mestrado 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Qualificações de Mestrado' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Conclusão_Qualificações_de_Mestrado.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        ######################################### Trabalhos de conclusão de curso de graduação 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Trabalhos de conclusão de curso de graduação' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Conclusão_Trabalho_graduacao.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        ######################################### Outros tipos 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Outros tipos' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Conclusão_Outros_tipos.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')
        
        ######################################### Concurso público 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Concurso público' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Julgadora_concurso.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')
        
        ######################################### Outras participações 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Outras participações' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Julgadora_Outras_participacoes.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        ######################################### Professor titular 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Professor titular' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Julgadora_Professor_titular.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        ######################################### Livre docência 
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Livre docência' in tag_b.get_text(strip=True):
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
                                    Resultados_Banca_Julgadora_Livre_docência.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')

        return Resultados_Banca_Conclusão_Mestrado , Resultados_Banca_Conclusão_Teses_de_doutorado ,Resultados_Banca_Conclusão_Qualificações_de_Doutorado ,Resultados_Banca_Conclusão_Qualificações_de_Mestrado ,Resultados_Banca_Conclusão_Trabalho_graduacao ,Resultados_Banca_Conclusão_Outros_tipos ,Resultados_Banca_Julgadora_concurso ,Resultados_Banca_Julgadora_Outras_participacoes ,Resultados_Banca_Julgadora_Professor_titular ,Resultados_Banca_Julgadora_Livre_docência

    except FileNotFoundError:
        print(f"O arquivo {arquivo_html} não foi encontrado.")
    except ValueError:
        print(f"Erro ao converter o ano para inteiro no arquivo {arquivo_html}.")
    except Exception as e:
        print(f"Ocorreu um erro no arquivo {arquivo_html}: {e}")
        return [], [], [], [], [], [], [], []
    
todos_resultados_Banca_Conclusão_Mestrado = []
todos_resultados_Banca_Conclusão_Teses_de_doutorado = []
todos_resultados_Banca_Conclusão_Qualificações_de_Doutorado = []
todos_resultados_Banca_Conclusão_Qualificações_de_Mestrado = []
todos_resultados_Banca_Conclusão_Trabalho_graduacao = []
todos_resultados_Banca_Conclusão_Outros_tipos = []
todos_resultados_Banca_Julgadora_concurso = []
todos_resultados_Banca_Julgadora_Outras_participacoes = []
todos_resultados_Banca_Julgadora_Professor_titular = []
todos_resultados_Banca_Julgadora_Livre_docência = []


for html_file in os.listdir("data"):
    if html_file.endswith(".html"):
        html_path = os.path.join("data", html_file)
        resultados_Banca_Conclusão_Mestrado, resultados_Banca_Conclusão_Teses_de_doutorado, resultados_Banca_Conclusão_Qualificações_de_Doutorado, resultados_Banca_Conclusão_Qualificações_de_Mestrado, resultados_Banca_Conclusão_Trabalho_graduacao, resultados_Banca_Conclusão_Outros_tipos, resultados_Banca_Julgadora_concurso, resultados_Banca_Julgadora_Outras_participacoes, resultados_Banca_Julgadora_Professor_titular, resultados_Banca_Julgadora_Livre_docência = processar_arquivo(html_path)

        todos_resultados_Banca_Conclusão_Mestrado.extend(resultados_Banca_Conclusão_Mestrado)
        todos_resultados_Banca_Conclusão_Teses_de_doutorado.extend(resultados_Banca_Conclusão_Teses_de_doutorado)
        todos_resultados_Banca_Conclusão_Qualificações_de_Doutorado.extend(resultados_Banca_Conclusão_Qualificações_de_Doutorado)
        todos_resultados_Banca_Conclusão_Qualificações_de_Mestrado.extend(resultados_Banca_Conclusão_Qualificações_de_Mestrado)
        todos_resultados_Banca_Conclusão_Trabalho_graduacao.extend(resultados_Banca_Conclusão_Trabalho_graduacao)
        todos_resultados_Banca_Conclusão_Outros_tipos.extend(resultados_Banca_Conclusão_Outros_tipos)
        todos_resultados_Banca_Julgadora_concurso.extend(resultados_Banca_Julgadora_concurso)
        todos_resultados_Banca_Julgadora_Outras_participacoes.extend(resultados_Banca_Julgadora_Outras_participacoes)
        todos_resultados_Banca_Julgadora_Professor_titular.extend(resultados_Banca_Julgadora_Professor_titular)
        todos_resultados_Banca_Julgadora_Livre_docência.extend(resultados_Banca_Julgadora_Livre_docência)


df_Banca_Conclusão_Mestrado = pd.DataFrame(todos_resultados_Banca_Conclusão_Mestrado, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Conclusão_Teses_de_doutorado = pd.DataFrame(todos_resultados_Banca_Conclusão_Teses_de_doutorado, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Conclusão_Qualificações_de_Doutorado = pd.DataFrame(todos_resultados_Banca_Conclusão_Qualificações_de_Doutorado, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Conclusão_Qualificações_de_Mestrado = pd.DataFrame(todos_resultados_Banca_Conclusão_Qualificações_de_Mestrado, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Conclusão_Trabalho_graduacao = pd.DataFrame(todos_resultados_Banca_Conclusão_Trabalho_graduacao, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Conclusão_Outros_tipos = pd.DataFrame(todos_resultados_Banca_Conclusão_Outros_tipos, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Julgadora_concurso = pd.DataFrame(todos_resultados_Banca_Julgadora_concurso, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Julgadora_Outras_participacoes = pd.DataFrame(todos_resultados_Banca_Julgadora_Outras_participacoes, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Julgadora_Professor_titular = pd.DataFrame(todos_resultados_Banca_Julgadora_Professor_titular, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Banca_Julgadora_Livre_docência = pd.DataFrame(todos_resultados_Banca_Julgadora_Livre_docência, columns=["Nome Completo", "Ano", "Informações Gerais"])


df_Banca_Conclusão_Mestrado = df_Banca_Conclusão_Mestrado.drop_duplicates()
df_Banca_Conclusão_Teses_de_doutorado = df_Banca_Conclusão_Teses_de_doutorado.drop_duplicates()
df_Banca_Conclusão_Qualificações_de_Doutorado = df_Banca_Conclusão_Qualificações_de_Doutorado.drop_duplicates()
df_Banca_Conclusão_Qualificações_de_Mestrado = df_Banca_Conclusão_Qualificações_de_Mestrado.drop_duplicates()
df_Banca_Conclusão_Trabalho_graduacao = df_Banca_Conclusão_Trabalho_graduacao.drop_duplicates()
df_Banca_Conclusão_Outros_tipos = df_Banca_Conclusão_Outros_tipos.drop_duplicates()
df_Banca_Julgadora_concurso = df_Banca_Julgadora_concurso.drop_duplicates()
df_Banca_Julgadora_Outras_participacoes = df_Banca_Julgadora_Outras_participacoes.drop_duplicates()
df_Banca_Julgadora_Professor_titular = df_Banca_Julgadora_Professor_titular.drop_duplicates()
df_Banca_Julgadora_Livre_docência = df_Banca_Julgadora_Livre_docência.drop_duplicates()


with pd.ExcelWriter('Bancas.xlsx') as writer:
    df_Banca_Conclusão_Mestrado.to_excel(writer, sheet_name='Banca de Conclusão de Mestrado', index=False)
    df_Banca_Conclusão_Teses_de_doutorado.to_excel(writer, sheet_name='Banca de Conclusão de Teses', index=False)
    df_Banca_Conclusão_Qualificações_de_Doutorado.to_excel(writer, sheet_name='Qualificações de Doutorado', index=False)
    df_Banca_Conclusão_Qualificações_de_Mestrado.to_excel(writer, sheet_name='Qualificações de Mestrado', index=False)
    df_Banca_Conclusão_Trabalho_graduacao.to_excel(writer, sheet_name='Trabalho de Graduação', index=False)
    df_Banca_Conclusão_Outros_tipos.to_excel(writer, sheet_name='Outros Tipos', index=False)
    df_Banca_Julgadora_concurso.to_excel(writer, sheet_name='Julgadora de Concurso', index=False)
    df_Banca_Julgadora_Outras_participacoes.to_excel(writer, sheet_name='Outras Participações', index=False)
    df_Banca_Julgadora_Professor_titular.to_excel(writer, sheet_name='Professor Titular', index=False)
    df_Banca_Julgadora_Livre_docência.to_excel(writer, sheet_name='Livre Docência', index=False)

