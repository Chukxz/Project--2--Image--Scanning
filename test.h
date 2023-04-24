#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char returnLine(int lineValue, char *filename1){

    FILE * fptr = fopen(filename1,"r");

    if(fptr == NULL){
        printf("Error opening file!");
        // Program exits if the file pointer returns NULL.
        return -1;
    }

    char buffer[100];

    for(int i=1; i<=lineValue; i++){
        fgets(buffer,100,fptr);
    }

    fclose(fptr);
    return *(buffer);
}