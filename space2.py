"""
Part 2
Optimize the previous code to reduce the runtime and memory.

Pseudocode
set an empty array
select every object from array
    apply order by module element%2==0
    add that element to our array
return the newarray with all elementens orderd by module

our new order will be something like this --> [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
"""

arraySimple = [1,2,3,4,35,12,52,128,256,512]
arraySimpleSortEvenLeftAndOddRight = sorted(arraySimple, key = lambda i:[i%2])

print(arraySimpleSortEvenLeftAndOddRight)


"""
Conclusion
The first algorithm is O(n^2) because it has two interaccions (two arrays), and the second algorithm is O(n),
That means the second algorithm is faster than the first one because it only has one interaccion (lambda function).

Comment
I also tried to use this method to measure the runtime but it's no the best way to do it(inaccurate):
import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
"""