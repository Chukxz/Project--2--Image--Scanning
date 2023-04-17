#include <iostream>
#include "sqlite3.h"
#include <string>
#include "changedir.hpp"
#include "regex.h"
#include "changedir.hpp"

using std::cout;
using std::endl;


int main(int argc, char* argv[]){
    const char * file;

    cout<<"Opening image and getting image data..."<<endl;
    file = "Resources/Generated_Images/Pipe Puzzle/Pipe Puzzle Pixel.db";

    sqlite3 * db;
    char *zErrMsg = 0;
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



