#!/bin/bash

gcc -fPIC -shared -o myfunc.so myfunc.c -l sqlite3
