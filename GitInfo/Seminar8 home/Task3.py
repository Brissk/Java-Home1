import json
def take_from_base(path = 'students.json'):
    with open(path,'r') as file:
        data = json.load(file)
        file.close()
    return data



student_dict = take_from_base()
# print(student_dict[int(max(student_dict.keys()))])
print(student_dict.keys()+1)




