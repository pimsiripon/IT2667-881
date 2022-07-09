from employee import Employee

class EmpIT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = None
        self.depertment = 'IT'

    def add_skill(self,skill:str):
       self.skill = skill

    def add_experience(self,exp:str):
       self.experience = exp

    def emp_detail(self):
        super().emp_detail()


        print(f'skill: {self.skill}')
        print(f'experience: {self.experience}')

    def it_salary(self):
       self._emp_salary()
