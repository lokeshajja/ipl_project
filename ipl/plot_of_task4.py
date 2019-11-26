from matplotlib import pyplot as plt



def compute_and_plot_match_of_2015_1(ids_of_2015,deliveries_data):
    #print(ids_of_2015)
    bowler_data={}
    for del_data in deliveries_data:
        if del_data['match_id'] in ids_of_2015:
            if del_data['bowler'] not in bowler_data:
                bowler_data[del_data['bowler']]={}
                bowler_data[del_data['bowler']]['del']=1
                bowler_data[del_data['bowler']]['runs']=int(del_data['total_runs'])
            elif del_data['bowler'] in bowler_data:
                bowler_data[del_data['bowler']]['del']+=1
                bowler_data[del_data['bowler']]['runs']+=int(del_data['total_runs'])
            else:
                pass

    economy_data={}
    def economy_of_bowlers(bowler_data):
        for bowler,b_data in bowler_data.items():
            overs=int((b_data['del']))//6
            economy=int(b_data['runs'])/overs
            economy_data[bowler]=economy
            #print(b_data['del'])
            #print(b_data['runs'])
            #print(economy_data)

        return economy_data

    economy_stats=economy_of_bowlers(bowler_data)
    
    #print((economy_stats))
    rev_ec_status=[]
    for ecn in sorted(economy_stats,key=economy_stats.get):
        d_temp=(ecn,economy_stats[ecn])
        rev_ec_status.append(d_temp)

    #print(rev_ec_status)
    top_ec_bowlers=[]
    count=0
    for avg in rev_ec_status:
        if count<=10:
            top_ec_bowlers.append(avg)
            count+=1
        
            

    #print(top_ec_bowlers)
    bowler_x=[]
    avg_x=[]
    for bowl_r,avg1 in top_ec_bowlers:
        bowler_x.append(bowl_r)
        avg_x.append(avg1)

    #print(bowler_x)
    #print(avg_x)

    plt.bar(bowler_x,avg_x)
    plt.title('Most Economic Bowlers Of 2015')
    plt.xlabel('Bowlers')
    plt.ylabel('Economy')
    plt.setp(plt.gca().get_xticklabels(),rotation=30,horizontalalignment='right')
    plt.show()

def matches_played_in_2015(matches):
    ids_of_2k15=[]
    for match_data in matches:
        if match_data['season']=='2015':
            ids_of_2k15.append(match_data['id'])
            
    return ids_of_2k15
            
def compute_and_plot_most_economic_bowlers_of_2015(matches,deliveries_data):
    ids_of_2015=matches_played_in_2015(matches)
    compute_and_plot_match_of_2015_1(ids_of_2015,deliveries_data)


    
