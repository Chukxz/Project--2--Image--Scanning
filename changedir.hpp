#ifndef CHANGEDIR
#define CHANGEDIR

#ifdef _WIN32
    #include "direct.h"
    #define PATH_SEP '\\'
    #define GETCWD _getcwd
    #define CHDIR _chdir
#else
    #include "unistd.h"
    #define PATH_SEP '/'
    #define GETCWD getcwd
    #define CHDIR chdir
#endif

#include <cstring>
#include <string>
#include <iostream>
using std::string;

string GetExecutableDirectory(const char* argv0){
    string path = argv0;
    int path_directory_index = path.find_last_of(PATH_SEP);
    return path.substr(0,path_directory_index+1);
}

bool ChangeDirectory(const char* dir){return CHDIR(dir)==0;}

string GetCurrentWorkingDirectory(){
    const int BUFSIZE = 4096;
    char buf[BUFSIZE];
    memset(buf,0,BUFSIZE);
    GETCWD(buf,BUFSIZE-1);
    return buf;
}
#endif