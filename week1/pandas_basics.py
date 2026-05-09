import pandas as pd

employees = pd.DataFrame({
    "name": [
        "Victor",
        "Anna",
        "Oleh",
        "Maria",
        "Ivan",
        "Sofia",
        "Andrii",
        "Olena",
        "Max",
        "Kateryna"
    ],
    "age": [22, 28, 31, 26, 35, 24, 29, 33, 21, 27],
    "salary": [1200, 1800, 2500, 1600, 3200, 1400, 2100, 2800, 1100, 1900]
})

print(employees)
print(employees["salary"])
print(employees[["name", "salary"]])

print(employees["salary"].mean())
print(employees["salary"].max())
print(employees["salary"].min())

print(employees[employees["salary"] > 2000])
print(employees[employees["age"] < 25])

employees["bonus"] = employees["salary"] * 0.1
print(employees)
employees["tax"] = employees["salary"] * 20 / 100
print(employees)
employees["total_salary"] = employees["salary"] + employees["bonus"] - employees["tax"]
print(employees)

employees_sorted = employees.sort_values(by="salary", ascending=False)
print(employees_sorted)

employees_sorted = employees.sort_values(by="age")
print(employees_sorted)
