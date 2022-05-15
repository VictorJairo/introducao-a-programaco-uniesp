
#Desenvolva os algoritmos abaixo em linguagem Python. Utilize o VS Code ou Pycharm, mas ao final entregue ao professor um arquivo .py para cada questão desenvolvida.
#  As atividades deverão ser entregues no Github.
#Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, chame este dicionário de glossário.
#Pense em cinco palavras relacionada à programação que você conheceu nesta disciplina. Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
#Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois
#  o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para 
# inserir uma linha em branco entre cada par palavra-significado em sua saída.



from tkinter import N


glossario = {'Vscode': 'O Visual Studio Code (VS Code) é um editor de código de código aberto desenvolvido pela Microsoft.' }
glossario['Algoritmos'] = 'Um Algoritmo Pode Ser Definido como Uma Sequência de passos que visam atingir um objetivo bem Definido.'
glossario['Lógica de Programação'] = 'Lógica de programação é a técnica de encadear pensamentos para atingir determinado objetivo.\n Estes pensamentos, podem ser descritos como uma seqüência de instruções, que devem ser seguidas para se cumprir uma determinada tarefa.\nSeqüência Lógica são passos executados até atingir um objetivo ou solução de um problema.'
glossario['Webscraping'] = 'O web scraping (raspagem de rede, em tradução livre), também conhecido como extração de dados da web,\n é o nome dado ao processo de coleta de dados estruturados da web de maneira automatizada'
glossario['Python'] = 'Python é uma linguagem Open-Source de propósito geral usado bastante em data science, machine learning, desenvolvimento de web,\n desenvolvimento de aplicativos, automação de scripts, fintechs e mais.'

print('------------------------------------------------------ \n')
print(f"Vscode: {glossario['Vscode']}\n")
print('------------------------------------------------------ \n')
print(f"Algoritmos: {glossario['Algoritmos']}\n")
print('------------------------------------------------------ \n')
print(f"Lógica de Programação: {glossario['Lógica de Programação']}\n")
print('------------------------------------------------------ \n')
print(f"Webscraping: {glossario['Webscraping']}\n")
print('------------------------------------------------------ \n')
print(f"Python: {glossario['Python']}\n")
print('------------------------------------------------------ \n')