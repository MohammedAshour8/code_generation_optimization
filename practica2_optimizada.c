#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

int main(int argc, char *argv[]){
    int i, j;
    int N = atoi(argv[1]);
    int ITER = atoi(argv[2]);
    float *x, *y, *z, tiempo_transcurrido = 0.0, tiempo_total = 0.0;
    struct timeval inicio, final;

    x = (float *) malloc(N * sizeof(float));
    y = (float *) malloc(N * sizeof(float));
    z = (float *) malloc(N * sizeof(float));

    for(i = 0; i < N; i++){
        x[i] = i;
        y[i] = i;
    }

    void suma2(float *x, float *y, float *z){
        for(i = 0; i < N; i++){
            z[i] = x[i] + y[i];
        }
    }

    for(j = 0; j < ITER; j++){
        gettimeofday(&inicio, NULL);
        suma2(x, y, z);
        gettimeofday(&final, NULL);
        tiempo_transcurrido = (final.tv_sec - inicio.tv_sec) + 1e-6*(final.tv_usec - inicio.tv_usec);
        tiempo_total += tiempo_transcurrido;
    }
    printf("%0.8f\n", tiempo_total / ITER);
    free(x);
    free(y);
    free(z);
    return 0;
}