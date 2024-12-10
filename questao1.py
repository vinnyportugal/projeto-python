# questao 1 -> estrtura de dados -> listas encadeadas
# cria os elementos da lista
import time
from time import sleep
t = 5
time.sleep(t)


class ElementoDaLista:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __repr__(self):
        return str(self.dado)

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            nodo = ElementoDaLista(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaLista(dado=elem)
                nodo = nodo.proximo

    def __repr__(self):
        nodos = []
        atual = self.head
        while atual is not None:
            nodos.append(repr(atual))
            atual = atual.proximo
        nodos.append("None")
        return " -> ".join(nodos)

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserir_sem_prioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo

    def inserir_com_prioridade(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

    def inserir(self):
        try:
            while True:
                cor = input('QUAL A COR DO CARTAO DO PACIENTE? (A / V)\n>>> ').upper()
                numero = int(input('QUAL O NUMERO DO PACIENTE?\n>>> '))
                dado = f"{cor}{numero}"
                if cor == 'A':
                    self.inserir_com_prioridade(ElementoDaLista(dado=dado))
                else:
                    self.inserir_sem_prioridade(ElementoDaLista(dado=dado))
                condicao = input('Deseja cadastrar mais algum paciente? (S/N)\n>>> ').upper()
                if condicao == 'N':
                    break
        except ValueError:
            print("SOMENTE NUMEROS INTEIROS")

    def atender_paciente(self):
        if self.head is None:
            raise Exception("Lista vazia")
        print(f"Paciente {self.head.dado} chamado para consulta!")
        self.head = self.head.proximo

    def imprimir_lista_espera(self):
        atual = self.head
        while atual is not None:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

# Programa principal
teste_menu = ListaEncadeadaSimples()

while True:
    print('|1 - adicionar paciente na fila |')
    print('|2 - mostrar paciente na fila   |')
    print('|3 - chamar paciente            |')
    print('|4 - sair                       |')
    menu = int(input('Qual operação deseja?\n>>> '))
    if menu == 1:
        teste_menu.inserir()
    elif menu == 2:
        teste_menu.imprimir_lista_espera()
    elif menu == 3:
        try:
            teste_menu.atender_paciente()
        except Exception as e:
            print(e)
    elif menu == 4:
        sleep(t)
        print('Encerrando programa!')
        break
    else:
        continue
