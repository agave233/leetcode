def isMatchSeatch(s,index,tag,m,n):
	if m == len(s):
		for i in range(n,len(index)):
			if tag[i] == 0:
				return False
		return True
	if n == len(index):
		if m < len(s):
			return False
		return True

	if tag[n]:
		if index[n] == '.':
			if isMatchSeatch(s,index,tag,m+1,n) == True:
				return True
			if isMatchSeatch(s,index,tag,m,n+1) == True:
				return True
		elif index[n] == s[m]:
			if isMatchSeatch(s,index,tag,m+1,n) == True:
				return True
			if isMatchSeatch(s,index,tag,m,n+1) == True:
				return True
		else:
			if isMatchSeatch(s,index,tag,m,n+1) == True:
				return True
	else:
		if index[n] == s[m]:
			if isMatchSeatch(s,index,tag,m+1,n+1) == True:
				return True
		else:
			return False
	return False

s = "abbbbbbbbbbbbbbbbbbbbbaccccccba"
p = "ab*a*c*a"
dfa = []
tag = []
j = 0
for i in range(len(p)):
    if(p[i] == '*'):
    	tag[j - 1] = 1
    else:   
        dfa.append("")
        tag.append("")
        dfa[j] = p[i]
        tag[j] = 0
        j = j + 1
print dfa
print tag
print isMatchSeatch(s,dfa,tag,0,0)