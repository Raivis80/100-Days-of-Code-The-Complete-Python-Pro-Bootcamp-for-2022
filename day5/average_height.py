student_heights = input("Input a list of student heights separating with space ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


# for loop solution
total = 0
len_list = len(student_heights)

for student in student_heights:
    total += student

print(round(total / len_list))

# len() and sum() solution
sum_off_heights = sum(student_heights)
len_of_heights = len(student_heights)

print(round(sum_off_heights / len_of_heights))
