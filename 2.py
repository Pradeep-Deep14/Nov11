def multi_func(x):
    if isinstance(x,str):
        return x[::-1]
    elif isinstance(x,int):
        if x%2 ==0:
            return "even"
        else:
            return "odd"
    elif isinstance(x,list):
        return sum(x)
    else:
        return "Error"
    

print(multi_func(2.5))


#Error since none of the conditions are met