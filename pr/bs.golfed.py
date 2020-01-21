def bs(a,k,l,h):
    if l>h:return-1
    m=(l+h)//2;n=a[m];return(k>n and bs(a,k,l+1,h))or(k<n and bs(a,k,l,h-1))or m
