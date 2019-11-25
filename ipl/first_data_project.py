
import os

os.system('cls')


f1=open('AAPL.csv','r')
f1_data=f1.read()

f2_split_data=list((f1_data.rstrip().split("\n")))
print(f2_split_data)


f3_split_data=[]


for item in f2_split_data:
    f3_split_data.append((list(item.split(','))))


f2_index_values=f3_split_data[0]
#print(f2_index_values)

#print(f3_split_data[1])
main_data={}

for i in f3_split_data[1:]:
    d_d=list(zip(f2_index_values[1:],i[1:]))
    #print(d_d)
    date_data=dict(d_d)
    main_data[i[0]]=date_data


#print(main_data['2019-11-20'])





    



    



