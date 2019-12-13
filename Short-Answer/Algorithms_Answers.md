#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). With the given input, the function will keep running until the while loop is deemed false. Seems like a linear function.


b) O(n^2). With a while loop nested in a for loop, I believe this function will take double the time to complete operations from 0 to n.


c) O(n). This is a recursive function, which will call itself as many times (n) as needed until reaching the base case. This seems to be linear.

## Exercise II

notes: 
- egg broken if: thrown off a floor >= f 
- egg not broken if: dropped off a floor < f

initialize broken and alive egg variables
loop through n story building
loop through each story n up to floor f
if story n >= floor f, egg is broken (increment broken by 1)
else if story n < floor f, egg is not broken (increment alive by 1)
return values

runtime complexity would be O(n^2) since we are nesting a loop in another loop. 