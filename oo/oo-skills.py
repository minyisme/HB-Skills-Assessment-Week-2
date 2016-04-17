# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?

# Explain each concept.

# 1. What is a class?

    # A class is a type of thing.
    # Default classes in Python include numbers, strings, lists, etc.
    # Objects of the same class will have features/behave in a similar
    # way. 

# 2. What is an instance attribute?

    # Instance attribute is the 'sticker on the body' example Joel gave.
    # It is an attribute that only applies to a specific instance of a 
    # class.
    # It doesn't apply to every instance in a class.

# 3. What is a method?
    
    # A method is a function that applies specifically to a class.
    # Syntax is object.method(arguments) in that object must be in a class
    # that the method can act on.

# 4. What is an instance in object orientation?
    
    # An instance is a specific object that belongs to a class.
    # It is created by a process called "instantiation".

# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.
    
    # Class attribute is an attribute that is defined at the class level.
    # Every instance of that class will have the class attribute.
    # For example, the Ada cohort can have a class attribute of Floor = 2.
    #
    # Instance attribute is an attribute that is defined at the instance 
    # level.
    # Only a specific instance of a class will have an instance attribute.
    # For example, I can have an instance attribute maggie.lightning_talk =
    # "4/21 Morning".


# Parts 2 through 5:
# Create your classes and class methods




# Creates Student class which takes first_name and last_name as args
class Student(object):

    # Sets first_name and last_name as Student instance attributes
    # Prompts for an address
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.address = raw_input("What is student's address?")




# Creates Questions class which takes question and answer as args
class Questions(object):

    # Sets question and answer as Questions instance attributes
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    # Method that asks user to answer a question and returns if answer is correct
    def ask_and_evaluate(self):
        evaluated = raw_input(self.question) == self.answer

        return evaluated




# Creates Exam class which takes exam name as arg
class Exam(object):

    def __init__(self, name):
        self.name = name
        # Creates empty list for questions to be add for instance of Exam
        self.questions = []

    # Method for questions to be added to Exam.questions list
    def add_question(self, question_name, question, correct_answer):
        question_name = Questions(question, correct_answer)
        self.questions.append(question_name)

    # Method that administers the exam and returns a score for correct answers
    def administer_test(self):
        score = 0

        # Loops through asking qeustions in self.questions and evaluates 
        # response
        # Adds 1 to score if response is correct
        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score += 1

        return ((score * 100) / (len(self.questions)))




# Creates class quiz, which is subclass of Exam
# Only difference is when administering, returns pass/fail, not % score
class Quiz(Exam):

    # Uses score from Exam's administer_test method and returns pass/fail
    def administer_test(self):

        # Use super to get results from parent Exam class's administer_test
        score = super(Quiz, self).administer_test()

        # If score over 50%, pass
        # Else, fail
        if score > 50:
            return "Passing"
        else:
            return "Failing"




# Function to administer test and returns student name and score
# A bit redundant I think
def take_test(student, test):

    student_score = test.administer_test()

    return [student, student_score]




# Create sample run of a exam for a student
def example_exam():

    # Sample student is jane_doe
    jane_doe = Student("Jane", "Doe")

    # Sample exam is mdt
    mdt = Exam("Midterm")

    # Adding questions to mdt
    mdt.add_question("add", "What is 4 + 3", 
                    "7")
    mdt.add_question("color", "What color is the sky?",     
                    "blue")
    mdt.add_question("country", "What country borders USA to the north?",
                    "Canada")
    mdt.add_question("state", "What is the Evergreen State?", 
                    "Washington")
    mdt.add_question("time", "What time zone is California in?", 
                    "pacific")

    # Administering mdt to jane_doe and returning a test_score
    test_score = (take_test(jane_doe, mdt))[1]

    # Returns a sentence telling jane_doe's percentage score for mdt.
    return "%s score for %s %s is %i percent!" %(mdt.name, 
        jane_doe.first_name, jane_doe.last_name, test_score)




# Run example exam
print example_exam()




# Create sample run of a quiz for a student
def example_quiz():
    # Sample student is jane_doe
    jane_doe = Student("Jane", "Doe")

    # Sample quiz is qz1
    qz1 = Quiz("Quiz 1")

    # Adding questions to qz1
    qz1.add_question("add", "What is 4 + 3", 
                    "7")
    qz1.add_question("color", "What color is the sky?",     
                    "blue")
    qz1.add_question("country", "What country borders USA to the north?",
                    "Canada")
    qz1.add_question("state", "What is the Evergreen State?", 
                    "Washington")
    qz1.add_question("time", "What time zone is California in?", 
                    "pacific")

    # Administering qz1 to jane_doe and returning a test_score
    test_score = (take_test(jane_doe, qz1))[1]

    # Returns a sentence telling jane_doe's pass/fail status for qz1.
    return "%s result for %s %s is %s!" %(qz1.name, 
        jane_doe.first_name, jane_doe.last_name, test_score)




# Run example quiz
print example_quiz()






