def print_emp_csv(name,email,empid):
    resp=str(f'{name},{email},{empid}\n')
    return resp

emp1={'name':'John','email':'john@place.com',"empid":1111}
emp2={'name':'Dave','email':'dave@place.com',"empid":2222}
emp3={'name':'Jill','email':'jill@place.com',"empid":3333}

emp_list=[emp1,emp2,emp3]
manage=open("employees.csv","w")

for person in emp_list:
    manage.write(print_emp_csv(person['name'],person['email'],person['empid']))
manage.close()