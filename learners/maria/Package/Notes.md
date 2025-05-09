#A simple project
#This tutorial uses a simple project named example_package_YOUR_USERNAME_HERE. If your username is me, then the #package would be example_package_me; this ensures that you have a unique package name that doesn’t conflict with #packages uploaded by other people following this tutorial. We recommend following this tutorial as-is using this #project, before packaging your own project.

#Create the following file structure locally:

packaging_tutorial/
└── src/
    └── example_package_YOUR_USERNAME_HERE/
        ├── __init__.py
        └── example.py
#The directory containing the Python files should match the project name. This simplifies the configuration and is #more obvious to users who install the package.

#Creating the file __init__.py is recommended because the existence of an __init__.py file allows users to import #the directory as a regular package, even if (as is the case in this tutorial) __init__.py is empty. [1]

#example.py is an example of a module within the package that could contain the logic (functions, classes, #constants, etc.) of your package. Open that file and enter the following content:

def add_one(number):
    return number + 1
#If you are unfamiliar with Python’s modules and import packages, take a few minutes to read over the Python #documentation for packages and modules.

#Once you create this structure, you’ll want to run all of the commands in this tutorial within the #packaging_tutorial directory.