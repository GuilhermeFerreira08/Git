import requests, sys, webbrowser, bs4
    if(name=='__main__'):
    print('Googling ...')
    #download da pagina
    res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
    res.raise_for_status()
    #obtem links dos principais resultados da pesquisa
    soup = bs4.BeautifulSoup(res.text,features="html.parser")
    linkElems = soup.select('.r a href')#gera um vetor de links
    #Abre uma aba do navegador para cada resultado
    numOpen = min(5,len(linkElems))#as cinco primerias referencias da palavra-chave
    for i in range(numOpen):
        webbrowser.open('http://google.com'+linkElems[i].get('href'))
