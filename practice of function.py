cities = ["delhi","up","haryana","pune","bihar","mumbai"]
heroes = ["thor","ironman","captain america","shaktiman"]
def print_len(list):
    print(len(list))
         
print_len(cities)
print_len(heroes) # practice question find len of lists using function

def print_list(list):
    for item in list:
        print(item,end="")
    
    
    print_list(heroes)