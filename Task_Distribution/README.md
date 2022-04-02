# Task Distribution Project

Solving questions appeared in previous several years is very helpful to take proper preparation for term final examination. This short program will distribute all the questions to each student randomly. Throughout the semester if each student solve 3-4 problems, we can combined them at the end and make a solution book. Everyone gets to read the solution book. It will save a lot of time and help us take good preparation for the exam.

### Requirements

* Python
* Python Modules: pandas, openpyxl, itertools, random
  [How to Install Python Module](https://youtu.be/7snh_1Hf_TI)
* Optional:
    * Jupyter Notebook [Get Started With Jupyter Notebook in Visual Studio Code](https://youtu.be/h1sAzPojKMg)

### Procedure

#### Step-1

    Create an excel file with two sheets.
    * 1st sheet contains the question data in the following format:

        |   Year   | MME213 | ME221 | ... |
        |----------|--------|-------|-----|
        |  2018-19 |    8   |   8   | ... |
        |  2017-18 |    8   |  12   | ... |
        | ... ...  |   ...  | ...   | ... | 

        First column containes the **academic sessions**.
        Rest of the columns containes the **total number of questions appeared in each course**.
    
    * 2nd sheet contains the Roll No.'s of the students in the following format:

        | Roll No. |
        |----------|
        |    1     |
        |    2     |
        |    3     |
        |    4     |
        |   ...    |

     **Make sure the question data sheet is before the roll no. sheet**

#### Step-2

#### Using Python File

    * Open "task_distribution.py" script.
    * Set the Question Datafile Name and Output file name.

        ```python
        data_file = "ques_data.xlsx"    # Question Datafile name
        output_file = "output.xlsx"     # Output file name
        ```
    * Run Code.

#### Using Jupyter Notebook:

    * Open "Task_Distribution.ipynb"
    * Set the Question Datafile Name and Output tile name.
    * Run each cell step by step.

Random distribution data will be saved on the same directory in a excel file.