#include <iostream>
#include "perbackendconfig.hpp"
#include "changedir.hpp"


using std::cout;
using std::endl;

int main(int argc, char **argv){
    if(myFunction()==1){
    cout << endl << "Current working directory was: " << GetCurrentWorkingDirectory() << endl;

    cout << "Changing directory..." << endl;    

    std::string exedir = GetExecutableDirectory(argv[0]);

    ChangeDirectory(exedir.c_str());
    
    cout << "Current working directory is now: " << GetCurrentWorkingDirectory() << endl;
    }

    else if(myFunction()==0){}

    return 0;
}