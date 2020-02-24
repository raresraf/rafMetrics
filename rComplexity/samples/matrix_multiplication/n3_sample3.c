#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include <sys/time.h>


int main(int argc, char* argv[])
{
	if(argc != 2)
	{
        printf("Usage: %s <matrixSize>\n", argv[0]);
		return -1;
	}


    // Matrix size
    int64_t N = atoi(argv[1]);

	int bl;

    int** a = (int **) malloc(N * sizeof(int *));
    int** b = (int **) malloc(N * sizeof(int *));
    int** c = (int **) malloc(N * sizeof(int *));
    for(int i = 0; i < N; i++){
        a[i] = (int *) malloc(N * sizeof(int));
        b[i] = (int *) malloc(N * sizeof(int));
        c[i] = (int *) malloc(N * sizeof(int));
    }

	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++){
			a[i][j] = rand() % 10;
			b[i][j] = rand() % 10;
			c[i][j] = 0;
		}


	int i,j,k,ii,jj,kk;

    struct timeval start, end;
	gettimeofday(&start, NULL);
	bl = 64;

    for(ii=0; ii<N; ii+=bl)
        for(jj=0; jj<N; jj+=bl)
            for(kk=0; kk<N; kk+=bl)
                for(i=0; i<bl && ii+i < N; i++)
                    for(j=0; j<bl && jj + j < N; j++)
                        for(k=0; k<bl && kk + k < N; k++)
                            c[ii+i][jj+j] += a[ii+i][kk+k]*b[kk+k][jj+j];
	gettimeofday(&end, NULL);


	float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
    printf("%12f\n", elapsed);

	return 0;
}

