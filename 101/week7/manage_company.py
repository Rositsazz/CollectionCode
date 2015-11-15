import sqlite3


connection = sqlite3.connect("company.db")
cursor = connection.cursor()

print("""Choose one of the commands:\n -list_employees\n -monthly_spending
 -yearly_spending \n -add_employee\n -delete_employee
 -update_employee \n -check_employee""")
command = input("command>")

if command == "list_employees":
    list_employees = """SELECT name, possition FROM company """
    cursor.execute(list_employees)

    for row in cursor:
        print('{0} - {1} '.format(row[0], row[1]))

elif command == "check_employee":
    emp_id = input("employee_id> ")
    emp_id = int(emp_id)
    check = """SELECT name FROM company WHERE id = {}""".format(emp_id)
    cursor.execute(check)
    print(cursor.fetchone()[0])

elif command == "monthly_spending":
    monthly_spending = """SELECT SUM(monthly_salary) FROM company"""
    cursor.execute(monthly_spending)
    salary = cursor.fetchone()[0]
    print("The company is spending ${} every month! ".format(salary))

elif command == "yearly_spending":
    yearly_spending = """SELECT SUM(yearly_bonus) FROM company"""
    cursor.execute(yearly_spending)
    print("The company is spending {} \
           every year!".format(cursor.fetchone()[0] + 12*salary))

elif command == "add_employee":
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    possition = input("possition>")
    insertion = (name, int(monthly_salary), int(yearly_bonus), possition)
    cursor.execute("""INSERT INTO company(name, monthly_salary, yearly_bonus, possition)
                  VALUES(?, ?, ?, ?)""", insertion)

elif command == "delete_employee":
    employee_id = input("input employee_id> ")
    name = """SELECT name FROM company WHERE id = {}""".format(employee_id)
    cursor.execute(name)
    deleted_employee = cursor.fetchone()[0]
    cursor.execute("""DELETE FROM company WHERE id = """ + employee_id)
    print("{} was deleted".format(deleted_employee))

elif command == "update_employee":
    employee_id = input("input employee_id> ")
    employee_id = int(employee_id)
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    possition = input("possition>")
    i = (name, int(monthly_salary), int(yearly_bonus), possition, employee_id)
    update_employee = """ UPDATE company
                          SET name = ?, monthly_salary = ?,
                            yearly_bonus = ?, possition = ?
                          WHERE id = ? """
    cursor.execute(update_employee, i)

else:
    print("Wrong command")

connection.commit()
