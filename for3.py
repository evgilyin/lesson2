school_data = [
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [3,5,5,5,4]}, 
{'school_class': '4c', 'scores': [2,2,3,5,5]},
]

#Посчитать и вывести средний балл по всей школе.
len_scores = 0
sum_scores = 0
for class_info in school_data:
  len_scores += len(class_info['scores'])
  sum_scores += sum(class_info['scores'])
print('Средний балл по всей школе:', sum_scores/len_scores)

#Посчитать и вывести средний балл по каждому классу.
for class_info in school_data:
  class_len = len(class_info['scores'])
  class_sum = sum(class_info['scores'])
  average_score = class_sum/class_len
  print(f"Средний балл в {class_info['school_class']} равен {average_score}")
