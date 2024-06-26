import json

def employees_rewrite(sort_type):

    with open("employees.json") as json_file:
        list_of_tasks = json.load(json_file)
        employees = list_of_tasks.get('employees')
        resalt_sorted = sorted(employees, key=lambda x: x[sort_type], reverse=True)\
        if isinstance(employees[0][sort_type], int) else sorted(employees, key=lambda x: x[sort_type])
        data = {('employees'): resalt_sorted}
        json_object = json.dumps(data, indent=4)
        with open('employees_' + sort_type + '_sorted.json', 'w') as outfile:
            outfile.write(json_object)
        if sort_type not in employees[0]:
            raise ValueError('Bad key for sorting\n'
                             'Вы можете выбрать только следующие виды сортировки: \n'
                             '"firstName", "lastName", "department", "salary"')
