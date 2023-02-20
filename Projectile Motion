'''
DEVELOPER: Soha Shahidi
PROFESSOR: Mark Aloka

This program implements the projectile formula to a function.

'''
#### CONSTANTS SECTION ####
# Step 1: Defining a constant global variable

acceleration = -9.8 # acceleration constant

#### FUNCTIONS SECTION ####
# Step 2: Defining a function to find the time of the maximum height
# name the function calc_time_max_height

def calc_time_max_height(velocity):
  time = -velocity/acceleration
  return time
  

# Step 3: Defining a function to find the height of the maximum height
# name the function calc_max_height

def calc_max_height(velocity, initial_height, time):
  max_height = ((1/2) * acceleration * (time**2)) + (velocity * time) + initial_height 
  return max_height

# Step 6: Combining two functions into one and returning two outputs
# name the function find_peak

def find_peak(velocity, initial_height):
  time_fp = calc_time_max_height(velocity)
  max_height_fp = calc_max_height(velocity, initial_height,time_fp)
  return time_fp, max_height_fp
  

#### MAIN PROGRAM ####
# Step 4: Using the calc_time_max_height to find the time of the maximum height
# passed values to a variable. Using the calc_max_height to find the maximum height and
# passed values to a variable.

velocity = 39.2
initial_height = 3
time = calc_time_max_height(velocity)
maximum_height = calc_max_height(velocity, initial_height, time)

# Step 5: Printing the results using calc_time_max_height and calc_max_height output.

print(f"The maximum height of the ball with velocity 39.2 m/s and initial velocity 3 m is {time:.2f} sec, with maxim height {maximum_height:.2f} meters using the two functions.")

# Step 7: Using the find_peak to find the maximum height and time
# passed values to two different variables

timemax_fp, maxheight_fp = find_peak(velocity, initial_height)


# Step 8: Printing the results using the find_peak output

print(f"The maximum height of the ball with velocity 39.2 m/s and initial velocity 3 m is {timemax_fp:.2f} sec, with maxim height {maxheight_fp:.2f} meters using the two functions")

