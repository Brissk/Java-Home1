import dict as D
import json

def take_from_base(path = 'students.json'):
    with open(path,'r') as file:
        data = json.load(file)
        file.close()
    return data

def rewrite_base(dictionary, path = 'students.json'):
    with open(path,'w') as file:
        json.dump(dictionary, file, indent=2)
        file.close()

def sit_places():
    sit_place = {}
    column = {}
    place = {}
    for i in range(1,6):
        for j in range(1,4):
            for k in range(1,3):
                place[k] = 0
            column[j] = place
        sit_place[i] = column
    return sit_place

def student_row_creation(
    name = '',
    surname = '',
    sex = 1,
    birthday = '',
    my_class = 1,
    class_type = 1,
    marks_status = 1
): 
    student_dict = take_from_base()
    person = \
    {
        'Name':name,
        'Surname':surname,
        'Sex':D.sex_dict[sex],
        'Birth day':birthday,
        'Class':D.class_dict[my_class],
        'Class Type':D.class_type_dict[class_type],
        'Marcs status':D.marks_status_dict[marks_status]
    }
    student_dict[int(max(student_dict.keys()))+1] = person
    return student_dict

def pop_student(ID_student,dictionary):
    new_dict = dictionary
    new_dict.pop(ID_student)
    return new_dict
    
def find_name(name:str,data:dict):
    return dict(filter(lambda x:x[1]['Name'== name, data.items()]))

    
rewrite_base(student_row_creation('Mikle','Lymarev',1,'31.09.1988',2,2,2))

