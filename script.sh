#!/bin/bash

gcc -Wall practica2.c -o p2 -O0
gcc -Wall practica2_optimizada.c -o p2op -O0

valores_n=(200000000 400000000 600000000 800000000 1000000000 1200000000)
potencia2=(268435456 536870912 1073741824)
valores_iter=(30 20 15 10 5)

for i in {0..4};
do
	for j in {0..9};
	do
		./p2 "${valores_n[$i]}" "${valores_iter[$i]}" | paste -sd ' ' >> salida_p2.csv
		./p2op "${valores_n[$i]}" "${valores_iter[$i]}" | paste -sd ' ' >> salida_p2op.csv
	done
done
echo "Terminado"

python3 script.py