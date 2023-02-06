# Quadratic Equations Solver:


Just a simple and easy to use python script providing you the ability to solve quadratic equations within your own script, including negative roots solutions.



# Usage:

First, you'll have to import the script to your project directory, then just import the script to your python code like this: ```import quadratic```. 
Then finally, use the ```solve``` function to get the result wanted.

# Examples:

```
import quadratic

print(quadratic.solve(5,2,1))
```
Result: S = { -0.2-0.4i ; -0.2+0.4i }

```
import quadratic

print(quadratic.solve(5,2,-1))
```

result: S = { 0.19 ; -0.79 }

# Note:
If the values provided to the function are not numerical data, or the values are 0s, the function will return errors:

```
import quadratic

print(quadratic.solve(0,0,1))
```
result: "Can't divide by 0..."
