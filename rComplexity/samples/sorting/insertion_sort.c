//Implementation of Insertion sort in C
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

typedef int TYPE;
void insertion_sort(TYPE [], int);
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
	insertion_sort(A, n);
    gettimeofday(&end, NULL);
    float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
    printf("%12f \n", elapsed);

	return EXIT_SUCCESS;
}

void insertion_sort(TYPE A[], int n) {
	int i, j;
	TYPE temp;
	
	for(i = 1; i < n; i++) {
		temp = A[i];
		j = i;
		while(j > 0 && A[j-1] > temp) {
			A[j] = A[j - 1];
			j--;
		}
		A[j] = temp;
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