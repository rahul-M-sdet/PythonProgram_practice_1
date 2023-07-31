emp ={"QA":"Rahul","Dev":["Naveen","Mukesh",'Deepak'],"DevOps":"vijay"}

print(len(emp))

print(emp.keys())

print(emp.values())

emp1 = (emp.copy())
print(emp1)

print(emp.get("Dev"))

print(emp.items())