#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

data_dict.pop('TOTAL', 0)

data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

### your code below

outlier = [2.67042290e+07, 9.73436190e+07]
data_keys = data_dict.keys()
# print 'salary', data_dict[data_keys[0]]['salary']

# Find key with outlier salary
# for key in data_keys:
#   if data_dict[key]['salary'] == outlier[0]:
#     print 'This is the outlier ', key

# for key in data_keys:
#   if data_dict[key]['salary'] == 'NaN' or data_dict[key]['bonus'] == 'NaN':
#     continue
#   if int(data_dict[key]['salary']) > 1000000 and int(data_dict[key]['bonus']) >= 5000000:
#     # print key
#     # print data_dict[key]['salary']
#     print key

print data_dict['LAY KENNETH L']
print
print '**********************************************************************************************************'
print
print data_dict['SKILLING JEFFREY K']
