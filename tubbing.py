##tubbing.py - pesquisa de videos no youtube
##coding:utf-8
import requests,bs4,select,webbrowser,sys

#download da pagina

def openPages(linkElems):
    numOpen = min(5,len(linkElems)) #as cinco primeiras referencias da palavra-chave
    for i in range(numOpen):#Abre uma aba do navegador para cada resultado
        webbrowser.open('http://youtube.com'+linkElems[i].get('href'))#watch?=token
    return

def wrappingTube(keyword):
    if(len(keyword) == 0):
        raise Exception("palavra-chave somente pode ser string")
    print('looking for a youtube videos at the moment...')
    res = requests.get('http://youtube.com/results?search_query='+''.join(keyword))
    res.raise_for_status()#interrompe programa se ocorrer erro em requests
    soup = bs4.BeautifulSoup(res.text,features="html.parser")#obtem links dos principais resultados da pesquisa
    linkElems = soup.find_all('a',attrs={'class':'pl-video-title-link'})#gera um vetor de links
    if(len(linkElems == 0)):
        raise Exception ("nenhum link encontrado")
    return linkElems

if(__name__=="__main__"):
    try:
        w = wrappingTube(sys.argv[1:])#palavra chave
        openPages(w)
    except Exception as err: #evitar que parametro não seja passado ou conexao abortada
        print("Erro:" + str(err))
else:
    w = wrappingTube(input('insira palavras-chaves'))
    openPages(w)
