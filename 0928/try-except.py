def getMean(numernicValue):
    return sum(numernicValue)/len(numernicValue)

my_list2 = []

try:
    result = getMean(my_list2)
    print("{}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("(Error) : {}".format(float('nan')))
    print("(Error) : {}".format(detail))
else:
    print("(The mean is) : {}".format(result))
finally:
    print("(Finally) : The finally block is executed every time")
    
