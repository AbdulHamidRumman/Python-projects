# Task Distribution Project

Solving questions appeared in previous several years is very helpful to take proper preparation for term final examination. This short program will distribute all the questions to each student randomly. Throughout the semester if each student solve 3-4 problems, we can combined them at the end and make a solution book. Everyone gets to read the solution book. It will save a lot of time and help us take good preparation for the exam.

### Used Python Packages

* numpy
* pandas
* openpyxl
* itertools
* random

### Procedure

1. Create a excel file (say "ques_data.xlsx") in the following format:

    |   Year   | COURSE-1 | COURSE-2 | ... |
    |----------|----------|----------|-----|
    |  2018-19 |    8     |     8    | ... |
    |  2017-18 |    8     |     12   | ... |
    | ... ...  |   ...    |    ...   | ... | 

    The first column must be named **'Year'**. Otherwise code won't work.

    In case of optional courses. Create another sheet in the excel file in the following format:

    | Optinal_COURSE-1 | Optinal_COURSE-2 | ... |
    |------------------|------------------|-----|
    |        2         |        1         | ... |
    |        5         |        3         | ... |
    |        7         |        8         | ... |
    |       10         |       12         | ... |
    |      ...         |      ...         | ... |

    **First Column** contains the roll numbers of the students who took **Optional_COURSE-1**
    **Second Column** contains the roll numbers of the students who took **Optional_COURSE-2**

    **Make sure the optional course datasheet is after the Question Datasheet**

2. Open 'Task_Distribution.ipynb'
3. Set the total number of students, Question Datafile Name and Output file name in the 2nd Cell:

    ```python
    N = 60                          # Total number of students is 60
    data_file = "ques_data.xlsx"    # Question Datafile name
    output_file = "output.xlsx"     # Output file name
    ```
4. Run every cells step by step.
5. Random distribution data on the same directory in a excel file. 