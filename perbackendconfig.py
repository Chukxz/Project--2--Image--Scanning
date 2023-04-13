#Configure file location for my computer will differ on your computer if you don't modify it.
import os

def testconfigure():
    location = os.getcwd()
    if not "Web Projects 2\Project-2-Image-Scanning-Backend" in location:
        try:
            os.chdir(r"C:\Users\USER\Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
        except FileNotFoundError:
            try:
                os.chdir(r"Users\USER\Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
            except FileNotFoundError:
                try:
                    os.chdir(r"USER\Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
                except FileNotFoundError:
                    try:
                        os.chdir(r"Documents\My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
                    except FileNotFoundError:
                        try:
                            os.chdir(r"My Homepage files\Web Projects 2\Project-2-Image-Scanning-Backend")
                        except FileNotFoundError:
                            try:
                                os.chdir(r"Web Projects 2\Project-2-Image-Scanning-Backend")
                            except FileNotFoundError:
                                try:
                                    os.chdir(r"Project-2-Image-Scanning-Backend")
                                except FileNotFoundError:
                                    print("Configure Directory Manually")

if __name__ != "__main__":
    def configure():
        r"""Custom module for configuring the current working directory of the program during runtime to
            "C:\\Users\\USER\\Documents\\My Homepage files\\Web Projects 2\\Project-2-Image-Scanning-Backend".
            It's a custom function that I implemented that helps me to open files without worrying much about the path I'm
            in as long as I am in the directory above or in a parent path relative to it.
        """
        testconfigure()
else:
    testconfigure()
    print("Running Locally")