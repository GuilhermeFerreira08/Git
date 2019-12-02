##tubbing.py - pesquisa de videos no youtube
##coding:utf-8
import requests,bs4,select,webbrowser,sys

#download da pagina

def openPages(links):
    numOpen = min(5,len(links)) #as cinco primeiras referencias da palavra-chave
    for i in range(numOpen):#Abre uma aba do navegador para cada resultado
        webbrowser.open('http://youtube.com'+links[i].get('href'))#watch?=token
    return

def wrappingTube(keyword):
    if(not keyword):
        raise Exception("não digitou palavre-chave")
    print('looking for a youtube videos at the moment...')
    res = requests.get('https://www.youtube.com/results?search_query='+''.join(keyword))
    res.raise_for_status() #interrompe programa se ocorrer erro em requests
    soup = bs4.BeautifulSoup(res.text,features="html.parser") #obtem links dos principais resultados da pesquisa
    links = soup.select('h3 > a[href]') #gera um vetor de links e seus enderecos
    if(not links):
        raise Exception ("nenhum link encontrado")
    return links

if(__name__=="__main__"):
    try:
        w = wrappingTube(sys.argv[1:])#palavra chave
        openPages(w)
    except Exception as err: #evitar que parametro não seja passado ou conexao abortada
        print("Erro:" + str(err))

keyword = input('insira palavra-chave')
w = wrappingTube(keyword)
openPages(w)
