def sum_all(*args):
    
    for i in args: #can use loops in args as it is iterable 
        print(i + 2)
    return sum(args)

print(sum_all(1,2,3,4,5))

