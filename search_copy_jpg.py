##searchjpg.py
##coding:utf-8##
###python search_copy_jpgs.py diretorio de origem diretorio de destino
from os import listdir
from os import mkdir
from os import walk
from os import listdir
from os.path import basename
from os.path import dirname
from sys import argv 
from shutil import copy

    
def verifyDir(dest):
    newFolder = 'C:\\Users\\Microsoft\\Pictures\\'+ dest
    if(os.path.exists('C:\\Users\\Microsoft\\Pictures\\' + dest) == False):
        newFolder = makedirs('C:\\Users\\Microsoft\\Pictures\\' + dest)
        return (newFolder)
    

def existingFile(filename,total_files_backup): ##se arquivo no diretorio de origem estiver presente no diretorio de destino
    if(filename not in total_files_backup):
        return (filename)
    return ''

def copyFiles(pics,backup):
    if(pics.endswith('.jpeg')):
        copy(pics,backup)
    elif (pics.endswith('.jpg')):
        copy(pics,backup)    
    return

def backupPics(backup):##padrao salvar na subpasta Pictures do usuario
    total_files_backup = listdir(backup)# diretorio destino das fotos
    for folderName,subfolders,filenames in walk(source):
        for subfolder in subfolders:
            for filename in filenames:
                pics = existingFile(filename,total_files_backup)
                return pics

def main():
    dest = input('Digite nome do diretorio destino de seus arquivos de backup')
    source = input('Fonte dos arquivos a copiar')
    source = os.path.dirname(source)##garante que somente o path seja repassado
    backup = verifyDir(dest) ##nome do diretorio recem-criado
    pics = backupPics(backup,source) ##fonte das fotos para sofrerem backup na pasta backup
    copyFiles(pics,backup)    


if(__name__='__main__'):
    backup = verifyDir(argv[3]) ##nome do diretorio recem-criado
    pics = backupPics(backup,argv[2]) ##fonte das fotos para sofrerem backup na pasta backup
    copyFiles(pics,backup)  

main()
#REGRAS:criar um diretorio novo ##verificar se o diretorio não fora criado###se nao cria-lo,caso contrario usar o mesmo diretorio especificado
      #percorrer a cadeia de diretorios no input do da chamada da funcao
      #identificar os arquivos neste contido com extensao de imagens
      #verificar se o arquivo fora originalmente copiado para evitar sobrescrever o anterior
      #copiar cada arquivo
      #mover este arquivo para o diretorio criado
      #ordenar alfabeticamaente
