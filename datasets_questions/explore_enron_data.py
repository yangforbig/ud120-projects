#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import os
#print os.getcwd()
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
count = 0
f = open('../final_project/poi_names.txt','r')
namelist = []

def modname(name):
    return name.strip(name[-1]).strip()

for line in f:
    line = line.upper().replace(',','')
    #print line
    for name in enron_data.keys():
        if enron_data[name]['poi'] == 1:
            #print name
            if name.strip(name[-1]).strip() in line:
                #print name
                count = count + 1
features = enron_data[enron_data.keys()[0]].keys()
print features

for name in enron_data.keys():
    namelist.append(name.strip(name[-1]).strip())
namelist = sorted(namelist)
print namelist

# stock option for Jeff Skilling
'''
for name in enron_data.keys():
    mod_name = modname(name)
    if mod_name == 'SKILLING JEFFREY':
        print enron_data[name]['exercised_stock_options']
'''

'''
for name in enron_data.keys():
    mod_name = modname(name)
    if mod_name == 'SKILLING JEFFREY':
        Ski = enron_data[name]['total_payments']
    if mod_name == 'FASTOW ANDREW':
        Fast = enron_data[name]['total_payments']

#print Ski, Fast
print enron_data['LAY KENNETH L']['total_payments']
'''

#how is an unfilled feature denoted?
'NaN'
#how many folks in this dataset have a quantified salary? Known email addres
