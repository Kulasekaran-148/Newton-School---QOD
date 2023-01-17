#include <stdio.h>
#include <stdlib.h>

void quicksort(long arr[], int low, int high);
int partition (long arr[], int low, int high);

int main() {
    long num_of_items, result=0, coupons, reducFactor;
    scanf("%ld %ld %ld",&num_of_items, &coupons, &reducFactor);
    long cost_array[num_of_items];
    for(int i=0;i<num_of_items;i++) {
        scanf("%ld",&cost_array[i]);
        if(cost_array[i] >= reducFactor) {
            if(coupons >= (cost_array[i]/reducFactor)) {
                coupons -= (cost_array[i]/reducFactor);
                cost_array[i] = cost_array[i] % reducFactor;
            } else {
                cost_array[i] -= (coupons * reducFactor);
                coupons = 0;
            }
        }
    }
    int zeroed_elements = 0;
    quicksort(cost_array, 0, num_of_items - 1);
    for(int i=0;i<num_of_items;i++) {
        if(cost_array[i] == 0) {
            zeroed_elements++;
        } else if (zeroed_elements < coupons) {
            zeroed_elements++;
            cost_array[i] = 0;
        }
        result += cost_array[i];
    }
    printf("%ld",result);
    return 0;
}

void quicksort(long arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

int partition (long arr[], int low, int high) {
    long pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high- 1; j++) {
        if (arr[j] >= pivot) {
            i++;
            long temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    long temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return (i + 1);
}