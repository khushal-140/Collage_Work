import pandas as pd
employee={
    "Empid":[101,102,103,104],
    "Name":["Khushal","Rahul","Amit","Nehal"],
    "DepartmentID":[1,2,1,3],
    "Gender":["M","M","F","F"],
    "Salary":[10000,20000,30000,40000]
}

Department={
    "DepartmentID":[1,2,3],
    "DepartmentName":["IT","HR","Sales"]
}

employee=pd.DataFrame(employee)
department=pd.DataFrame(Department)

df=pd.merge(employee,department,on="DepartmentID")
#Inner
pd.merge(employee,
         department,
         on="DepartmentID",
         how="inner")
#Left
pd.merge(employee,
         department,
         on="DepartmentID",
         how="left")
#Rigth
pd.merge(employee,
         department,
         on="DepartmentID",
         how="right")
#Outer 
pd.merge(employee,
         department,
         on="DepartmentID",
         how="outer")


print("---------Join------")
employee.set_index("DepartmentID",inplace=True)
department.set_index("DepartmentID",inplace=True)
join=employee.join(department)
print(join)

print("---------concat()------")
print(pd.concat([employee,department]))

print(pd.concat([employee,department],
          axis=1))

print("----------Map---------")
employee["Gender"] = employee["Gender"].map({
    "M":"Male",
    "F":"Female"
})
print(employee["Gender"])


print("------------apply()----------")
def bonus(x):
    return x*1.10

employee["Salary"]=employee["Salary"].apply(bonus)
print(employee["Salary"])