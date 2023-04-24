#include <stdio.h>
#include <stdlib.h>
#include "sqlite3.h"

int runsqlite3(int width, int height){
    sqlite3 * db;
    // char *zErrMsg = 0;
    int rc;
    rc = sqlite3_open("Pixel.db", &db);

    if (rc){
        fprintf(stderr,"Can't open database: %s\n", sqlite3_errmsg(db));
        return (0);
    } else
        fprintf(stderr, "Opened database successfully\n");
    
    // char const* const filename = ".store.txt";
    // FILE *fptr = fopen(filename,"r");
    // const unsigned MAX_LENGTH = 128;
    // char buffer[MAX_LENGTH];

    // while(fgets(buffer,sizeof(MAX_LENGTH),fptr)){
    //     printf("%s",buffer);
    // };

    /* Create SQL statement */

    sqlite3_close(db);

    printf("width of image is %d and height of image is %d",width,height);

    return 0;
}