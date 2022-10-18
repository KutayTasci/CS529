import numpy as np
import sys


f_event = open("assignment2_data/events_nodeset.csv", "r")
events_ls = f_event.read().splitlines()
events = {}

for i, node in enumerate(events_ls[1:]):
    events[i] = node.split(",")[0]
events_inv = {v: k for k, v in events.items()}
print(events)

f_people = open("assignment2_data/people_nodeset.csv", "r")
people_ls = f_people.read().splitlines()
people = {}

for i, node in enumerate(people_ls[1:]):
    people[i] = node.split(",")[0]
people_inv = {v: k for k, v in people.items()}
print(people)

f_links = open("assignment2_data/people_by_events_edge_list.csv", "r")
links_ls = f_links.read().splitlines()
event_people_mat = np.zeros((len(events), len(people)))


for i in links_ls[1:]:
    source, target = i.split(",")[0], i.split(",")[1]
    ev = events_inv[target]
    pe = people_inv[source]
    event_people_mat[ev][pe] = 1

people_people_mat = np.matmul(event_people_mat.T, event_people_mat)
event_event_mat = np.matmul(event_people_mat, event_people_mat.T)

original_stdout = sys.stdout
with open('Event-Event/Adjacency_Matrix_KutayTasci.csv', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    for i in events.items():
        print(","+str(i[1]), end="")
    for i in events.items():
        print("\n"+str(i[1]), end="")
        for j in events.items():
            print(","+str(event_event_mat[i[0]][j[0]]), end="")
    sys.stdout = original_stdout

with open('People-People/Adjacency_Matrix_KutayTasci.csv', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    for i in people.items():
        print(","+str(i[1]), end="")
    for i in people.items():
        print("\n"+str(i[1]), end="")
        for j in people.items():
            print(","+str(people_people_mat[i[0]][j[0]]), end="")
    sys.stdout = original_stdout



