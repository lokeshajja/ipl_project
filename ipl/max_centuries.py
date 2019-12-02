from file_extraction import extract_file



def plot_max_centuries(plot_data):
    pass

def compute_centuries_data_over_all_years():
    matches=extract_file('matches.csv')
    deliveries_data=extract_file('deliveries.csv')




    ids_yearwise={}
    def year_wise_ids(matches):
        for id_data in matches: 
            if id_data['season'] not in ids_yearwise:
                ids_yearwise[id_data['season']]={}
        #print(ids_yearwise)
        ids_yearwise1={}
        for year in sorted(ids_yearwise.keys()):
            ids_yearwise1[year]={}
        #print(ids_yearwise1)

        return ids_yearwise1
        

    def ids_of_each_year(year_wise_data):
        print(year_wise_data)
        

        for mat in matches:
            year_wise_data[mat['season']][mat['id']]={}
        #print(year_wise_data)

        return year_wise_data


    def batsman_wise_data(year_wise,deliveries_data):
        #print(year_wise)
        
        
        for del_data in deliveries_data:
            for year in year_wise:
                if del_data['match_id'] in year_wise[str(year)]:
                    if del_data['batsman'] not in year_wise[str(year)][del_data['match_id']]:
                        year_wise[str(year)][del_data['match_id']][del_data['batsman']] = int(del_data['batsman_runs'])
                    elif del_data['batsman'] in year_wise[str(year)][del_data['match_id']]:
                        year_wise[str(year)][del_data['match_id']][del_data['batsman']] += int(del_data['batsman_runs'])
                    

        #print(year_wise)      
        return year_wise      
#print(mat_data['season'],mat_data['id'],i)
    
    def centuries_year_wise(matches,scores_year_wise,cent_per_year):
        
        for mat_data in matches:
            for i in scores_year_wise[mat_data['season']][mat_data['id']]:
                if int(scores_year_wise[mat_data['season']][mat_data['id']][i])>=100:
                    if i not in cent_per_year[mat_data['season']]:
                        cent_per_year[mat_data['season']][i]=1
                    elif i in cent_per_year[mat_data['season']]:
                        cent_per_year[mat_data['season']][i] += 1

        #print(cent_per_year)


                    



                    


            
            




                

                

            



            
        




    year_wise_data=year_wise_ids(matches)
    cent_per_year=year_wise_ids(matches)
    year_wise=ids_of_each_year(year_wise_data)
    scores_year_wise=batsman_wise_data(year_wise,deliveries_data)
    centuries_year_wise(matches,scores_year_wise,cent_per_year)
    #print(cent_per_year)

            

def ids_of_each_year(year_wise_data,mock_matches):
        print(year_wise_data)
        

        for mat in mock_matches:
            year_wise_data[mat['season']][mat['id']]={}
        #print(year_wise_data)

        return year_wise_data
    