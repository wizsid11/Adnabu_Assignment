import numpy as np
a=["hello world python","scala world","java python scala hello world","world python hello","world hello","python clojure java world"]
b = ["hello world python","python world","python"]
c=["scala world","python closure world scala"]
ans=dict((s,[1,s.split(" "),len(s.split(" "))]) for s in a)# creating the ans dict
root_list=[]
all_lengths = list(set(map(lambda x:x[2],ans.values())))
min_length = np.array(all_lengths).min()# calculating the minimum length
for key,value in ans.items():
	if value[2]==min_length:
		root_list.append(key)
root_list=list(set(root_list))# remove duplicate strings
all_lengths.remove(min_length)
for key,value in ans.items():
		for r in root_list: 
			if (set(ans[r][1]).issubset(set(value[1]))):# check for subset
				ans[key][0]=0
				break;
		if ans[key][0]==1:
			root_list.append(key)# update root list
print root_list
# for l in all_lengths:
# 	for key,value in ans.items():
# 		if value[2]==l:
# 			for r in root_list: 
# 				if (set(ans[r][1]).issubset(set(value[1]))):# check for subset
# 					ans[key][0]=0
# 					break;
# 			if ans[key][0]==1:
# 				root_list.append(key)# update root list
# print root_list