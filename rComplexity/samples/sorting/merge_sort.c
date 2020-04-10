//Implementation of Merge Sort in C
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

typedef int TYPE;
void merge(TYPE [], int, int, int);
void merge_sort(TYPE [], int, int);
void print_array(TYPE [], int);

TYPE* init_array(int size){
    TYPE* v = (TYPE *) malloc(size * sizeof(TYPE));
    for(int i = 0; i < size; i++){
        v[i] = rand();
    }
    return v;
}

int main(int argc, char **argv){
    if(argc != 2)
    {
        printf("Usage: %s <sortingSize>\n", argv[0]);
        return -1;
    }

    int n = atoi(argv[1]);
    TYPE *A = init_array(n);

    struct timeval start, end;
    gettimeofday(&start, NULL);
	merge_sort(A, 0, n-1);
    gettimeofday(&end, NULL);
    float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
    printf("%12f \n", elapsed);

	return EXIT_SUCCESS;
}
void merge(TYPE A[], int p, int q, int r) {
	int i, j, k;
	int nL = q - p + 1; 
	int nR = r - q;

	TYPE *L = malloc(sizeof(TYPE)*nL);
	TYPE *R = malloc(sizeof(TYPE)*nR);
	
	for (i = 0; i < nL; i++)	
		L[i] = A[p + i];
	
	for (j = 0; j < nR; j++)	
		R[j] = A[q + 1 + j];
	
	i = j = 0;
	k = p;
	
	while (i < nL && j < nR) 
		if (L[i] <= R[j])  A[k++] = L[i++];
		else  A[k++] = R[j++];
	
	while (i < nL)	A[k++] = L[i++];
	while (j < nR)	A[k++] = R[j++];
		
	free(L);
	free(R);
}
void merge_sort(TYPE A[], int p, int r) {
	if(p < r) {
		int q = (p + r) / 2;
		merge_sort(A, p, q);
		merge_sort(A, q + 1, r);
		merge(A, p, q, r);
	}
}
void print_array(TYPE A[], int n) {
	int i = 0;
	putchar('[');
	while(i < n) {
		if(i > 0) printf(", ");
		printf("%d", A[i++]); 
	}
	puts("]");
}