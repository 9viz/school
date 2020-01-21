def f(a,k,l,h):
	if l>h:return-1
	m=(l+h)//2;return(k>a[m]and f(a,k,l+1,h))or(k<a[m]and f(a,k,l,h-1))or m
