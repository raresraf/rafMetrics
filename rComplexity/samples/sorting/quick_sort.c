//Implementation of Quick Sort in C
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define swap(t, x, y) { t z = x; x = y; y = z; }
typedef int TYPE;
int partition(TYPE [], int, int);
void quick_sort(TYPE [], int, int);
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
	quick_sort(A, 0, n-1);
    gettimeofday(&end, NULL);
    float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
    printf("%12f \n", elapsed);

	return EXIT_SUCCESS;
}
int partition(TYPE A[], int p, int r) {
	TYPE x = A[r]; //pivot
	int i = p - 1, j;
	for(j = p; j < r ; j++) {
		if(A[j] <= x) {
			i = i + 1;
			swap(TYPE, A[i], A[j]); 
		}
	}
	i = i + 1;
	swap(TYPE, A[i], A[r]);
	return i;
}
void quick_sort(TYPE A[], int p, int r) {
	if(p < r) {
		int t = (rand() % ( r - p + 1) + p);
		swap(TYPE, A[t], A[r]); 
		//Used to avoid O(n^2) worst case
		
		int q = partition(A, p, r);
		quick_sort(A, p, q - 1);
		quick_sort(A, q + 1, r);
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