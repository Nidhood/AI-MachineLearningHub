
# Importamos la clase ConfigParser de la librería configparser, el cual nos permitirá leer y escribir archivos de configuración en formato INI.
from configparser import ConfigParser

parser = ConfigParser()
parser.read('../config/config.ini')