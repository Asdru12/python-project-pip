import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots() # Me crea la figura
    ax.bar(labels, values) # asigna los labels y values a la grafica
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [150, 200, 100]
    #generate_bar_chart(labels,values)
    generate_pie_chart(labels, values)
