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

2. Open 'Task_Distribution.ipynb'
3. Set the Question Datafile Name and Output file name:

    ```python
    data_file = "ques_data.xlsx"    # Question Datafile name
    output_file = "output.xlsx"     # Output file name
    ```
4. Run every cells step by step.
5. Random distribution data will be saved on the same directory in a excel file. 