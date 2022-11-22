student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)
#
# # Keyword Method with iterrows()
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)

# Looping through rows:
for (index, row) in student_data_frame.iterrows():
    # Access row, column via index or column name
    print(row.student)
    print(row.score)
    print(row)