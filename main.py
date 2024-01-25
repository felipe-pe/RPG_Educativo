from time import sleep
import sys



"""
    Título: CodeQuest

    Cenário:
    CodeQuest se passa em um mundo futurista onde a programação é a chave para o avanço tecnológico.
    Os jogadores assumem o papel de um jovem programador talentoso, recrutado para uma missão épica 
    pela renomada Guilda dos Codificadores.

    Enredo:
    O protagonista é chamado para uma jornada desafiadora para resolver uma crise tecnológica que ameaça
    paralisar todo o ecossistema digital. Uma inteligência artificial malévola, conhecida como "BugMancer", 
    está se espalhando rapidamente e corrompendo códigos vitais.

    Missão:
    A Guilda dos Codificadores, percebendo a ameaça, seleciona o jogador para deter o BugMancer.
    A jornada é dividida em várias fases, cada uma representando uma área do ecossistema digital
    afetada pelo BugMancer. Para avançar, o jogador deve resolver desafios de programação em cada fase.

    Personagens:
    1. Protagonista: O jogador, um jovem talentoso programador com habilidades variadas.
    2. Mestre da Guilda: Um sábio líder da Guilda dos Codificadores que orienta o protagonista.
    3. BugMancer: A inteligência artificial malévola que corrompe códigos e cria desafios complexos.

    Fases do Jogo:
    1. Cidade Inicial: Introdução ao jogo, apresentação do problema e tutorial básico.
    2. Floresta dos Loops: Os jogadores enfrentam desafios relacionados a estruturas de repetição.
    3. Montanha das Condições: Desafios que envolvem declarações condicionais e lógica.
    4. Deserto das Funções: Fase centrada em funções e modularização do código.
    5. Caverna das Variáveis: Enfrentar desafios complexos que exigem manipulação eficiente de variáveis.
    6. Cidadela da Recursão: Introdução à recursão e desafios que exploram essa técnica.
    7. Enfrentando o BugMancer: O confronto final com o BugMancer, onde todas as habilidades adquiridas
    são postas à prova.

    Recursos:
    Ao longo da jornada, o jogador recebe "PowerBugs", pequenos aliados virtuais que concedem poderes especiais 
    para auxiliar na resolução de desafios.

    Artigo de Auxílio:
    A cada fase concluída, o jogador recebe um artigo educativo que aprofunda os conceitos aprendidos naquela fase.
    Por exemplo, após a fase da "Floresta dos Loops", o jogador recebe um artigo detalhando os diferentes 
    tipos de loops e suas aplicações.

    Conclusão:
    Ao derrotar o BugMancer, o jogador não só salva o mundo digital, mas também se torna um mestre codificador, 
    reconhecido pela Guilda e pelos habitantes do ecossistema digital.
"""





def primeiro_desafio():
    print("corrigir o erro na declaração da variável")
    nome = 'paulo'
    numero = 2


def animar_texto(texto):
    for i in texto:
        print(i, end="")
        sys.stdout.flush()
        sleep(.05)


b = """
    .-------.
   /        /
  | ()   () |
   \  ___  /
    | \_/ |

Vamos começar nossa jornada!
"""
animar_texto(b)

print(""" 
         Qual A opção que deseja escolher ?, 1 - primeiro desafio   2 - explicação 
         Lembrando você só pode ir para o próximo desafio caso tenha concluido o anterior """)


opcao = int(input("Informe sua Opção? "))

if opcao == 1:
    possivel = input('é possível somar essas duas variáveis: nome = paulo + numero = 2: ')
    if possivel == 'nao':
        print("acertou")
    else:
        print("errou")
    
if opcao == 2:
    print('Não é possível somar String com Número: Só inteiro com inteiro ou float')
