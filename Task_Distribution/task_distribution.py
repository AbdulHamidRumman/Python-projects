import pandas as pd
import itertools
import random

data_file = "ques_data.xlsx"    # Question Datafile name
output_file = "output.xlsx"     # Output file name

def read_data(file):
    """
        This function reads sheets in the excel file and collects the Question Data and Roll Numbers

        Parameters:
        ----------
        file -> Question Data file name

        Returns:
        -------
        df      -> Question Dataframe from 1st sheet
        roll_df -> Roll No. Dataframe from 2nd sheet
        
    """

    data = pd.read_excel(file,sheet_name=None)
    sheet = list(data.keys())
    col1 = data[sheet[0]].columns.to_list()[0]
    df = data[sheet[0]].astype({col1:"string"})
    roll_df = data[sheet[1]]
    
    return df,roll_df

def extract_ques(table):
    """
        This function Extracts All the Questions from the "table" dataframe and creates a list "q_list"
        
        Parameters:
        ----------
        table   -> A dataframe containing "Year" in the first column and "Course Code" in the rest of the columns
        q_list  -> A list of strings having the questions in the format of "CourseCode-Year-(Ques.No.)"

        Returns:
        -------
        q_list  -> List of Questions
        
    """
    q_list = []
    y = table.columns.to_list()[0]                                      # Year Column or First Column
    crs = table.columns.to_list()[1:]                                   # Rest of the columns containing the course no.
    r = len(table.index)
    for c in crs:                            
        for i in range(r): 
            yr = table.loc[i,y]                                         # Each Year
            qs_n = table.loc[i,c]                                       # No. of Questions
            q_no = [str(j) for j in range(1,qs_n+1)]                    # Creates a string list of question no.
            lst_per = list(itertools.product(*[[c],[yr],q_no]))         # List of all question in 'yr' year in 'c' Course
            for k in lst_per:
                crs_code,year,ques_no = k                                                
                q_list.append(crs_code+'-'+year+'-'+'('+ques_no+')') 
    
    return q_list

def random_dist(st_df,q_list):
    """
        This Function Distributes each questions of "q_list" to dataframe "st_df"
        * It creates new columns named Task1, Task2, ...
        * In each column it distrubutes questions randomly.
        * Each time this function is called the "st_df" will change randomly

        Parameters:
        ----------
        st_df   -> Dataframe containing students roll no.
        q_list  -> List of all questions generated from extract_ques() function
        
    """

    n = st_df.index.size
    ts = 1  # Task No.                                    
    while len(q_list):
        if len(q_list)<n:
            remain = n-len(q_list)
            for _ in range(remain):
                q_list.append('-')    
        sample = random.sample(q_list,n)
        for _ in range(n):
            random.shuffle(sample)
        st_df['Task'+str(ts)] = pd.Series(sample)
        ts = ts+1
        for q in sample:
            q_list.remove(q)
    
    return None


df, roll_df = read_data(data_file)
ques_list = extract_ques(df)
random_dist(roll_df,ques_list)
roll_df.to_excel(output_file,index=False)       # Saves the "roll_df" dataframe to output file