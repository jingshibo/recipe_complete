# %%
my_number = 2.6
round_down = int(my_number)
round_nearest = round(my_number)
new_float = float(round_nearest)
my_number = -3.6
c = 1j

##
string1 = "I'm the best "
string2 = "at coding in Python"
joined_string = string1 + string2
print(joined_string)

##
string1 = "Python"
string2 = "is my favourite language"

excerpt1 = string1[-1]
print(excerpt1)

excerpt2 = string2[1:10:3]
print(excerpt2)

excerpt3 = string2[1::2]
print(excerpt3)

##
choice = "I like it very much"
print(choice[0])
first_three = choice[0:3]
last_three = choice[-3:]
new_string = first_three + last_three
second_string = choice[1::2]
code_string = "q!2refrdgho2!c73 h#eg4hfet@f gvdd4e kkfgc1dab,r3fcgh fguthofeYe"
message = code_string[:-2:3]

##
shopping_list = ["apples", "bananas", "bread", "mushrooms"]
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[1:4:2])
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[2][2])

##
cuddly_animals = ["rabbit", "hamster"]
cuddly_animals.append("rat")
cuddly_animals.insert(1, "chinchilla")
joined_list = cuddly_animals + shopping_list
print(joined_list)

# %%
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
dict1 = {1: "integer_keyed_item", "a": "string_keyed_item", False: "boolean_keyed_item", 3.14: "Pi"}
print(dict1.keys())
print(list(dict1.keys()))
dict1 = {1: "integer_keyed_item", "a": "string_keyed_item", False: "boolean_keyed_item", 3.14: "Pi"}
print(dict1.items())

##
print("Case A")
print(not True)

print("Case B")
print(3 > 4 or 1 in [1, 2])

print("Case C")
print(10 % 2 == 0 and 5 != 6)

# %%
if 1 < 3 and 2 > 4:
    print("wrong")
elif "a" in "and":
    print("it is " + "right")

##
my_list = range(4)
for item in my_list:
    print(item)
words = ["hello", "world", "spam", "eggs"]
for i in words:
    print(i + "!")

# %%
numbers = range(10)
print(numbers)


##
def greater_than(x: object, y: object) -> object:
    if x > y:
        return (True)
    else:
        return (False)
    print("This code is unreachable and will never be printed")


print(greater_than(3, 7))


##
def largest(x, y=False):
    max_value = max(x);
    if y == True:
        min_value = min(x)
        max_abs = max(max_value, -min_value)
        return max_abs
    else:
        return max(x)


print(largest([10, 15, -30], True))

# %%
import math
from math import asin as arcsin


def triangle(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c


print(triangle(2, 3))

##
tuple1 = (1, "a", False)
print(tuple1[0])
x = 1
y = 2
(x, y) = (y, x)
print(x)
print(y)

# %%
import test as un

(minimum, maximum) = un.smallest_biggest([1, 4, 99, -5])

print(minimum)
print(maximum)

##
time = list(range(0, 25, 3))
population = [1, 2.2, 3.9, 8.5, 16.4, 30, 65, 135, 240]

i = 0;
for t in time:
    a = math.exp(0.231 * t)
    i = i + 1

##
import matplotlib.pyplot as plt
import math

time = list(range(0, 25, 3))
population = [1, 2.2, 3.9, 8.5, 16.4, 30, 65, 135, 240]

timerr = 0.5
poperr = []
for p in population:
    poperr.append(p * 0.1)

# Create the lists to hold the y-coordinates of the fit and the upper and lower y-coordinates of the confidence interval
fitvalue = []
shaded_lower = []
shaded_upper = []

# Calcualte the y-coordinates of the fit and the upper and lower y-coordinates of the confidence interval
for t in time:
    fit = math.exp(0.231 * t)
    fitvalue.append(fit)
    print(fitvalue)
    shaded_lower.append(fit * 0.92)
    shaded_upper.append(fit * 1.08)
plt.figure()
# Set the ylabel, xlabel and title
plt.ylabel("Bacteria Population (Arbitrary Units)")
plt.xlabel("Time (h)")
plt.title("Bacteria Population as a Function of Time")

plt.errorbar(time, population, xerr=timerr, yerr=poperr, fmt="none", label="observation")
plt.plot(time, population, label="Fit", color="red")
plt.fill_between(time, shaded_lower, shaded_upper, alpha=0.3, color="red", label="Confidence Interval")

plt.legend()
plt.savefig("figure.svg")
plt.show()


##
# import scipy.io
#
# mat = scipy.io.loadmat('Experiment_Data_20211028.mat')
# data = mat["orig_processed_EMG"]
# data1 = data[0, 0]
# a = data1[1, :]


##
def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("You can't divide by zero! You'll doom us all!")
    finally:
        print("Division complete")


divide(10, 0)
divide(10, 2)
print("Let's try the next call")


##
def divide2(a, b):
    if (b != 0):
        print(a / b)
    else:
        print("You can't divide by zero! You'll doom us all!")


divide2(10, 0)
divide2(10, 2)
print("Division complete")

# %%
# @title

# Import the math module
import math


# Define the function
def quadratic(a, b, c):
    # Calcualte the discriminant
    discriminant = b ** 2 - 4 * a * c

    # If the discriminant is zero, return one root

    if (a == 0 or b == 0):
        raise ValueError("undefined")

    if discriminant == 0:
        # We can assume that a is not zero here as we were told we could assume at least one of a and b is non-zero and, if a were zero, b would have to be zero to return a discriminant of zero
        return ([-b / (2 * a)])

    try:
        # Try to return two roots
        return ([(-b + math.sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a)])
    # Catch the case where a is zero
    except ZeroDivisionError:
        # If a is zero, the result should be -c/b
        return ([-c / b])
    except ValueError:
        return ("not negative")
    # If a ValueError exception is raised from taking the square root of a negative discriminant, it will be passed back to wherever the function was called from.


# Test with some values
print(quadratic(2, -5, -12))  # Should have two roots
print(quadratic(-2, -4, -2))  # Should have one root
print(quadratic(0, 1, 2))  # Should have one root (and tests the except is catching when a=0)
# print(quadratic(1,1,1)) # Should raise a ValueError as the discriminant will be zero
print(quadratic(0, 0, 1))  # Should raise our ValueError as a and b are both zero

##
import math


def find_hypotenuse(length1, length2):
    # This function finds the hypotenuse of a right-angled triangel given the length of its other two sides
    if length1 < 0 or length2 < 0:
        raise ValueError("Both lengths must be non-negative")
    else:
        return (math.sqrt(length1 ** 2 + length2 ** 2))
    try:
        return (math.sqrt(length1 ** 2 + length2 ** 2))
    except ValueError:
        print("Both lengths must be non-negative")


print(find_hypotenuse(3, 4))
print(find_hypotenuse(-3, 4))


# %%
# Define the function
def quadratic(a, b, c):
    # Check if both a and b are zero
    if (a == 0 and b == 0):
        raise ValueError("Both a and b are zero, so x has no defined value")

    # Calcualte the discriminant
    discriminant = b ** 2 - 4 * a * c

    # If the discriminant is zero, return one root
    if discriminant == 0:
        # We can assume that a is not zero here as we were told we could assume at least one of a and b is non-zero and, if a were zero, b would have to be zero to return a discriminant of zero
        return ([-b / (2 * a)])

    try:
        # Try to return two roots
        return ([(-b + math.sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a)])
    # Catch the case where a is zero
    except ZeroDivisionError:
        # If a is zero, the result should be -c/b
        return (-c / b)
    # If a ValueError exception is raised from taking the square root of a negative discriminant, it will be passed back to wherever the function was called from.


# Test with a case where a and b are both zero
print(quadratic(2, -5, -12))  # Should have two roots
print(quadratic(-2, -4, -2))  # Should have one root
print(quadratic(0, 1, 2))  # Should have one root (and tests the except is catching when a=0)
print(quadratic(1, 1, 1))  # Should raise a ValueError as the discriminant will be zero
print(quadratic(0, 0, 1))  # Should raise our ValueError as a and b are both zero

# %%
import matplotlib.pyplot as plt

# Create the set of values
# Each inner list refers to the values are various values of y at a constant x
values = [[0, 0, 0, 0, 0], [0, 1, 2, 1, 0], [0, 2, 5, 2, 0], [0, 1, 5, 1, 0], [0, 1, 5, 1, 0]]
plt.imshow(values, extent=extent)
plt.show()

# %%
# Create the figure and axes
fig = plt.figure()
ax = plt.axes()

# Define the axes
# The values are the lower extent of x, the upper extent of x, the lower extent of y and the upper extent of y
extent = [-2, 2, -2, 2]

# Create an imshow
# Pass the values to give the values at different points
# Provide the extent so the values lie on the correct points
# Also save the reference to the imshow into the variable "im"
im = ax.imshow(values, extent=extent)
# Add a colorbar to the figure
# Pass "im" as an argument so the values and colours  from the imshow can be used
plt.colorbar(im)
plt.show()

# %%
import math
import matplotlib.pyplot as plt

# Create the coordinates and values for the gravity well
x_well = []
y_well = []
for i in range(21):
    x_well.append(-10 + i)
    y_well.append(-10 + i)

values_well = []

for ix in range(21):
    values_well.append([])
    for iy in range(21):
        if x_well[ix] == 0 and y_well[iy] == 0:
            value = - 1
        else:
            value = - 1 / (x_well[ix] ** 2 + y_well[iy] ** 2)
        values_well[ix].append(value)

# Create the coordinates for the planet's orbit
x_orbit = []
y_orbit = []
z_orbit = []

for i in range(101):
    x_orbit.append(5 * math.cos(i * math.pi / 50))
    y_orbit.append(5 * math.sin(i * math.pi / 50))
    z_orbit.append(0.5)

# Write your code to plot the elements of the figure below
# Create the figure and axes
fig = plt.figure()
ax = plt.axes()
# plt.contour3D(x_well,y_well,values_well)
plt.plot3D(x_orbit, y_orbit, z_orbit)
plt.scatter3D(0, 0, 0.5)
plt.scatter3D(5, 0, 0.5)

##

# First create some toy data:
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)


# Create just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# Create two subplots and unpack the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# Create four polar axes and access them through the returned array
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')

# Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')

# Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

# Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)

# Create figure number 10 with a single subplot
# and clears it if it already exists.
fig, ax = plt.subplots(num=10, clear=True)

plt.show()
