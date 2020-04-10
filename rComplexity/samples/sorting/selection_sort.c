//Implementation of Selection sort in C
#include <stdio.h>
#include <stdlib.h>
#define swap(t, x, y) t z = x; x = y; y = z;
typedef int TYPE;
void selection_sort(TYPE [], int);
void print_array(TYPE [], int);

int main(){
	TYPE A[] = {16, 3, 154, 86, 11};
	int n = sizeof(A) / sizeof(TYPE);
	
	printf("Unsorted: ");
	print_array(A, n);
	
	printf("Sorted (descending): ");
	selection_sort(A, n);
	print_array(A, n);
	
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