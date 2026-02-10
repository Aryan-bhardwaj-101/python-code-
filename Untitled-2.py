def cala_sum(n):
    if(n==0):
        return
    return calc_sum(n-1) + n
    
calc_sum(5)
    