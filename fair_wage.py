"""This program detects whether or not you make a fair hourly wage based on the 30% rule, and then calculates what a fair wage would be if not.

According to the Brooke Amendment (as amended by Congress in 1981), public housing must not cost more than 30% of a renter's income. This has given rise to the '30% rule,' a general rule of thumb that rent should not cost more than 30% of someone's monthly income. This program will calculate whether or not your rental cost meets this rule of thumb based on your hourly wage. This program will also calculate what your wage should be to meet the rule of thumb. Everyone deserves to make a fair wage!

A fair wage is based on more than just housing costs, but this calculator is simplified based on a general rule of thumb, and also doesn't take taxes into account. This program also assumes you are working one job.
"""

##########################################
# FUNCTIONS:
##########################################

def calc_monthly_wage(hourly_wage, hours_per_week): # calculates user's monthly wage assuming that 4 weeks = 1 month, uses branching statements to determine whether user is paid overtime
  if hours_per_week <= 40 and hours_per_week > 0: # checks if user worked between 0-40 hours and calculates monthly wage
    monthly_wage = (hours_per_week * hourly_wage) * 4
  elif hours_per_week > 40: # checks if user is paid overtime, and calculates monthly wage while adding overtime pay
    overtime = (hours_per_week - 40) * 1.5
    monthly_wage = ((hourly_wage * 40) + overtime) * 4
  else: # takes 0 and negative inputs to mean a monthly wage of 0
    monthly_wage = 0
  return monthly_wage

def calc_fair_wage(rent, hours_per_week): # calculates how much a fair hourly wage would be if the user works at their current hours, based on making your rent 30% of your income
  fair_monthly_wage = rent / 0.3
  fair_wage = fair_monthly_wage / (hours_per_week * 4) # assumes each month is 4 weeks
  return fair_wage

# calculates what percentage of your monthly wage your rent is
def percent_burdened(rent, monthly_wage):
  burden = (rent / monthly_wage)*100
  return burden

# this function checks if the user is rent burdened by calculating what your rent should be if you're paying 30% of your income to rent, and then comparing that to what you're actually paying
def check_30_rule(monthly_wage, rent, fair_wage, hours_per_week): 
  rent_check = monthly_wage * 0.3 # calculates what 30% of your monthly wage is to compare with your rent
  if rent_check >= rent: # checks if you are paying less rent than 
    fair_or_not = 'You make a fair wage according to the 30% rule!'
  elif rent_check < 0: # detects if user is inputting negative numbers and asks them to rerun program
    fair_or_not = "Value(s) entered were negative, please rerun program and use positive inputs."
  else: # only other option is that your rent is more than 30% of your income, uses output from calc_fair_wage() to tell the user how much they should make per hour if they work the same number of hours per week
    fair_or_not = f'You do not make a fair wage according to the 30% rule, a fair wage for you would be ${fair_wage:.2f} an hour if you work {hours_per_week:.0f} hour weeks.'
  return fair_or_not

##########################################
# MAIN PROGRAM:
##########################################
  
def main():
  print('This program will calculate whether or not you are rent burdened according to the 30% rule.')
  while True:
    try:
      input_hourly_wage = float(input('\nPlease input your hourly wage: ')) # allows user to input their hourly wage as a float, so will accept fractions of dollars
      input_hours_worked = float(input('Please input the number of hours you work per week: ')) # allows use to input hours worked weekly as a float, so can accept fractions of hours 
      input_rent = float(input('Please input your monthly rent: ')) # allows user to input rent as a float, so can put fractions of dollars
      break
    except ValueError:
      print("Error! Please enter a valid numerical value.")

  # runs monthly wage and fair wage calculator functions, whos outputs are assigned to a variable and used to check if the user is rent-burdened 
  monthly_wages = calc_monthly_wage(input_hourly_wage, input_hours_worked)
  fair_wages = calc_fair_wage(input_rent, input_hours_worked) 

  # runs function to calculate how much the user is rent-burdened
  rent_burden = percent_burdened(input_rent, monthly_wages)

  print(f'\nYour rent burden is {rent_burden:.1f}%.')

  # runs function to check if the user is rent-burdened, then assigns output to a variable to be printed
  rent_burdened = check_30_rule(monthly_wages, input_rent, fair_wages, input_hours_worked)

  print(f'\n{rent_burdened}')
  

main()
  
