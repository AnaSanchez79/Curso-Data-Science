target = 200
ways = 0

a = target
while a >= 0 :
    b = a 
    while b >= 0 :
        c = b
        while c >= 0 :
            d = c
            while d >= 0 :
                e = d
                while e >= 0 :
                    f = e 
                    while f >= 0 :
                        g = f 
                        while g >= 0 :
                            ways = ways + 1
                            g = g - 2
                        f = f -5
                    e = e - 10
                d = d -20
            c = c -50
        b = b - 100
    a = a - 200
    
print(ways)