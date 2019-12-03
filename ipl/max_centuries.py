from file_extraction import extract_file





def year_wise_ids(matches):
    
        ids_yearwise={}
        for id_data in matches: 
            if id_data['season'] not in ids_yearwise:
                ids_yearwise[id_data['season']]={}
        
        ids_yearwise_sorted={}
        for year in sorted(ids_yearwise.keys()):
            ids_yearwise_sorted[year]={}
        

        return ids_yearwise_sorted





def batsman_wise_data(year_wise,deliveries_data):

    for del_data in deliveries_data:
        for year in year_wise:
            if del_data['match_id'] in year_wise[str(year)]:
                if del_data['batsman'] not in year_wise[str(year)][del_data['match_id']]:
                    year_wise[str(year)][del_data['match_id']][del_data['batsman']] = int(del_data['batsman_runs'])
                elif del_data['batsman'] in year_wise[str(year)][del_data['match_id']]:
                    year_wise[str(year)][del_data['match_id']][del_data['batsman']] += int(del_data['batsman_runs'])
                
            
    return year_wise   





def centuries_year_wise(matches,scores_year_wise,century_per_year):
    
    for match in matches:
        for i in scores_year_wise[match['season']][match['id']]:
            if int(scores_year_wise[match['season']][match['id']][i])>=100:
                if i not in century_per_year[match['season']]:
                    century_per_year[match['season']][i]=1
                elif i in century_per_year[match['season']]:
                    century_per_year[match['season']][i] += 1


    return century_per_year





def ids_of_each_year(year_wise_data,matches):
        
    for match in matches:
        year_wise_data[match['season']][match['id']]={}
    

    return year_wise_data





def compute_centuries_data_over_all_years():

    matches=extract_file('matches.csv')
    deliveries_data=extract_file('deliveries.csv')
    year_wise_data=year_wise_ids(matches)
    cent_per_year=year_wise_ids(matches)
    year_wise=ids_of_each_year(year_wise_data,matches)
    scores_year_wise=batsman_wise_data(year_wise,deliveries_data)
    centuries_per_year=centuries_year_wise(matches,scores_year_wise,cent_per_year)
    print(centuries_per_year)