# multidownloadPics.pyw - download pictures
#-*-coding:UTF-8-*-

import sys,os,bs4,requests,datetime,time,os

def ArquivarImagem(imagem):
    imgContents = open(folder,'wb') ## criar path com o arquivo  
    for i in imagem.iter_content(100000):
        imageContents.write(i) ## escrever a imagem para a pasta no path especificado acima
    imageContents.close()    ## retorna o path com os arquivos salvos          

#extrair a imagem do referido objeto em bs4
def SelecionarQuadrinho(comicPage):
    tag = comicPage.find_all('img',class_='w-100 h-100')
    if(len(tag) == 0):
        raise('Quadrinho nao encontrado')
    tagComic = tag[0].get('src')
    res = requests.get(tagComic)
    res.raise_for_status()
    return res   

#gera objeto soup da pagina pesquisada
def AcessarPagina(tk):
    url = 'https://www.comicskingdom.com/arctic-circle/'+ str(tk)
    res = requests.get(url)
    res.raise_for_status() ## objeto de conexao de resposta em 200,senao encerra conexao
    comicPage = bs4.BeautifulSoup(res.text,features="lxml")
    return comicPage

if(__name__=='__main__'):###python multidownloadPics diretorio ano mes dia
    if(os.path.isdir(sys.argv[1]):
        folder = os.makedirs(sys.argv[1] + "\downloadPics\",exist_ok=True) ###armazenamento dos arquivos de imagens
            try: ###selecionar todos os quadrinhos de uma data
                dia_atual = datetime.datetime(argv[2], argv[3], argv[4])
                tk = datetime.datetime.strftime(dia_atual,format='%Y-%m-%d')
                pagina = AcessarPagina(tk)
                imagem = SelecionarQuadrinho(pagina)
                ArquivarImagem(imagem)
            except Exception(err):
                print('Erro:' + str(err))
    else:sys.exit()
