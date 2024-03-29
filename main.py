import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Real, Roleta, Heurístico, Creep, 1% por geracao, x²+y²+(3x+4y-26)², x E [0, 10], y E [0, 20]
pop_usuario = int(input("Deseja definir alguma população inicial, caso não digite valores menores ou iguais a 0: "))
pop_computador = 10000
populacao = 0
num_geracoes = 0
orderedFitness = []

if(pop_usuario > 0):
    populacao = pop_usuario
else:
    populacao = pop_computador

def fitness(curPopulation, currX, currY):
    if(curPopulation != 0 and (currX >= 0 and currX <= 10) and (currY >= 0 and currY <= 20)):
        fit = pow(currX, 2) + pow(currY, 2) + pow(((3 * currX) + (4 * currY) - 26), 2)
        orderedFitness.append({"x": currX, "y": currY, "fitness": fit})
        curPopulation -= 1
        currY += 1
        if(currY > 20):
            currY = 0
            currX += 1
            if(currX > 10):
                return
        fitness(curPopulation, currX, currY)


def selecao():
    totalFitness = sum(item["fitness"] for item in orderedFitness)
    numeroSorteio = random.uniform(0, totalFitness) # Sorteia um número entre 0 e o fitness para servir de base para a seleção de indivíduos
    somadorFitness = 0
    for item in orderedFitness:
        somadorFitness += item["fitness"]
        if somadorFitness > numeroSorteio:
            return item

def cruzamento():
    print("Aqui será feito o cruzamento pelo Ruan!")

def mutacaoCreepUniforme(individuo, sigma=0.1):
    valor = random.gauss(0, sigma) # Gera um valor entre 0 e sigma
    individuo["x"] += valor
    individuo["y"] += valor
    return individuo

def mutacaoCreepNaoUniforme(individuo, Liminf, Limsup, i):
    z = random.randint(0, 1) # Gera um valor binário para decidir se vai somar ou subtrair
    delta = random.random() # Gera um valor para ser multiplicado
    if z == 1:
        individuo["x"] += delta * (i, Limsup - individuo["x"])
        individuo["y"] += delta * (i, Limsup - individuo["y"])
    else:
        individuo["x"] -= delta * (i, individuo["x"] - Liminf)
        individuo["y"] -= delta * (i, individuo["y"] - Liminf)
    return individuo

def elitismo():
    print("Aqui será feita o elitismo pelo Ruan!")

def plotagem():
    x_values = [item["x"] for item in orderedFitness]
    y_values = [item["y"] for item in orderedFitness]
    fitness_values = [item["fitness"] for item in orderedFitness]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_values, y_values, fitness_values, c='r', marker='o')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Fitness')
    plt.show()


        
fitness(populacao, 0, 0)
selecionado = selecao() # Seleciona o indivíduo, será feito o cruzamento e a mutação
print("Escolha o tipo de mutacao \n-[1] Creep Uniforme \n-[2] Creep Não Uniforme")
mutacaoOp = int(input())
if mutacaoOp == 1:
    selecionadoMutacao = mutacaoCreepUniforme(selecionado)
elif mutacaoOp == 2:
    selecionadoMutacao = mutacaoCreepNaoUniforme(selecionado, 0, 10, 20) # Limite inferior, limite superior, i = 20
else: 
    print("Opção inválida")

if orderedFitness:
    # Encontra o dicionário com o maior valor de fitness
    melhor_individuo = max(orderedFitness, key=lambda x: x["fitness"])
    
    print("Melhor indivíduo:")
    print("x:", melhor_individuo["x"])
    print("y:", melhor_individuo["y"])
    print("fitness:", melhor_individuo["fitness"])

    plotagem()
else:
    print("Nenhum dado fitness foi calculado.")



