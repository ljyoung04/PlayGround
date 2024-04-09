#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define SWAP(x,y,t) ((t) = (x),(x)=(y),(y)=(t))
void perm(char *list, int i, int n);

int main() {
	char str[100];
	printf("Recursive permutation generator : ");
	scanf("%s",&str);
	int n = strlen(str);
	perm(str,0,n-1);
	return 0;
}

void perm(char *list, int i, int n){
	int j, temp;
	if(i != n){
		for(j=i;j<=n;j++){
			SWAP(list[i],list[j],temp);
			
			perm(list,i+1,n);
			SWAP(list[i],list[j],temp);
			
		}
	}
	else{
		for(j=0;j<=n;j++)
			printf("%c",list[j]);
		printf("  ");
	}
}