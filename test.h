#include <stdio.h>
#include <stdlib.h>

char * _return_line_value_(int lineValue, char *filename, char * buffer){

    FILE * fptr = fopen(filename    ,"r");
    if(fptr == NULL){
        printf("Error opening file!");
        // Program exits if the file pointer returns NULL.
        exit(1);
    }

    for(int i=1; i<=lineValue; i++){
        fgets(buffer,100,fptr);
    }

    fclose(fptr);
    return buffer;
}