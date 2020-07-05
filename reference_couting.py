import sys
import ctypes

a = [1,2,3]

#get the id of the reference
id(a)

# get the total reference count, subtract always one because the function itself is a reference
sys.gettotalrefcount(a)

#return the adress inputing the id(a) by ref_count(id(a)) 
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

