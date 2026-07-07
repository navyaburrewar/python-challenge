## when to use the count sort when to not use the count sort

# Data Type	Can Counting Sort be used?	Reason
# [3, 1, 2, 5]	✅ Yes	               Integers can be used as indices
# [2.5, 1.7, 3.9]	❌ No	           Floats cannot be list indices
# ["apple", "banana"]	❌ No	        Strings cannot be list indices
# [-2, -1, 0, 3]	⚠️ Not with this basic code	|Negative indices need extra handling


## when to use the count-sort
#  1.the elements are integers
#  2.the numbers are ina small range#
#  3.there  are many duplicates values


## when to not use the count-sort
# 1. when the max value is very large
## 2. when the data contains floating-point numbers
## when the data contains strings
## when the range is much larger than the numbers of elements



# Array	        Use Counting Sort?	Reason
# [2,4,3,1,5]	✅ Yes	             Small range
# [3,2,2,1,4,3]	✅ Yes	             Many duplicates
# [1,3,6,8,100]	❌ Not recommended 	 Large range compared to n
# [1,1000000]	❌ No	             Huge count array needed
# [2.5,3.7,1.2]	❌ No	             Floating-point values
# ["cat","dog","bat"]	❌ No	     Strings cannot be used as indices