def can_be_palindrome(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
        c=0
    for v in d.values():

       if v%2!=0:
            c=c+1
       if c>1:
         print("no")
       else:
         print("yes")

s="malayalam"
can_be_palindrome(s)
        
