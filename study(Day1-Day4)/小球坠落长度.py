def distance(high):
    d=0
    for i in range(10):
        d+=high#记录走过的距离
        high=high*0.5
        d+=high
        print(d)

distance(100)
     