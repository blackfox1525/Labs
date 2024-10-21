numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

kolichestvo = len(numbers) # Количество чисел в списке

left_summ = sum(numbers[0:4])
right_summ = sum(numbers[5:])
summ = left_summ + right_summ # Сумма чисел вв списке

schet = summ / kolichestvo # Среднее арифметическое

numbers[4] = schet # Замена значения в списке

print("Измененный список:", numbers)
