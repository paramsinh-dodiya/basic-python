def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)


city=["kodinar","dolasa","una","diu","kaj"]

print_list(city)