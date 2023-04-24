#!/bin/bash

gcc -shared database.c -l sqlite3 -o database