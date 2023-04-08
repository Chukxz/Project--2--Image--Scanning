#ifndef PERBACKENDCONFIG
#define PERBACKENDCONFIG

#include <filesystem>
#include <fstream>

using std::cout;
using std::endl;
namespace fs = std::filesystem;

int myFunction(){
    fs::path current_dir = fs::current_path();
    cout<< "Currrent directory: "<<current_dir<<endl;
    fs::path search_dir("C:/Users/USER/Documents/My Homepage files/Web Projects 2/Project-2-Image-Scanning-Backend");

    if(current_dir==search_dir){
        return 0;
    }
    else{
        return 1;
    }
    return 0;
}

#endif
