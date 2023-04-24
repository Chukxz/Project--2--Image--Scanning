#include <stdio.h>
#include "sqlite3.h"

#ifndef EXAMPLES
#define EXAMPLES

int operate(const char * op){
    sqlite3 * db;
    // char *zErrMsg = 0;
    int rc;
    rc = sqlite3_open(op, &db);

    if (rc){
        fprintf(stderr,"Can't open database: %s\n", sqlite3_errmsg(db));
        return (0);
    } else {
        fprintf(stderr, "Opened database successfully\n");
    }
    sqlite3_close(db);
    return 0;
}

#endif
