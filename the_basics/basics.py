# import datetime
# print("The date and time is:", datetime.datetime.now())
# # print(datetime.datetime.now())

# monday_temperatures = [9.1, 8.8, 7.5]

# # dictionary:
# for grades in student_grades.item():
#                             .keys():
#                             .values():

temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)