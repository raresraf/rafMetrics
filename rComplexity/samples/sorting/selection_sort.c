//Implementation of Selection sort in C
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define swap(t, x, y) t z = x; x = y; y = z;
typedef int TYPE;
void selection_sort(TYPE [], int);
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
	selection_sort(A, n);
    gettimeofday(&end, NULL);
    float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
    printf("%12f \n", elapsed);

	return EXIT_SUCCESS;
}

void selection_sort(TYPE A[], int n) {
	int i, j, max;
	for(i = 0; i < n - 1; i++) {
		max = i;
		for(j = i + 1; j < n; j++) {
			if(A[max] < A[j]) max = j;
		}
		if(max != i) { 
			swap(TYPE, A[i], A[max]); 
			// '{' and '}' are  needed when using macros inside condition
		}
	}
}
void print_array(TYPE A[], int n) {
	int i = 0;
	putchar('[');
	while(i < n) {
		if(i > 0) printf(", ");
		printf("%d", A[i++]); //first A[i] is done then i = i + 1
	}
	puts("]");
}