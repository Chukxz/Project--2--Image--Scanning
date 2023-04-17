#include <stdio.h>
#include "sqlite3.h"

int main(int argc, char* argv[]){
    const char * file;

    printf("Opening image and getting image data...");
    file = "Resources/Generated_Images/Pipe Puzzle/Pipe Puzzle Pixel.db";

    sqlite3 * db;
    // char *zErrMsg = 0;
    int rc;
    rc = sqlite3_open(file, &db);

    if (rc){
        fprintf(stderr,"Can't open database: %s\n", sqlite3_errmsg(db));
        return (0);
    } else {
        fprintf(stderr, "Opened database successfully\n");
    }
    sqlite3_close(db);

    return 0;
}