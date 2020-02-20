#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include <sys/time.h>


int main(int argc, char* argv[])
{
	if(argc != 2)
	{
		printf("apelati cu %s <dim_matricei>\n", argv[0]);
		return -1;
	}

	int64_t N = atoi(argv[1]);  // dimensiunea matricei
	int bl;
	// TODO alocari si initializari
	int a[N][N];
	int b[N][N];
	int c[N][N];

	int aa[N][N];
	int bb[N][N];
	int cc[N][N];

	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++){
			a[i][j] = rand() % 10;
			b[i][j] = rand() % 10;
			c[i][j] = 0;
			aa[i][j] = a[i][j];
			bb[i][j] = b[i][j];
			cc[i][j] = 0;
		}

	struct timeval start, end;
	gettimeofday(&start, NULL);
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			for(int k = 0; k < N; k++)
				c[i][j] += a[i][k] * b[k][j];
	gettimeofday(&end, NULL);
	float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
	printf("Before optimization:%12f\n", elapsed);

	int i,j,k,ii,jj,kk;
	gettimeofday(&start, NULL);
	bl = 32;
    for(ii=0; ii<N; ii+=bl)
        for(jj=0; jj<N; jj+=bl)
            for(kk=0; kk<N; kk+=bl)
                for(i=0; i<bl; i++)
                    for(j=0; j<bl; j++)
                        for(k=0; k<bl; k++)
                            cc[ii+i][jj+j] += aa[ii+i][kk+k]*bb[kk+k][jj+j];
	gettimeofday(&end, NULL);


	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			if(c[i][j] != cc[i][j]){
				printf("Whoopsie, wrong calculated (%d, %d)\n", i, j);
			}
	elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
	printf("[Block size:%d] After optimization:%12f\n", bl, elapsed);


	gettimeofday(&start, NULL);
	bl = 64;
    for(ii=0; ii<N; ii+=bl)
        for(jj=0; jj<N; jj+=bl)
            for(kk=0; kk<N; kk+=bl)
                for(i=0; i<bl; i++)
                    for(j=0; j<bl; j++)
                        for(k=0; k<bl; k++)
                            cc[ii+i][jj+j] += aa[ii+i][kk+k]*bb[kk+k][jj+j];
	gettimeofday(&end, NULL);


	
	elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
	printf("[Block size:%d] After optimization:%12f\n", bl, elapsed);


	gettimeofday(&start, NULL);
	bl = 128;
    for(ii=0; ii<N; ii+=bl)
        for(jj=0; jj<N; jj+=bl)
            for(kk=0; kk<N; kk+=bl)
                for(i=0; i<bl; i++)
                    for(j=0; j<bl; j++)
                        for(k=0; k<bl; k++)
                            cc[ii+i][jj+j] += aa[ii+i][kk+k]*bb[kk+k][jj+j];
	gettimeofday(&end, NULL);


	
	elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
	printf("[Block size:%d] After optimization:%12f\n", bl, elapsed);

	return 0;
}

