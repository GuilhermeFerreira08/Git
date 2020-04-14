import re
import pyperclip


def getPhone(teste):
    phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?         #codigo de area
                        (\s|-|\.)?              #separador
                        (\d{3})                  #primeiros 3 digitos
                        (\s|-|\.)               #separador
                        (\d{4})                 #últimos 3 dígitos
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?      #extensão #comentarios na expressao regular
                        )''',re.VERBOSE)  
    return phoneRegex

def getEmail(teste2):
    emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4})
                        )''',re.VERBOSE)
    return emailRegex


def getRequest(teste3):
    requestRegex = re.compile(r'^(http://|https://)(www)(\.\w+)(\.\w{2,3}$')    
    return requestRegex 

                                    
def matchesResults(ph,em,req):
    matches = []
    for groups in req.findall(teste3):
        matches.append('-'.join([groups[1],groups[2]]))
    for groups in em.findall(teste2):
        matches.append(groups[0])
    for groups in ph.findall(teste):
        matches.append('-'.join([groups[1],groups[3],groups[5]]))
    return matches

def regexInfo(teste,teste2,teste3):
    ph,em,req = getPhone(teste),getEmail(teste2),getRequest(teste3)
    return ph,em,req

def main(ph,em,req):
    results = matchesResults(ph,em,req)
    pyperclip.copy('\n'.join(results))
    print('Copied to clipboard:')
    print('\n'.join(matches))
    if (len(results) > 0):
        ph.search(results[2]).group()
        em.search(results[1]).group()
        req.search(results[0]).group()
        #print('{0}\n{1}\n{2}'.format(ph,em,req))
    else:print('No phone numbers or email or addresses found.')


try:    
    teste = '(011) 256-5678' 
    teste2 = 'fulano@gmail.com.br'
    teste3 = 'http://www.youtube.com'
    t1,t2,t3 = regexInfo(teste,teste2,teste3)   
    main(t1,t2,t3)
except Exception(err):
    print(str(err))
else:
'''----storing on var text---'''
    text = str(pyperclip.paste())
    print(text)







