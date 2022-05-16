
sample_string= input("Write some numbers separated by comma: ")

list = sample_string.split(",")
tuple = tuple(sample_string.replace(',',''))

print(f"The list is {list}")
print(f"The tuple is {tuple}")