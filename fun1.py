#def add_numbers():
#    c=0
#    for number in range(1,100+1):
#        print(number)
#        c=c+number
#    return(c)
#answer=add_numbers()
#print(answer)



start=int()
end=int()
def add_numbers(start,end):
    c=0
    for number in range(start,end+1):
        c=c+number
    return(c)

add_numbers(333,777)
answer=add_numbers(333,777)
print(answer)
