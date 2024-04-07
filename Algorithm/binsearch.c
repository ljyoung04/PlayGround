#include <stdio.h>
#define ARR_SIZE 10
int binsearch(int arr[], int left, int right, int target){
    while(left <= right){
        int mid = (left + right)/2;

        if(arr[mid] == target)
            return mid;
        if(arr[mid] < target)
            left = mid + 1;
        else
            right = mid -1;
    }
    return -1;
}

int main() {
    int target,res;
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    printf("What do you want to find? : ");
    scanf("%d", &target);
    res = binsearch(arr,0,ARR_SIZE-1,target);

    if(res == -1)
        printf("Can not found!");
    else
        printf("%d is located %d",target,res);

    return 0;
}