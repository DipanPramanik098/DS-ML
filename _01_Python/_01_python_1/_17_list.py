x = [1, 2, 3, 4, 5, 6]

def print_elements(x):
    for i in range(len(x)):
        print(x[i])

print_elements(x)


# search
def search(x,key):
    for i in range(len(x)):
        if x[i] == key:
            return True;
    return False;

print(search(x,1));
print(search(x,11));