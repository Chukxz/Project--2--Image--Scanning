#!/bin/bash

g++ -fPIC -shared -o myfunc.so myfunc.c -l sqlite3

echo "Done."