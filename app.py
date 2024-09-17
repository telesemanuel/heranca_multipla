from modulo import *

if __name__ == "__main__":
    # instancia do objeto da superclasse
    h = Filho('','','','',0.0,0.0,'')

    # entrada de dados
    h.nome = input('Informe o nome do herdeiro: ')
    h.email = input('Informe o e-mail: ')
    h.profissao = input('Informe a profissão: ')
    h.olhos = input('Infome a cor dos olhos: ')
    h.peso = float(input('Infome o peso em kg: ').replace(',','.'))
    h.altura = float(input('Infome a altura em metros: ').replace(',','.'))
    h.cor_cabelo = input('Infome a cor do cabelo: ')

    # saída de dados
    print('\n')
    h.exibir_cartao_visitas()
    h.exibir_fisico()