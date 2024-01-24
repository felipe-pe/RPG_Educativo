import subprocess

def abrir_editor(editor,arquivo):
    subprocess.run([editor,arquivo])
    
def criar_arquivo_de_desafio(nome_do_desafio, codigo_do_desafio):
    with open(f'./desafios/{nome_do_desafio}.py', 'w') as desafio:
        desafio.write(codigo_do_desafio)

def ler_arquivo_de_desafio(nome_do_desafio):
    with open(f'./desafios/{nome_do_desafio}.py', 'r') as desafio:
        return desafio.read()

