import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
    print("Aqui será feita a seleção pelo Pato!")

def cruzamento():
    print("Aqui será feito o cruzamento pelo Ruan!")

def mutacao():
    print("Aqui será feita a mutação pelo Pato!")

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



