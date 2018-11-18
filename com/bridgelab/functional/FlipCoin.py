from com.bridgelab.utility.Utility import Utility
utility_obj=Utility()
print("Enter Number of Times You want to flip coin")
times=utility_obj.get_int()
head,tail=utility_obj.get_probability(times)
print("Head Percentage "+str(head))
print("Tail Percentage "+str(tail))