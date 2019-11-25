f=open('deliveries.csv', 'r')
delivery_data=f.read()
delivery_data1=list(delivery_data.rstrip().split('\n'))
#print(delivery_data1)

delivery_stats=[]
for delivery in delivery_data1:
    delivery_stat=list(delivery.split(','))
    delivery_stats.append(tuple(delivery_stat))

print(delivery_stats[12345])
