from matplotlib import pyplot as plt





def economy_of_bowlers(bowler_data):

    economy_data={}
    for bowler,bowler_data in bowler_data.items():
        overs=int((bowler_data['balls']))//6
        economy=int(bowler_data['runs'])/overs
        economy_data[bowler]=economy
    

    return economy_data





def plot_top_economy_data(ordered_economy):

    top_economical_bowlers=[]
    count=0
    for avg in ordered_economy:
        if count<=10:
            top_economical_bowlers.append(avg)
            count+=1
    
    bowler=[]
    average=[]
    for ball,avg in top_economical_bowlers:
        bowler.append(ball)
        average.append(avg)

    plt.bar(bowler,average)
    plt.title('Most Economic Bowlers Of 2015')
    plt.xlabel('Bowlers')
    plt.ylabel('Economy')
    plt.setp(plt.gca().get_xticklabels(),rotation=30,horizontalalignment='right')
    plt.show()





def compute_matches_of_2015(ids_of_2015,deliveries_data):

    bowler_data={}
    for ball in deliveries_data:
        if ball['match_id'] in ids_of_2015:
            if ball['bowler'] not in bowler_data:
                bowler_data[ball['bowler']]={}
                bowler_data[ball['bowler']]['balls']=1
                bowler_data[ball['bowler']]['runs']=int(ball['total_runs'])
            elif ball['bowler'] in bowler_data:
                bowler_data[ball['bowler']]['balls']+=1
                bowler_data[ball['bowler']]['runs']+=int(ball['total_runs'])
            else:
                pass

    economy_statistics=economy_of_bowlers(bowler_data)
    ordered_economy=[]

    for economy in sorted(economy_statistics,key=economy_statistics.get):
        bowler_economy=(economy,economy_statistics[economy])
        ordered_economy.append(bowler_economy)


    plot_top_economy_data(ordered_economy)



    

def matches_played_in_2015(matches):
    ids_of_2015=[]
    for match_data in matches:
        if match_data['season']=='2015':
            ids_of_2015.append(match_data['id'])


    return ids_of_2015





def compute_and_plot_most_economic_bowlers_of_2015(matches,deliveries_data):
    ids_of_2015=matches_played_in_2015(matches)
    compute_matches_of_2015(ids_of_2015,deliveries_data)


    
