from abc import ABC


class Employee(ABC):
    name: str
    salary: int

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary


class Manager(Employee):
    department: str

    def __init__(self, name: str, salary: int, department: str):
        super().__init__(name, salary)
        self.department = department


class TestEnginner(Employee):
    programming_language: str


class TeamLead(Manager, TestEnginner):
    team_size: int

    def __init__(self, name: str, salary: int, department: str, team_size: int):
        super().__init__(name, salary, department)
        self.team_size = team_size
