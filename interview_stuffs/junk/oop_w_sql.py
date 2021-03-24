

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def Repeat(self):
        return(print("The question is: ",{self.question}))



class FunFact:
    def __init__(self, fact):
        self.fact = fact
