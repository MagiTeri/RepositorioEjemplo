# Tarea / base de datos de los pinguinos
# Montes MartÃ­nez Itsy Teri

import pandas as pd
import matplotlib.pyplot as plt


train_data = pd.read_csv(r'C:\Users\980032406\Documents\7 semestre\Reconocimiento de patrones\penguins_testing.csv')
# Cuando lleva {} se le llama diccionario
plt.figure(figsize=(10,6))
species = {'Adelie Penguin (Pygoscelis adeliae)':'blue',
            'Chinstrap penguin (Pygoscelis antarctica)':'green',
            'Gentoo penguin (Pygoscelis papua)':'red'}

for specie, color in species.items():
     subset = train_data[train_data['Species']==specie]
     plt.scatter(subset['Sex'],subset['Body Mass (g)'],color=color,
                 label=specie,alpha=0.6)


plt.xlabel('Sexo')
plt.ylabel('Body Mass (g)')
plt.title('Sexo vs masa')
plt.legend()
plt.grid(True)
