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

	// TODO alocari si initializari
	int a[N][N];
	int b[N][N];
	int c[N][N];

	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++){
			a[i][j] = rand() % 10;
			b[i][j] = rand() % 10;
			c[i][j] = 0;
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


	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++){
			a[i][j] = rand() % 10;
			b[i][j] = rand() % 10;
			c[i][j] = 0;
		}

	gettimeofday(&start, NULL);
	for(int i = 0; i < N; i++){
		int *orig_pa = &a[i][0];
		for(int j = 0; j < N; j++){
			int *pa = orig_pa;
			int *pb = &b[0][j];
			register int suma = 0;
			for(int k = 0; k < N; k++){
			 	suma += *pa * *pb;
			 	pa++;
			 	pb += N;
			}
		 c[i][j] = suma;
		}
	}
	gettimeofday(&end, NULL);

	elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
	printf("After optimization:%12f\n", elapsed);


	return 0;
}

