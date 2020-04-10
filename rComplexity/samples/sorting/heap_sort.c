/*Heap sort implementation in C*/
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

typedef int TYPE;
int left(int);
int right(int); 
int parent(int);
void max_heapify(TYPE [], int, int);
void build_max_heap(TYPE [], int);
void heap_sort(TYPE [], int);
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
	heap_sort(A, n);
    gettimeofday(&end, NULL);
    float elapsed = ((end.tv_sec - start.tv_sec)*1000000.0f + end.tv_usec - start.tv_usec)/1000000.0f;
    printf("%12f \n", elapsed);

	return EXIT_SUCCESS;
}


void heap_sort(TYPE a[], int length){
	build_max_heap(a, length);
	int i = length - 1;
	do {
		TYPE temp = a[0];
		a[0] = a[i];
		a[i] = temp;
		
		max_heapify(a, 0, --length);
	} while(--i >= 0);
}
void build_max_heap(TYPE a[], int length){
	int i = length/2;
	do {
		max_heapify(a, i, length);
	}while(--i  >= 0); //first i = i - 1 is doen and then i >= 0 afterwards.
}
void max_heapify(TYPE a[], int i, int length){
	int r = right(i);
	int l = left(i);
	int max = i;
	if(l < length && a[max] < a[l]) max = l;
	if(r < length && a[max] < a[r]) max = r;
	if(max != i) {
		TYPE temp = a[i];
		a[i] = a[max];
		a[max] = temp;
		max_heapify(a, max, length);
	}
}
int left(int i) {
	return 2*i + 1;
}
int right(int i) {
	return 2*i + 2;
}
int parent(int i) {
	return (i - 1)/2;
}
void print_array(TYPE a[], int length){
	int i = 0;
	putchar('[');
	while(i < length) {
		if(i > 0) printf(", ");
		printf("%d", a[i++]); 
	} 
	puts("]");
}