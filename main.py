"""The Programming Formalisms Learners Project.

Project used in the UPPMAX Programming Formalisms course.

You need to have the weather Python package installed.

Tip: run './scripts/install_this_package.sh'
"""

from weather.reader import (
    read_data,
)

if __name__ == "__main__":
    read_data("data/uppsala_tm_1722-2022.dat")
