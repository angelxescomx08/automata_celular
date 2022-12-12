# Autómata celular

Una aplicación para poder ver todas las reglas (256) de un autómata celular, también permite crear configuraciones de células específicas y guardar las configuraciones
y los resultados en un archivo.

## Correr el proyecto

NOTA: Para ejecutar el programa se necesitará tener matplotlib que puede que no esté instalada por defecto en caso de que
no se encuentre ese módulo ejecutar lo siguiente:

```bash
pip install matplotlib
```

Para correr el proyecto ejecutaremos la siguiente linea en nuestra terminal:

```bash
python interfaz.py
```

## Archivos para seer cargados

El programa puede cargar archivos ".txt" que generan un autómata celular, dichos archivos contienen 3 lineas.
1. La primera linea representa el número dee iteraciones (el alto del autómata).
2. La segunda linea representa la regla a utilizar hasta 255.
3. La tercera linea representa la configuración inicial.
