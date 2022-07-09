from empIT import EmpIT

mike = EmpIT("001","Mike","60000")
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()


from empmkt import EmpMKT
anna = EmpMkt("002","Anna",35000)
anna.emp_detail()
anna._emp_salary()
anna.emp_detail()
anna.mkt_salary()

jess = EmpMkt()
jess.add_location('Chiang Mai')
jess.add_commission(35)
jess.emp_detail()
jess.mkt_salary()


