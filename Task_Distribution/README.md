# Task Distribution Project

Solving questions appeared in previous several years is very helpful to take proper preparation for term final examination. This short program will distribute all the questions to each student randomly. Throughout the semester if each student solve 3-4 problems, we can combined them at the end and make a solution book. Everyone gets to read the solution book. It will save a lot of time and help us take good preparation for the exam.

### Used Python Packages

* numpy
* pandas
* openpyxl
* itertools
* random

### Procedure

1. Create a excel file (say 'ques_data.xlsx') in the following format:

    |   Year   | COURSE-1 | COURSE-2 | ... |
    |----------|----------|----------|-----|
    |  2018-19 |    8     |     8    | ... |
    |  2017-18 |    8     |     12   | ... |
    | ... ...  |   ...    |    ...   | ... | 

    The first column must be named **'Year'**. Otherwise code won't work.

2. Open 'Task_Distribution.ipynb'
3. Set the value of total number of students:

    ```python
    n = 60  # Total number of students is 60
    ```
4. Set excel file name (Here 'ques_data.xlsx' was used):

    ```python
    df = pd.read_excel('ques_data.xlsx').astype({'Year':"string"})
    ```
5. Run every cells step by step.
6. At the last cell set Output file name (Here 'output.xlsx' was used) and run the cell:

    ```python
    dist.to_excel("output.xlsx",index=False)    # Saves the "dist" dataframe to "output.xlsx" file
    ```
   It will save the random distribution data on the same directory. 