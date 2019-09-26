import random

num_set={2,6,4,98,6,42,11,96,33}

print(num_set)
print(len(num_set))

name_list=['Adam','Barry','Doug','Cathy','Ellen']
volunteers=set(random.sample(name_list,3))
qualified=set(random.sample(name_list,3))

print('Volunteers:',volunteers)
print('Qualified:',qualified)

new_team=volunteers.intersection(qualified)
print('New Team', new_team)