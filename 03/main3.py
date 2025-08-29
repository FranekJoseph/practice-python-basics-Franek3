def find_max_number (a,b,c):
    if a > b and a> c:
        return a
    if b > a and b> c:
        return b
    if c > a and c > b:
        return c
    elif a == b == c:
        return a,b,c
        
