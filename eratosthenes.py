req_list = range(2,102)
mainlist = req_list
j = 0
check = 2
count = 1
index = count
while(check*check <= mainlist[-1]):
	ind = req_list.index(check)+ 1

	while(ind<len(req_list)):
		if req_list[ind]%check == 0:
			del req_list[ind]
		ind+=1
	j+=1
	check = req_list[j]
print req_list,len(req_list)
