# code_generation_optimization
En la presente práctica se ha realizado un estudio sobre la generación y optimización de un código en lenguaje *C*. La técnica de optimización es el **paso de bucles a una función**, la cual consiste en localizar un bucle determinado y mandarlo a una función. Desde el *main*, se realiza una llamada a esa función que contiene el bucle
## Ficheros
Se cuenta con dos códigos en *C*, un script en *Python* y otro en *Bash*:
- <a href="https://github.com/MohammedAshour8/code_generation_optimization/blob/main/practica2.c">practica2.c</a>: Código en *C* no optimizado. En él se encuentra el bucle dentro de la función *main*, no dentro de una función
- <a href="https://github.com/MohammedAshour8/code_generation_optimization/blob/main/practica2_optimizada.c">practica2_optimizada.c</a>: Código en *C* optimizado. A diferencia del código anterior y tal y como se ha comentado anteriormente, se ha añadido una función que recoge el bucle en el que se realizarán las operaciones.
- <a href="https://github.com/MohammedAshour8/code_generation_optimization/blob/main/script.py">script.py</a>: script en *Python* que se encarga de realizar la representación gráfica de los tiempos de ejecución de los dos programas en C. Con esto se podrá comprobar el comportamiento de los tiempos de ejecución en función del número de iteraciones del bucle de operaciones.
- <a href="https://github.com/MohammedAshour8/code_generation_optimization/blob/main/script.sh">script.sh</a>: script en *Bash* que se encarga de realizar las múltiples ejecuciones 

## Ejecución
Para su ejecución, desde una terminal de *Linux*, simplemente hay que ejecutar el script de bash del siguiente modo:

    $ bash script.sh
 
 Cabe destacar que todos los ficheros tienen que estar en un mismo directorio, y el comando anterior tiene que ser ejecutado dentro de la susodicha ruta.
