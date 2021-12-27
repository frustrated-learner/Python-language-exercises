# Write a function with the signature shown below:

# def is_int_array(arr):
#     return True
# returns true / True if every element in an array is an integer or a float with no decimals.
# returns true / True if array is empty.
# returns false / False for every other input.


def is_int_array(arr):
    try:
        if arr == []:
            return True
        elif len(arr) <= 0:
            return False
        
        for numbers in arr:
            if numbers != int(numbers):
                return False
            
        return True
    
    except:
        return False

print(is_int_array([1.0, 2.0, 3.0]))