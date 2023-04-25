#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int * getValues(int lineValue, char *filename, char * buffer, int * hold, char store[]){
    
    char * _a;
    char * _b;
    char * _c;
    int a;
    int b;
    int c;

    char delim[] = "(,)";
    for(int i = 0; i < 3; i++){
        if(i==0){
           _a = strtok(store,delim); 
        }
        if(i==1){
            _b = strtok(NULL,delim);
        }
        if(i==2){
            _c = strtok(NULL,delim);
        }
    }

    a = (int) strtol(_a,NULL,10);
    b = (int) strtol(_b,NULL,10);
    c = (int) strtol(_c,NULL,10);

    hold[0] = a;
    hold[1] = b;
    hold[2] = c;

    return hold;
}

