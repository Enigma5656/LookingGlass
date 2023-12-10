# Author- Connor Dedic
# Date- 12/9/2023
# Summary- Main program

# Importing functions
from operator import le
import LookingGlassLib as lgl
from pandas import DataFrame, set_option
import time


def main():
    # initalizing lists
    matches_list = []
    possible_score_list = []
    scores_list = []

    # Defining Variables
    # Change ---V--- this number to change the maximum edit distance
    max_score = 2
    length_incor = lgl.lenOfList(correctlist=False)
    length_cor = lgl.lenOfList(correctlist=True)

    # Start timer
    start_time = time.time()
    print(f'\n')
    # Data loop
    # It begins by selecting number in the first list
    for i in range(length_incor):
        # Sets the current number to the number with the present index
        current_val = str(lgl.readLst(i, 'Incorrect.csv')).replace('\n', '')
        # These lines make the timer and progress update run
        timer = time.time()
        present_time  = (timer - start_time) / 60
        progress = (i / length_incor) * 100
        time_left = (present_time + 0.001) * ((100-progress) / (progress + 0.001))
        # color
        print(f'\u001b[37;1mtime since start: \u001b[34;1m{present_time:.2f}\u001b[37;1m min; time left:\u001b[35;1m {time_left:.1f}\u001b[37;1m min; percent complete: \u001b[36;1m{progress:.1f}%; \u001b[37;1miteration: \u001b[32;1m{i}\u001b[37;1m', end= '\r')
        # no color
        # print(f'time since start: {present_time:.2f} min; time left: {time_left:.1f} min; percent complete: {progress:.1f}%; iteration: {i}')
        for i in range(length_cor):
            # This loop sets the comparison number to the number matching the 
            # index of this loop
            comparison_val = str(lgl.readLst(i, 'Correct.csv')).replace('\n', '')
            # Then scores the numbers here
            current_score = lgl.scoreCalc(current_val, comparison_val)
            # print(f'{current_val}, {comparison_val}, {current_score}', end='\n')
            # If the first digit in the variables are the same 
            # this conditional activates
            # if current_val[0] == comparison_val[0]:
                # if the edit distance is within the allowed range:
                # max_score >= current_score > 0 
                # then this conditional activates
            if current_score <= max_score and current_score != 0:
                # It then adds them to the lists initalized above
                matches_list.append(current_val)
                possible_score_list.append(comparison_val)
                scores_list.append(current_score)
                
                    # data[current_val] = comparison_val, current_score
            
    # The lists are then compiled into this dataframe as a dictionary, with 
    # corresponding keys that will become columns
    data_frame = DataFrame({'Matches' : matches_list, 
            'Possible Match' : possible_score_list,
            'Score of pair' : scores_list
            })

    # If printing a dataframe in the console uncomment these lines
    set_option('display.max_rows', None)
    set_option('display.max_columns', None)
    set_option('display.width', None)
    set_option('display.max_colwidth', None)
    print('\n')
    print(data_frame)

    # If saving dataframe to a csv, uncomment this line
    # data_frame.to_csv(r'output.csv')

main()
