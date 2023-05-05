class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def work(self):
        pass

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def __init__(self, name, salary, bonus=0.1):
        super().__init__(name, salary)
        self.__bonus = bonus
        self.__work_hours = 0


    def work(self, work_done):
        bonus_work = work_done * self.__bonus
        work_to_pay = work_done + bonus_work
        self.__work_hours += work_to_pay
        print(f"work's hours with bonus for {self.get_name()}: {work_to_pay}")

    def get_salary(self):
        final_salary = super().get_salary() + (self.__work_hours * 10)
        print(f"Final salary for {self.get_name()}: {final_salary}")


class Worker(Employee):
    def __init__(self, name, salary, penalty=0.1):
        super().__init__(name, salary)
        self.__penalty = penalty
        self.__work_hours = 0

    def work(self, work_done):
        penalty_work = work_done * self.__penalty
        work_to_pay = work_done - penalty_work
        self.__work_hours += work_to_pay
        print(f"work's hours with penalty for {self.get_name()}: {work_to_pay}")

    def get_salary(self):
        final_salary = super().get_salary() + (self.__work_hours * 5)
        print(f"Final salary for {self.get_name()}: {final_salary}")


manager = Manager("John", 1000)
worker = Worker("Jane", 500)

manager.work(8)
worker.work(8)

manager.get_salary()
worker.get_salary()
