class Quiz:
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0
    def setup_quizzes(self):
        self.quizzes.append(Quiz("호주의 수도는?", "캔버라"))
        self.quizzes.append(Quiz("터키의 수도는?", "앙카라"))
        self.quizzes.append(Quiz("브라질의 수도는?", "브라질리아"))
        self.quizzes.append(Quiz("캐나다의 수도는?", "오타와"))
        self.quizzes.append(Quiz("뉴질랜드의 수도는?", "웰링턴"))
    def play(self):
        for quiz in self.quizzes:
            print(quiz.question)
            user_answer = input("정답: ")
            if user_answer.strip() == quiz.answer:
                print("정답입니다! 🎉")
                self.score += 1
            else:
                print("틀렸습니다. 정답은", quiz.answer)
        print(f"\n{len(self.quizzes)}문제 중 {self.score}개 맞혔어요!")
game = QuizGame()
game.setup_quizzes()
game.play()                