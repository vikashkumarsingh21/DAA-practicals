#include <stdio.h>

int main(){
    int arr[]={10,20,30,40,80,100,2000,500,425};
    int num = 20;
    int low = 0;
    int high = 8;
    int found = 0;

    while (low <= high){
        int mid = low + (high - low) / 2;

        if (arr[mid] == num){
            printf("Element found at index %d", mid);
            found = 1;
            return 0;
        }
        else if (arr[mid] < num){
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }

    if(found == 0){
        printf("Element not found");
    }
    return 0;
}