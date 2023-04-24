#include <stdio.h>

void change(int * ar){
    ar[0] = 1;
}

void changes(char * arra){
    *(arra) = 'o';
}


int main(int argc, char * argv[]){

    int arr[50];
    char array[10];

    change(arr);
    changes(array);

    printf("%i",*arr);
    printf("%c",*array);
    
}