## math module


## The math module provides mathematical functions and constants for:

# Basic arithmetic helpers
# Trigonometry
# Logarithms & exponentials
# Rounding
# Geometry
# Number theory
# It’s part of the Python Standard Library, so no installation needed.


## import math



#################### math constants   ##########################33


import math
print(math.pi)
print(math.e)  ## eulers function

print(math.tau)   ## angular calculations

print(math.inf)   ## infinity

print(math.nan)       ## invalid num


## power and logarithmic functions

print(math.sqrt(25))
print(math.pow(2,4))
print(math.log(5))    ## log (x)   e =2.718
print(math.log10( 2))
print(math.log2(2))



# Trigonometric Functions (angles in radians)
# Function	Description
# math.sin(x)	Sine
# math.cos(x)	Cosine
# math.tan(x)	Tangent
# math.asin(x)	Inverse sine
# math.acos(x)	Inverse cosine
# math.atan(x)	Inverse tangent
# math.degrees(x)	Radians → Degrees
# math.radians(x)	Degrees → Radians



# 🔄 Rounding & Absolute Value
# Function	Description
# math.ceil(x)	Round up
# math.floor(x)	Round down
# math.trunc(x)	Remove decimals
# math.fabs(x)	Absolute value




# 📏 Geometry & Distance
# Function	Description
# math.hypot(x, y)	√(x² + y²) (distance)
# math.dist(p, q)	Distance between 2 points


# 🧮 Number Theory Functions
# Function	Description
# math.factorial(n)	n!
# math.gcd(a, b)	Greatest common divisor
# math.lcm(a, b)	Least common multiple
# math.isqrt(n)	Integer square root





# 🔍 Floating-Point Helpers
# Function	Description
# math.isfinite(x)	Is finite number
# math.isinf(x)	Is infinity
# math.isnan(x)	Is NaN
# math.fmod(x, y)	Remainder
# math.remainder(x, y)	IEEE 




# 🧠 Special Functions
# Function	Description
# math.perm(n, r)	Permutations (nPr)
# math.comb(n, r)	Combinations (nCr)
# math.prod(iterable)	Product of elements
# math.fsum(iterable)	Accurate float sum

# import math

# r = 7
# area = math.pi * math.pow(r, 2)
# print("Area of circle:", area)

# print("Factorial:", math.factorial(5))
# print("GCD:", math.gcd(24, 36))