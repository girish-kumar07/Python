# Updating two dictionary.
def add_dict(dict1,dict2):
    new_dict = dict1.copy()

    new_dict.update(dict2)

    return new_dict


dict = {'January':'31','Marks':'28','March':'31','April':'30'}
info = {'Riya':'CSE','Marks':'100','Ishpreet':'Eng','Kamaal':'Env.Sc'}

result = add_dict(dict,info)
print(result)