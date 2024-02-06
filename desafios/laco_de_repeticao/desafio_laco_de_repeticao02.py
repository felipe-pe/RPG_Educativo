# É necessário saber se tem o nome na lista de inserir foi criada essa função com o intuito 
# de ajudar o cliente na hora de inserir um no produto. quando ele executa imprimi as duas mensagens 
# como podemos corrigir


def achar_elemento(array, elemento):
  
  tamanho = len(array)
  
  for i in range(tamanho):
    if array[i] == elemento:

        print(f" O Nome {elemento} esta no Array")
        
  else:
        print(f"O nome {elemento} Não está no Aarry")

nomes = ["ana", "joao", "maria", "paulo"]

achar_elemento(nomes, "ana")