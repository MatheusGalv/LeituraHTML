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

        artigos_completos = soup.find_all('div', class_='artigo-completo')
        cita_artigos_list = soup.find_all('div', class_='cita-artigos')

        resultados_trabalho = []
        resultados_APStrabalho = []
        resultados_artigo = []
        resultados_artigoaceitos =[]
        resultados_livros = []
        resultados_capitulos = []
        resultados_jornais = []
        resultados_demais = []
        resultados_ResumoExp = []
        resultados_Resumo = []
        #resultados_prefacio = []
        #resultados_traducao = []



        for artigo in artigos_completos:
            # Extraindo o ano
            ano = artigo.find('span', {'data-tipo-ordenacao': 'ano'})
            ano_texto = ano.text if ano else None
            
            # Verificando se o ano é válido e maior ou igual a 2021
            if ano_texto and int(ano_texto) >= 2021:
                # Extraindo o título do artigo
                Informações_artigo = artigo.get_text(separator=' ', strip=True)

                
                # Extraindo o DOI, se disponível
                link_doi = artigo.find('a', class_='icone-producao icone-doi')
                Link_artigo = link_doi['href'] if link_doi else None
                
                # Extraindo os autores
                autores_element = artigo.find('span', {'data-tipo-ordenacao': 'autor'})
                autores = autores_element.text if autores_element else None

                # Encontrar a tag <span> com a classe "citado"
                span_tag = artigo.find('span', class_='citado')

                cvuri = span_tag['cvuri'] if span_tag else None

                if cvuri:  # Verifica se cvuri não é None
                    # Analisar a URL para extrair os parâmetros
                    parsed_url = urlparse(cvuri)
                    params = parse_qs(parsed_url.query)

                    # Criar o dicionário de parâmetros
                    params_dict = {key: values[0] for key, values in params.items()}

                    volume = params_dict.get('volume')
                    pagina_inicial = params_dict.get('paginaInicial')

                    # Imprimindo os valores extraídos
                    #print(f"Ano: {ano_texto}")
                    #print(f"Título do Artigo: {Informações_artigo}")
                    #print(f"DOI: {Link_artigo}")
                    #print(f"Autores: {autores}")
                    #print(f"Volume: {volume}")
                    #print(f"Página Inicial: {pagina_inicial}")
                    #print("--------------------------------------------------")
                # Adicionando os dados extraídos à lista de resultados
                resultados_artigo.append(
                (nome_completo,ano_texto, Informações_artigo, Link_artigo, autores, volume, pagina_inicial)
                )




        ########################## livro




        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Livros publicados/organizados ou edições' in tag_b.get_text(strip=True):
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
                                    resultados_livros.append((nome_completo,ano, texto_span))
                                    #print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')



        ###################### Capitulos


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Capítulos de livros publicados' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                    resultados_capitulos.append((nome_completo,ano, texto_span))
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


        ###################### jornais


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Textos em jornais de notícias/revistas' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                    resultados_jornais.append((nome_completo,ano, texto_span))
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')



        ###################### Trabalho


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Trabalhos completos publicados em anais de congressos' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')



        ###################### Resumos expandidos


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Resumos expandidos publicados em anais de congressos' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                    resultados_ResumoExp.append((nome_completo,ano, texto_span))
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')




        ###################### Resumos 


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Resumos publicados em anais de congressos' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                    resultados_Resumo.append((nome_completo,ano, texto_span))
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


        ###################### Artigos aceitos 


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Artigos aceitos para publicação' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                    resultados_artigoaceitos.append((nome_completo,ano, texto_span))
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


        ###################### apresentação trabalho


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Apresentações de Trabalho' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                    resultados_APStrabalho.append((nome_completo,ano, texto_span))
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')



        ###################### Demais


        # Loop por cada div com a classe 'cita-artigos'
        for cita_artigos in cita_artigos_list:
            tag_b = cita_artigos.find('b')

            # Verifica se a tag_b contém o texto desejado
            if tag_b and 'Outras produções bibliográficas' in tag_b.get_text(strip=True):
            # print("Texto encontrado:", tag_b.get_text(strip=True))

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
                                    resultados_demais.append((nome_completo,ano, texto_span))
                                # print("Ano:", ano, "Informações:", texto_span)

                    # Move para o próximo layout-cell-11
                    layout = layout.find_next('div', class_='layout-cell-11')


        return resultados_trabalho , resultados_APStrabalho , resultados_artigo , resultados_artigoaceitos , resultados_livros , resultados_capitulos , resultados_jornais , resultados_demais , resultados_ResumoExp , resultados_Resumo 

    except FileNotFoundError:
        print(f"O arquivo {arquivo_html} não foi encontrado.")
    except ValueError:
        print(f"Erro ao converter o ano para inteiro no arquivo {arquivo_html}.")
    except Exception as e:
        print(f"Ocorreu um erro no arquivo {arquivo_html}: {e}")
        return [], [], [], [], [], [], [], []


todos_resultados_trabalho = []
todos_resultados_APStrabalho = []
todos_resultados_artigo = []
todos_resultados_artigoaceitos =[]
todos_resultados_livros = []
todos_resultados_capitulos = []
todos_resultados_jornais = []
todos_resultados_demais = []
todos_resultados_ResumoExp = []
todos_resultados_Resumo = []


for html_file in os.listdir("data"):
    if html_file.endswith(".html"):
        html_path = os.path.join("data",html_file)
        resultados_trabalho , resultados_APStrabalho , resultados_artigo , resultados_artigoaceitos , resultados_livros , resultados_capitulos , resultados_jornais , resultados_demais , resultados_ResumoExp , resultados_Resumo = processar_arquivo(html_path)
        todos_resultados_trabalho.extend(resultados_trabalho)
        todos_resultados_APStrabalho.extend(resultados_APStrabalho)
        todos_resultados_artigo.extend(resultados_artigo)
        todos_resultados_artigoaceitos.extend(resultados_artigoaceitos)
        todos_resultados_livros.extend(resultados_livros)
        todos_resultados_capitulos.extend(resultados_capitulos)
        todos_resultados_jornais.extend(resultados_jornais)
        todos_resultados_demais.extend(resultados_demais)
        todos_resultados_ResumoExp.extend(resultados_ResumoExp)
        todos_resultados_Resumo.extend(resultados_Resumo)

# Criando os DataFrames com as colunas ajustadas para cada tipo de dado
df_trabalho = pd.DataFrame(todos_resultados_trabalho, columns=["Nome Completo","Ano", "Informações Gerais"])
df_APStrabalho = pd.DataFrame(todos_resultados_APStrabalho, columns=["Nome Completo","Ano", "Informações Gerais"])
df_artigo = pd.DataFrame(todos_resultados_artigo, columns=["Nome Completo","Ano", "Informações do Artigo", "Link do Artigo", "Autores", "Volume", "Página Inicial"])
df_artigoaceitos = pd.DataFrame(todos_resultados_artigoaceitos, columns=["Nome Completo","Ano", "Informações do Artigo"])
df_livros = pd.DataFrame(todos_resultados_livros, columns=["Nome Completo","Ano", "Informações Gerais"])
df_capitulos = pd.DataFrame(todos_resultados_capitulos, columns=["Nome Completo","Ano", "Informações Gerais"])
df_jornais = pd.DataFrame(todos_resultados_jornais, columns=["Nome Completo","Ano", "Informações Gerais"])
df_demais = pd.DataFrame(todos_resultados_demais, columns=["Nome Completo","Ano", "Informações Gerais"])
df_ResumoExp = pd.DataFrame(todos_resultados_ResumoExp, columns=["Nome Completo","Ano", "Informações Gerais"])
df_Resumo = pd.DataFrame(todos_resultados_Resumo, columns=["Nome Completo","Ano", "Informações Gerais"])

df_trabalho = df_trabalho.drop_duplicates()
df_APStrabalho = df_APStrabalho.drop_duplicates()
df_artigo = df_artigo.drop_duplicates()
df_artigoaceitos = df_artigoaceitos.drop_duplicates()
df_livros = df_livros.drop_duplicates()
df_capitulos = df_capitulos.drop_duplicates()
df_jornais = df_jornais.drop_duplicates()
df_demais = df_demais.drop_duplicates()
df_ResumoExp = df_ResumoExp.drop_duplicates()
df_Resumo = df_Resumo.drop_duplicates()


with pd.ExcelWriter('Producao_Bibliografica.xlsx') as writer:
    df_trabalho.to_excel(writer, sheet_name='Trabalhos anais de congresso', index=False)
    df_APStrabalho.to_excel(writer, sheet_name='Apresentação Trabalho', index=False)
    df_artigo.to_excel(writer, sheet_name='Artigos Publicados', index=False)
    df_artigoaceitos.to_excel(writer, sheet_name='Artigos Aceitos', index=False)
    df_livros.to_excel(writer, sheet_name='Livros Publicados', index=False)
    df_capitulos.to_excel(writer, sheet_name='Capitulos Publicados', index=False)
    df_jornais.to_excel(writer, sheet_name='Textos em Jornais', index=False)
    df_demais.to_excel(writer, sheet_name='Demais Produções', index=False)
    df_ResumoExp.to_excel(writer, sheet_name='Resumos Expandidos', index=False)
    df_Resumo.to_excel(writer, sheet_name='Resumos Simples', index=False)
