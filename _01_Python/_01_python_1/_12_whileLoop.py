i=1;
while(i<=5) :
    print(i);
    i=i+1;
    
# 2

# 
a = input("Enter A string   ");
i=0;
while(i< len(a)):
    if(a[i] not in ['a','e','i','o','u','A','E','I','O','U']):
        print(a[i]);
    
    i=i+1;