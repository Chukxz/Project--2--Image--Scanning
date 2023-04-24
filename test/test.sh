#!/bin/bash

gcc -fPIC -shared -o test.so test.c -l sqlite3