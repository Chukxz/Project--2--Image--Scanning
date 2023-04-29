#Configure file location for my computer will differ on your computer if you don't modify it.
from os import chdir,getcwd

def testconfigure():
    location = getcwd()
    if not "Web Projects 2\Project-2-Image-Scanning-Backend" in location:
        try:
           chdir(r"C:\Users\USER\Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
        except FileNotFoundError:
            try:
                chdir(r"Users\USER\Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
            except FileNotFoundError:
                try:
                    chdir(r"USER\Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
                except FileNotFoundError:
                    try:
                        chdir(r"Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
                    except FileNotFoundError:
                        try:
                            chdir(r"My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
                        except FileNotFoundError:
                            try:
                                chdir(r"Web Projects 2\Project-2-Image-Scanning-Backend")
                            except FileNotFoundError:
                                try:
                                    chdir(r"Project-2-Image-Scanning-Backend")
                                except FileNotFoundError:
                                    print("Automatic configuration failed, configure directory manually")

if __name__ != "__main__":
    def configure():
        r"""Custom module for configuring the current working directory of the program during runtime to
            "C:\\Users\\USER\\Documents\\My Homepage files\\Web Projects 2\\Project-2-Image-Scanning-Backend".
            It's a custom function that I implemented that helps me to open files without worrying much about the path I'm
            in as long as I'm in the directory above or in a parent path relative to it.
        """
        testconfigure()
else:
    testconfigure()
    print("Running Locally")
    print(getcwd())
