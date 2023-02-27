'''
DEVELOPER: Soha Shahidi
PROFESSOR: Mark Aloka
'''

""" This program can be used to determine final course grade or to find the expected number of assignments for a given week of the semester.
"""

''' GRADING SCALE FOR REFERENCE
A: Satisfactory on = 4 Unit Deliverables Satisfactory on > 14 labs ≥ 45 engagements pts
B: Satisfactory on = 3 Unit Deliverables Satisfactory on > 12 labs ≥ 40 engagements pts
C/P: Satisfactory on = 2 Unit Deliverables Satisfactory on > 10 labs ≥ 35 engagements pts
D/NP: Satisfactory on = 1 Unit Deliverables Satisfactory on > 8 labs ≥ 30 engagements pts
'''

##### FUNCTION DEFINITIONS #####

def determine_grade(uds, labs, eps):
  
  if uds == 4 and labs > 14 and eps >= 45:
    grade = 'A'
  elif uds >= 3 and labs > 12 and eps >= 40:
    grade = 'B'
  elif uds >= 2 and labs > 10 and eps >= 35:
    grade = 'C'
  elif uds >= 1 and labs > 8 and eps >= 30:
    grade = 'D'
  elif uds >= 0 and labs <= 8 and eps <30:
    grade = 'F'
  else:
    grade = 'Error'
  return grade

def a_or_an(grade_earned):
  if grade_earned == 'A' or grade_earned == 'F' or grade_earned == 'Error':
    word = 'an'
  else:
    word = 'a'
  return word

def progress_check_a(weeks_completed):

# Calculate expected unit deliverables
  expected_uds = weeks_completed / 5
  if expected_uds < 1:
    uds_needed = 0
  elif expected_uds >=1 and expected_uds < 1.8:
    uds_needed = 1
  elif expected_uds >=1.8 and expected_uds < 2.6:
    uds_needed = 2
  elif expected_uds >= 2.6 and expected_uds < 3.4:
    uds_needed = 3
  else:
    uds_needed = 4
    
# Calculate expected labs
  expected_labs = int((weeks_completed / 16) * 15)
# Calculate expected engagement points  
  expected_eps = int((weeks_completed / 16) * 45)
# Returns expected values as integers
  return uds_needed, expected_labs, expected_eps
  
##### MAIN PROGRAM #####

def main():
  input_weeks = int(input('How many weeks have you been taking CS138? '))
  input_uds = int(input('Enter the number of unit deliverables completed: '))
  input_labs = int(input('Enter the number of labs completed: '))
  input_eps = int(input('Enter the number of engagement points you have: '))
  print('Your current grade is', a_or_an(determine_grade(input_uds, input_labs, input_eps)), determine_grade(input_uds, input_labs, input_eps) + '.')
  num_ud, num_lab, num_ep = progress_check_a(input_weeks)
  print(f'To be on track for an A, after completing {input_weeks} weeks of the semester you should have {num_ud} unit deliverables completed, {num_lab} labs completed, and earned {num_ep} engagement points.')

main()
