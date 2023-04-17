#!/bin/bash
g++ -fPIC -shared -o example2.so example2.c -l sqlite3

echo "Done."