//Implementation of Insertion sort in C
#include <stdio.h>
#include <stdlib.h>
typedef int TYPE;
void insertion_sort(TYPE [], int);
void print_array(TYPE [], int);

int main(){
	TYPE A[] = {55, 2, 18, 332, 1};
	int n = sizeof(A) / sizeof(TYPE);
	
	printf("Unsorted: ");
	print_array(A, n);
	
	printf("Sorted: ");
	insertion_sort(A, n);
	print_array(A, n);
	
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