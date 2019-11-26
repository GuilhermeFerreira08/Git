import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for par in doc.paragraphs:
        fullText.append(' ' + par.text)
    return '\n\n'.join(fullText)
