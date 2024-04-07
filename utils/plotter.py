import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output
from config.config_parser import parser
plt.ion()


def plot(obstacles, path_points, population, path_lengths, gen, last_gen):

    for i, chromosome in enumerate(population):
        _reset_plot(obstacles, path_points)

        path_x = [path_points[j][0] for j, c in enumerate(chromosome) if c == '1']
        path_y = [path_points[j][1] for j, c in enumerate(chromosome) if c == '1']

        plt.plot(path_x, path_y, '-')
        plt.text(1, int(parser['Plot Axes']['y_end']) + 1,
                 f"Generación: {gen}, Cromosoma No. {i + 1}\nLongitud del Camino: {path_lengths[i]}")

        plt.pause(0.025)
        clear_output(wait=True)  # Limpiar la salida de la celda antes de mostrar la siguiente iteración

    if last_gen:
        _show_final_path(obstacles, path_points, population, path_lengths, gen)

def _plot_evolution(evolution_data):
    plt.figure()
    plt.plot(evolution_data, marker='o', linestyle='-')
    plt.xlabel('Generación')
    plt.ylabel('Longitud Media del Camino')
    plt.title('Evolución de la Longitud Media del Camino a lo largo de las Generaciones')
    plt.grid(True)
    plt.show()

def _show_final_path(obstacles, path_points, population, path_lengths, gen):
    index_min = np.argmin(path_lengths)

    plt.ioff()
    _reset_plot(obstacles, path_points)
    
    chromosome = population[index_min]

    path_x = [path_points[j][0] for j, c in enumerate(chromosome) if c == '1']
    path_y = [path_points[j][1] for j, c in enumerate(chromosome) if c == '1']

    plt.plot(path_x, path_y, '-')
    plt.text(1, int(parser['Plot Axes']['y_end']) + 1, f"Finalizado en la generación: {gen}\nCamino más corto encontrado: {path_lengths[index_min]}")

    plt.pause(1)
    print('¡Listo! Camino más corto encontrado.')
    plt.show()

def _reset_plot(obstacles, path_points):
    
    plt.clf()

    axes = parser['Plot Axes']
    plt.axis([int(axes['x_start']), 
        int(axes['x_end']),
        int(axes['y_start']),
        int(axes['y_end'])])

    _plot_obstacles(obstacles)
    _plot_path_points(path_points)

def _plot_path_points(path_points):
    path_point_x = [path_point[0] for path_point in path_points]
    path_point_y = [path_point[1] for path_point in path_points]

    plt.plot(path_point_x[1:-1], path_point_y[1:-1], "k.")
    plt.plot(path_point_x[0], path_point_y[0], "bo", label='Source')
    plt.plot(path_point_x[-1], path_point_y[-1], "go", label='Goal')

    plt.legend(loc="upper left")

def _plot_obstacles(obstacles):
    
    for obstacle in obstacles:
        x_values, y_values = [], []

        for vertex in obstacle:
            x_values.append(vertex[0])
            y_values.append(vertex[1])
        
        plt.fill(x_values, y_values, 'r')