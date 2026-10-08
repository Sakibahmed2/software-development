from function import double
from kargs_multiple import full_name as name

result = double(30)
print('Inside the modules file',result)

f_name = name(firsName="Sakib", lastName="Loskor")
print(f_name)