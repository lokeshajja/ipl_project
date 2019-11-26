'''
1. extract the data files
2. extract bowler number of overs and runs given in each over
   2.1. initialize a bowlers account on new bowler 
        count over change on change of bowler
        until then add the runs to bowlers account
   2.2. in each iteration of initiated temp count number of runs by the bowler

3.form the data calculate number of overs of each bowler and runs conceded by him
4. from this data plot the graph of the relevant
'''





from file_extraction import extract_file
from plot_of_task4 import compute_and_plot_most_economic_bowlers_of_2015





def main():
    matches=extract_file('matches.csv')
    deliveries_data=extract_file('deliveries.csv')
    compute_and_plot_most_economic_bowlers_of_2015(matches,deliveries_data)




if __name__=="__main__":
    main()