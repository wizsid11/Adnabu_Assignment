import numpy as np
a=["hello world python","scala world","java python scala hello world","world python hello","world hello","python clojure java world"]
b =  ["hello world python","python world","python"]
c=["scala world","python closure world scala"]
root_list=[]
ans=dict((s,[1,s.split(" "),len(s.split(" "))]) for s in a)# creating the ans dict
all_lengths = np.array(list(set(map(lambda x:x[2],ans.values())))).tolist()
min_length = np.array(list(set(map(lambda x:x[2],ans.values())))).min()# calculating the minimum length
for key,value in ans.items():
	if value[2]==min_length:
		root_list.append(key)
all_lengths.remove(min_length)
for l in all_lengths:
	for key,value in ans.items():
		if value[2]==l:
			for r in root_list: 
				if (set(ans[r][1]).issubset(set(value[1]))):
					ans[key][0]=0
					break;
			if ans[key][0]==1:
				root_list.append(key)
print root_list