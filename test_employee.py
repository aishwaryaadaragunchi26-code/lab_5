from employee import employee_details

def test_employee_details():
    result = employee_details("Pavitra",EMP164,"IT",50000)

    expected = (
        "Name:Pavitra\n"
        "Employee ID:EMP164\n"
        "Department:IT\n"
        "Salary:50000"
    )

    assert result == expected