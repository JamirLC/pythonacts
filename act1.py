def problem_1():
  students = {'John', 'Maria', 'David', 'Samantha'} 
  
  while True:
    try:
      index = int(input('Enter index: '))
      
      current_index = 0
      student = None
      
      for stud in students:
        if current_index == index:
          student = stud
          break
        current_index += 1
      
      if student is not None:
        print(f'Student at index {index} is {student}.')
      else:
        raise IndexError('Enter only between -4 and 3')
      break
    except ValueError:
      print('Enter only integer numbers\n')
    except IndexError as ie:
      print(f'Error: {ie}\n')

def problem_2():
  numbers = (1, 4, 7, 10, 13, 16)
  sum_of_even = 0
  
  for x in numbers:
    if x % 2 == 0:
      sum_of_even += x
  
  average = sum_of_even / len(numbers)
  print(f'The average of even numbers in the tuple is {average:.2f}')

def problem_3():
  people = {'users':
            {
             'John': 19,
             'Emily': 21,
             'Sarah': 25,
             'Tom': 18
            }
           }
  print('User/s that is older than 19\n')
  for _, inner in people.items():
    for user, age in inner.items():
      if age > 19:
        print(f'Name: {user}')


def problem_4():
  numbers = (1, 3, 2, 4, 3, 1, 2, 5, 10)
    
  for i in range(len(numbers)):
    count = 0
    is_counted = False
    
    for k in range(i):
      if numbers[k] == numbers[i]:
        is_counted = True
        break
        
    if not is_counted:
      for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
          count += 1
      if count > 1:
           print(f'{numbers[i]} appeared in the tuple {count} times')

def problem_5():
  student_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]
  lowest_score = student_scores[0]
  
  for student, score in student_scores:
    if score < lowest_score[1]:
      lowest_score = (student, score)
  print(f'Student with a lowest score is {lowest_score[0]} with a score of {lowest_score[1]}')
      
 
def divider():
  print("/" * 30)
  print()
  
def main():
  print("Select a problem to solve (1-5):")
  print("1: Problem 1")
  print("2: Problem 2")
  print("3: Problem 3")
  print("4: Problem 4")
  print("5: Problem 5")
  print()

  while True:
    try:
      choice = int(input("Enter your choice: "))
      if choice < 1 or choice > 5:
        raise ValueError("Choice must be between 1 and 5.")
        divider()
        break
      else:
        divider()
        break
    except ValueError as ve:
      print(f"Invalid input: {ve}. Please enter an integer between 1 and 5.")
      divider()
        
        
  if choice == 1:
    divider()
    problem_1()
  elif choice == 2:
    divider()
    problem_2()
  elif choice == 3:
    divider()
    problem_3()
  elif choice == 4:
    divider()
    problem_4()
  elif choice == 5:
    divider()
    problem_5()
    
if __name__ == "__main__":
    main()        