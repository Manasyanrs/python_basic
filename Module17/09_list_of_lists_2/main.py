
# TODO list set dict tuple в именовании не используем

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

results = [third_level for first_level in nice_list
           for second_level in first_level
           for third_level in second_level]
print(results)