import numpy as np
a=["hello world python","scala world","java python scala hello world","world python hello","world hello","python clojure java world"]
b =  ["hello world python","python world","python"]
parent_list=[]
ans=dict((s,[0,s.split(" "),len(s.split(" "))]) for s in a)# creating the ans dict
all_lengths = np.array(list(set(map(lambda x:x[2],ans.values())))).tolist()
min_length = np.array(list(set(map(lambda x:x[2],ans.values())))).min()# calculating the minimum length
for key,value in ans.items():
	if value[2]==min_length:
		ans[key][0]=1
		parent_list=list(set(parent_list+value[1]))# creating the parent list from string of minimu length 
all_lengths.remove(min_length)
for l in all_lengths:
	for key,value in ans.items():
		if value[2]==l:
			if(len(set(value[1]))>=len(set(parent_list))):
				if(len(set(value[1])-set(parent_list)))>1:
					ans[key][0]=1# changing boolean value
					parent_list=list(set(parent_list+value[1]))# updating parent list
				else:
					parent_list=list(set(parent_list+value[1]))
			elif(len(set(parent_list))>=len(set(value[1]))):
				if(len(set(parent_list)-set(value[1])))>1:
					ans[key][0]=1# changing boolean value
					parent_list=list(set(parent_list+value[1]))# updating parent list
				else:
					parent_list=list(set(parent_list+value[1]))# no change in boolean value only updating parent list
for key,value in ans.items():
	if value[0]==1:
		print key