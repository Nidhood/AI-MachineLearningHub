# Algoritmo Genético para Planificación de Rutas 🧬🗺️

Una implementación del algoritmo genético utilizado para encontrar la ruta más corta desde un punto a otro con algunos obstáculos en medio, utilizando los puntos de ruta disponibles en todo el espacio. He utilizado Matplotlib para mostrar la simulación. Algunas ayudas fueron tomadas de [la implementación de Yaaximus aquí](https://github.com/Yaaximus/genetic-algorithm-path-planning), pero el enfoque adoptado es diferente y he codificado formas de generar obstáculos y puntos de ruta aleatoriamente, por lo que el método es mucho más dinámico en lugar de centrarse en obstáculos y rutas estáticas.

## Instrucciones de Configuración

Asegúrate de tener Python 3.6 o superior instalado. Clona el repositorio y realiza lo siguiente en el directorio.

**Linux**
```python
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 simulate.py
```

**Windows**
```python
python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
python simulate.py
```

## Conclusiones

Este proyecto presenta una implementación efectiva del algoritmo genético para resolver el problema de la planificación de rutas. Al utilizar una población inicial de cromosomas y aplicar operadores genéticos como el cruce y la mutación, el algoritmo es capaz de encontrar soluciones cercanas a la óptima para una variedad de configuraciones de obstáculos y puntos de ruta. Además, la capacidad de generar obstáculos y puntos de ruta de manera dinámica hace que la solución sea más versátil y adaptable a diferentes escenarios. En resumen, este proyecto demuestra el poder y la flexibilidad del algoritmo genético en la resolución de problemas de optimización complejos como la planificación de rutas.