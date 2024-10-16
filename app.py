# Inicializando uma lista vazia para as tarefas
tarefas = []

# Perguntando quantas tarefas o usuário deseja cadastrar
num_tarefas = int(input("Quantas tarefas deseja cadastrar hoje? "))

# Loop para adicionar as tarefas
for i in range(num_tarefas):
    tarefa = input(f"Digite a tarefa {i+1}: ")
    tarefas.append(tarefa)

# Exibindo a lista de tarefas ao final
print("\nLista de tarefas do dia:")
for i, tarefa in enumerate(tarefas, 1):
    print(f"{i}. {tarefa}")
