import PySimpleGUI as sg
import zipfile

sg.theme('dark grey 9')

layout = [
    [sg.Text('Escolha o arquivo .ZIP')],
    [sg.InputText(key='zipfile'), sg.FileBrowse('Pesquisar')],
    [sg.Submit('Enviar')]
]

window = sg.Window('Project Python 3.9.0', layout)

event, values = window.read()

zip_file = values['zipfile']
zip_object = zipfile.ZipFile(file=zip_file, mode='r') #Pegou tudo e vai ler... e o modo que ele vai estar 'r' = read.
zip_object.extractall("C:/Users/username/Desktop") #Para qual caminho o arquivo vai.
