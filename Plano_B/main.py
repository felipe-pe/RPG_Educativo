import subprocess


def abrir_editor(editor,arquivo):
    subprocess.run([editor,arquivo])
    input("Após a edição aperte ENTER para continuar.")
    
    
def ler_arquivo_de_desafio(nome_do_desafio):
    with open(f'./desafios/{nome_do_desafio}', 'r') as desafio:
        return desafio.read()

def executar_desafio(nome_do_desafio): 
    return subprocess.run(['python', f'desafios/{nome_do_desafio}'],capture_output=True, text=True)

def verificar_resultado_do_desafio(resultado):
    match resultado.returncode:
        case 0:
            print("rodou o codigo normalmente")
            #O codigo foi executado corretamente. Agora tem que verificar se a saida é o resultado esperado do desafio.
            
        case 1:
            print("O codigo não rodou") 
            #O codigo não foi executado por erro do codigo 
            
        case _:
            ...
            #Erros inesperados
            




# Exemplo de usa das funções acimas

abrir_editor(editor='notepad.exe',arquivo='condicional/desafio_condicional01.py')
codigo_do_desafio = ler_arquivo_de_desafio("condicional/desafio_condicional01.py")
resultado_do_codigo = executar_desafio('condicional/desafio_condicional01.py')
verificar_resultado_do_desafio(resultado_do_codigo)