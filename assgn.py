f=open('testcases.txt','r')
text=f.read()
test_cases=text.split("\n")
ans=dict((s,[1,set(map(lambda x:(x,s.strip().split(" ").count(x)),s.strip().split(" "))),len(s.strip().split(" "))]) for s in test_cases)# creating the ans dict
root_list=set()
key_log=ans.keys()
key_log.sort(key=len)
for key in key_log:
		for r in root_list: 
			if (set(ans[r][1]).issubset(ans[key][1])):# check for subset
				ans[key][0]=0
				break;
		if ans[key][0]==1:
			root_list.add(key)# update root list
print root_list