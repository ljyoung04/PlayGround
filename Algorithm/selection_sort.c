#include <stdio.h>
#include <stdlib.h>
#define SWAP(x,y,t) ((t) = (x),(x)=(y),(y)=(t))
void sort(int [],int);

int main() {
    int i,n;
    int list[101];
    printf("Enter the number of numbers to geneate.");
    scanf("%d",&n);

    if(n < 1 || n > 101){
        fprintf(stderr,"Improper value of n\n");
        exit(EXIT_FAILURE);
    }

    for(i = 0 ; i < n; i++){
        list[i] = rand()%1000;
        printf("%d ",list[i]);
    }
    sort(list,n);
    printf("\n Sorted array \n");
    for(i = 0 ; i < n ; i++){
        printf("%d ",list[i]);
    }
    printf("\n");
    return 0;
}

void sort(int list[], int n){

    int i,j, min, temp;

    for(i=0 ; i < n-1 ; i ++){
        min = i;
        for(j=i+1 ; j < n ; j++){
            if(list[j] < list[min])
                min = j;
        }
    SWAP(list[i],list[min],temp);
    }
}