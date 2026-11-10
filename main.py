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
    def show_menu(self):
        while True:                          # ① 무한 반복 (종료 전까지)
            print("\n===== 수도 퀴즈 게임 =====")
            print("1. 게임 시작")
            print("2. 최고 점수 보기")
            print("3. 종료")

            choice = input("선택: ").strip()  # ② 입력받기 (공백 제거!)

            if choice == "1":                 # ③ if
                self.play()
            elif choice == "2":               # ④ elif (또 다른 조건)
                print("최고 점수 기능은 곧 추가할게요!")
            elif choice == "3":               # ⑤ elif
                print("게임을 종료합니다. 안녕히 가세요! 👋")
                break                         # ⑥ 반복 탈출!
            else:                             # ⑦ 1,2,3 아닌 경우
                print("1~3 사이로 입력해주세요! 😊")
game = QuizGame()
game.setup_quizzes()
game.show_menu()    