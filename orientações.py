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

        Resultados_dissertacao_mestrado = []
        Resultados_tese_doutorado = []
        Resultados_Trabalho_de_conclusão = []
        Resultados_Iniciação_científica = []
        Resultados_Supervisão_de_pós_doutorado = []
        Resultados_Monografia = []
        Resultados_dissertacao_mestrado_2 = []
        Resultados_tese_doutorado_2 = []
        Resultados_Trabalho_de_conclusão_2 = []
        Resultados_Iniciação_científica_2 = []
        Resultados_Supervisão_de_pós_doutorado_2 = []
        Resultados_Monografia_2 = []

        for inst_back in inst_back_list:
            tag_b = inst_back.find('b')
            if tag_b:
                texto_inst_back = tag_b.get_text(strip=True)

                if "Orientações e supervisões em andamento" in texto_inst_back: 
                    
                    cita_artigos_list = inst_back.find_next_siblings('div', class_='cita-artigos')

                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Dissertação de mestrado' in tag_b.get_text(strip=True):
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
                                                Resultados_dissertacao_mestrado.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')

                    ###########################################   Tese de doutorado          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Tese de doutorado' in tag_b.get_text(strip=True):
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
                                                Resultados_tese_doutorado.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')

                    
                    ###########################################   Trabalho de conclusão de curso de graduação          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Trabalho de conclusão de curso de graduação' in tag_b.get_text(strip=True):
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
                                                Resultados_Trabalho_de_conclusão.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')
                    
                    ###########################################   Iniciação científica          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Iniciação científica' in tag_b.get_text(strip=True):
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
                                                Resultados_Iniciação_científica.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')

                    ###########################################   Monografia de conclusão de curso de aperfeiçoamento/especialização          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Monografia de conclusão de curso de aperfeiçoamento/especialização' in tag_b.get_text(strip=True):
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
                                                Resultados_Monografia.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')

                    ###########################################   Supervisão de pós-doutorado          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Supervisão de pós-doutorado' in tag_b.get_text(strip=True):
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
                                                Resultados_Supervisão_de_pós_doutorado.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')
                
                
                elif "Orientações e supervisões concluídas" in texto_inst_back:

                    cita_artigos_list = inst_back.find_next_siblings('div', class_='cita-artigos')

                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Dissertação de mestrado' in tag_b.get_text(strip=True):
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
                                                Resultados_dissertacao_mestrado_2.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')

                    ###########################################   Tese de doutorado          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Tese de doutorado' in tag_b.get_text(strip=True):
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
                                                Resultados_tese_doutorado_2.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')

                    
                    ###########################################   Trabalho de conclusão de curso de graduação          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Trabalho de conclusão de curso de graduação' in tag_b.get_text(strip=True):
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
                                                Resultados_Trabalho_de_conclusão_2.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')
                    
                    ###########################################   Iniciação científica          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Iniciação científica' in tag_b.get_text(strip=True):
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
                                                Resultados_Iniciação_científica_2.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11')
        
                    ###########################################   Monografia de conclusão de curso de aperfeiçoamento/especialização          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Monografia de conclusão de curso de aperfeiçoamento/especialização' in tag_b.get_text(strip=True):
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
                                                Resultados_Monografia_2.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11') 
                    
                    ###########################################   Supervisão de pós-doutorado          
            
                    for cita_artigos in cita_artigos_list:
                        tag_b = cita_artigos.find('b')

                        # Verifica se a tag_b contém o texto desejado
                        if tag_b and 'Supervisão de pós-doutorado' in tag_b.get_text(strip=True):
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
                                                Resultados_Supervisão_de_pós_doutorado_2.append((nome_completo, ano, texto_span))
                                                #print("Ano:", ano, "Informações:", texto_span)

                                # Move para o próximo layout-cell-11
                                layout = layout.find_next('div', class_='layout-cell-11') 

                                
        return Resultados_dissertacao_mestrado ,Resultados_tese_doutorado ,Resultados_Trabalho_de_conclusão ,Resultados_Iniciação_científica ,Resultados_Supervisão_de_pós_doutorado ,Resultados_Monografia ,Resultados_dissertacao_mestrado_2 ,Resultados_tese_doutorado_2 ,Resultados_Trabalho_de_conclusão_2 ,Resultados_Iniciação_científica_2 ,Resultados_Supervisão_de_pós_doutorado_2 ,Resultados_Monografia_2
    
    
    except FileNotFoundError:
        print(f"O arquivo {arquivo_html} não foi encontrado.")
    except ValueError:
        print(f"Erro ao converter o ano para inteiro no arquivo {arquivo_html}.")
    except Exception as e:
        print(f"Ocorreu um erro no arquivo {arquivo_html}: {e}")
        return [], [], [], [], [], [], [], []
    


todos_resultados_dissertacao_mestrado = []
todos_resultados_tese_doutorado = []
todos_resultados_Trabalho_de_conclusao = []
todos_resultados_Iniciacao_cientifica = []
todos_resultados_Supervisao_de_pos_doutorado = []
todos_resultados_Monografia = []
todos_resultados_dissertacao_mestrado_2 = []
todos_resultados_tese_doutorado_2 = []
todos_resultados_Trabalho_de_conclusao_2 = []
todos_resultados_Iniciacao_cientifica_2 = []
todos_resultados_Supervisao_de_pos_doutorado_2 = []
todos_resultados_Monografia_2 = []



for html_file in os.listdir("data"):
    if html_file.endswith(".html"):
        html_path = os.path.join("data", html_file)

        # Chamada para a função com os novos resultados
        resultados_dissertacao_mestrado, resultados_tese_doutorado, resultados_Trabalho_de_conclusao, resultados_Iniciacao_cientifica, resultados_Supervisao_de_pos_doutorado, resultados_Monografia, resultados_dissertacao_mestrado_2, resultados_tese_doutorado_2, resultados_Trabalho_de_conclusao_2, resultados_Iniciacao_cientifica_2, resultados_Supervisao_de_pos_doutorado_2, resultados_Monografia_2 = processar_arquivo(html_path)

        # Extensão das listas com os resultados obtidos
        todos_resultados_dissertacao_mestrado.extend(resultados_dissertacao_mestrado)
        todos_resultados_tese_doutorado.extend(resultados_tese_doutorado)
        todos_resultados_Trabalho_de_conclusao.extend(resultados_Trabalho_de_conclusao)
        todos_resultados_Iniciacao_cientifica.extend(resultados_Iniciacao_cientifica)
        todos_resultados_Supervisao_de_pos_doutorado.extend(resultados_Supervisao_de_pos_doutorado)
        todos_resultados_Monografia.extend(resultados_Monografia)
        todos_resultados_dissertacao_mestrado_2.extend(resultados_dissertacao_mestrado_2)
        todos_resultados_tese_doutorado_2.extend(resultados_tese_doutorado_2)
        todos_resultados_Trabalho_de_conclusao_2.extend(resultados_Trabalho_de_conclusao_2)
        todos_resultados_Iniciacao_cientifica_2.extend(resultados_Iniciacao_cientifica_2)
        todos_resultados_Supervisao_de_pos_doutorado_2.extend(resultados_Supervisao_de_pos_doutorado_2)
        todos_resultados_Monografia_2.extend(resultados_Monografia_2)


df_dissertacao_mestrado = pd.DataFrame(todos_resultados_dissertacao_mestrado, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_tese_doutorado = pd.DataFrame(todos_resultados_tese_doutorado, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Trabalho_de_conclusao = pd.DataFrame(todos_resultados_Trabalho_de_conclusao, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Iniciacao_cientifica = pd.DataFrame(todos_resultados_Iniciacao_cientifica, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Supervisao_de_pos_doutorado = pd.DataFrame(todos_resultados_Supervisao_de_pos_doutorado, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Monografia = pd.DataFrame(todos_resultados_Monografia, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_dissertacao_mestrado_2 = pd.DataFrame(todos_resultados_dissertacao_mestrado_2, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_tese_doutorado_2 = pd.DataFrame(todos_resultados_tese_doutorado_2, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Trabalho_de_conclusao_2 = pd.DataFrame(todos_resultados_Trabalho_de_conclusao_2, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Iniciacao_cientifica_2 = pd.DataFrame(todos_resultados_Iniciacao_cientifica_2, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Supervisao_de_pos_doutorado_2 = pd.DataFrame(todos_resultados_Supervisao_de_pos_doutorado_2, columns=["Nome Completo", "Ano", "Informações Gerais"])
df_Monografia_2 = pd.DataFrame(todos_resultados_Monografia_2, columns=["Nome Completo", "Ano", "Informações Gerais"])

df_dissertacao_mestrado = df_dissertacao_mestrado.drop_duplicates()
df_tese_doutorado = df_tese_doutorado.drop_duplicates()
df_Trabalho_de_conclusao = df_Trabalho_de_conclusao.drop_duplicates()
df_Iniciacao_cientifica = df_Iniciacao_cientifica.drop_duplicates()
df_Supervisao_de_pos_doutorado = df_Supervisao_de_pos_doutorado.drop_duplicates()
df_Monografia = df_Monografia.drop_duplicates()
df_dissertacao_mestrado_2 = df_dissertacao_mestrado_2.drop_duplicates()
df_tese_doutorado_2 = df_tese_doutorado_2.drop_duplicates()
df_Trabalho_de_conclusao_2 = df_Trabalho_de_conclusao_2.drop_duplicates()
df_Iniciacao_cientifica_2 = df_Iniciacao_cientifica_2.drop_duplicates()
df_Supervisao_de_pos_doutorado_2 = df_Supervisao_de_pos_doutorado_2.drop_duplicates()
df_Monografia_2 = df_Monografia_2.drop_duplicates()

with pd.ExcelWriter('orientações.xlsx') as writer:
    df_dissertacao_mestrado.to_excel(writer, sheet_name='Dissertações de Mestrado - andamento', index=False)
    df_tese_doutorado.to_excel(writer, sheet_name='Teses de Doutorado - andamento', index=False)
    df_Trabalho_de_conclusao.to_excel(writer, sheet_name='Trabalhos de Conclusão - andamento', index=False)
    df_Iniciacao_cientifica.to_excel(writer, sheet_name='Iniciação Científica - andamento', index=False)
    df_Supervisao_de_pos_doutorado.to_excel(writer, sheet_name='Supervisão de Pós-Doutorado - andamento', index=False)
    df_Monografia.to_excel(writer, sheet_name='Monografias - andamento', index=False)
    df_dissertacao_mestrado_2.to_excel(writer, sheet_name='Dissertações de Mestrado - Concluida', index=False)
    df_tese_doutorado_2.to_excel(writer, sheet_name='Teses de Doutorado - Concluida', index=False)
    df_Trabalho_de_conclusao_2.to_excel(writer, sheet_name='Trabalhos de Conclusão - Concluida', index=False)
    df_Iniciacao_cientifica_2.to_excel(writer, sheet_name='Iniciação Científica - Concluida', index=False)
    df_Supervisao_de_pos_doutorado_2.to_excel(writer, sheet_name='Supervisão de Pós-Doutorado - Concluida', index=False)
    df_Monografia_2.to_excel(writer, sheet_name='Monografias - Concluida', index=False)


