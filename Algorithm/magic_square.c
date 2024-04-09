#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 15
int main(){
	int sqr[MAX_SIZE][MAX_SIZE];
	int i,j,row,col;
	int count;
	int size;

	printf("Enter the size of the square: ");
	scanf("%d",&size);

	if(size < 1 || size > MAX_SIZE +1){
		fprintf(stderr, "Size is out of range\n");
		exit(EXIT_FAILURE);
	}

	if(!(size%2)){
		fprintf(stderr,"Size is even\n");
		exit(EXIT_FAILURE);
	}

	for(i=0;i<size;i++)
		for(j=0;j<size;j++)
			sqr[i][j] = 0;
	
	sqr[0][(size-1)/2] = 1;
	i = 0;
	j = (size-1)/2;

	for(count = 2; count <= size*size;count++){
		row = (i-1<0) ? (size -1):(i-1);
		col = (j-1<0) ? (size -1):(j-1);
		if(sqr[row][col])
			i = (++i) % size;
		else{
			i = row;
			j = (j-1<0) ? (size -1):--j;
		}
		sqr[i][j] = count;
		printf("sqr[%d][%d] = %d\n",i,j,count);
	}
	printf("Magic Square of size %d : \n\n",size);
	for(i=0;i<size;i++){
		for(j=0;j<size;j++)
			printf("%5d",sqr[i][j]);
		printf("\n");
	}

	printf("\n\n");
	return 0;
}