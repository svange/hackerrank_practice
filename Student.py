class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
import statistics
class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        mean = statistics.mean(self.scores)
        if mean >= 90:
            return 'O'
        elif mean >= 80:
            return 'E'
        elif mean >= 70:
            return 'A'
        elif mean >= 55:
            return 'P'
        elif mean >= 40:
            return 'D'
        else:
            return 'T'