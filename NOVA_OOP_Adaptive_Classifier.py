import numpy as np

class ParameterSet:
    def __init__(self, E, A, F, R, V):
        self.E, self.A, self.F, self.R, self.V = E, A, F, R, V

    def compute_learning_gain(self, alpha):
        L = (alpha[0]*self.E +
             alpha[1]*self.A*100 +
             alpha[2]*self.F +
             alpha[3]*self.R +
             alpha[4]*self.V)
        return L


class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
        self.records = {}

    def add_subject(self, subject):
        self.subjects[subject.name] = subject

    def study(self, optimizer):
        for subject in self.subjects.values():
            params = subject.generate_parameters()
            L = optimizer.optimize(params)
            stage = optimizer.classify_stage(L)
            self.records[subject.name] = {"L": L, "stage": stage}


class Subject:
    def __init__(self, name, difficulty_weight):
        self.name = name
        self.difficulty_weight = difficulty_weight

    def generate_parameters(self):
        E = np.random.uniform(10, 40)
        A = np.random.uniform(0.4, 0.9) * self.difficulty_weight
        F = np.random.randint(5, 20)
        R = np.random.uniform(2, 5)
        V = np.random.randint(1, 10)
        return ParameterSet(E, A, F, R, V)


class Optimizer:
    def __init__(self, alpha=[0.25, 0.35, 0.15, 0.15, 0.10]):
        self.alpha = alpha

    def optimize(self, paramset):
        return paramset.compute_learning_gain(self.alpha)

    def classify_stage(self, L):
        return "Advance" if L >= 60 else "Reinforce"


if __name__ == "__main__":
    subjects = [Subject("Math", 1.0), Subject("Science", 0.9), Subject("Social", 1.1)]
    optimizer = Optimizer()
    students = [Student(f"Student_{i+1}") for i in range(20)]

    for s in students:
        for subj in subjects:
            s.add_subject(subj)
        s.study(optimizer)

    for s in students:
        print(f"\n{s.name}")
        for subj, rec in s.records.items():
            print(f"  {subj}: L={rec['L']:.2f}, Stage={rec['stage']}")
