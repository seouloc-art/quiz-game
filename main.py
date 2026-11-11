import json
import os


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0
        self.best_score = 0

    def setup_quizzes(self):
        self.quizzes.append(Quiz("호주의 수도는?", ["시드니", "캔버라", "멜버른", "브리즈번"], 2))
        self.quizzes.append(Quiz("터키의 수도는?", ["이스탄불", "앙카라", "이즈미르", "안탈리아"], 2))
        self.quizzes.append(Quiz("브라질의 수도는?", ["리우데자네이루", "상파울루", "브라질리아", "살바도르"], 3))
        self.quizzes.append(Quiz("캐나다의 수도는?", ["토론토", "밴쿠버", "몬트리올", "오타와"], 4))
        self.quizzes.append(Quiz("뉴질랜드의 수도는?", ["오클랜드", "웰링턴", "크라이스트처치", "해밀턴"], 2))

    def play(self):
        self.score = 0
        for quiz in self.quizzes:
            print(quiz.question)
            for i in range(len(quiz.choices)):
                print(f"{i + 1}. {quiz.choices[i]}")
            user_answer = input("정답 번호: ")
            if user_answer.strip() == str(quiz.answer):
                print("정답입니다! 🎉")
                self.score += 1
            else:
                print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")
        print(f"\n{len(self.quizzes)}문제 중 {self.score}개 맞혔어요!")
        if self.score > self.best_score:
            self.best_score = self.score
            print("🏆 새로운 최고 점수예요!")
        self.save_state()

    def save_state(self):
        data = {
            "best_score": self.best_score,
            "quizzes": []
        }
        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_state(self):
        if not os.path.exists("state.json"):
            print("저장 파일이 없어서 기본 퀴즈로 시작해요!")
            self.setup_quizzes()
            return
        with open("state.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.best_score = data["best_score"]
        self.quizzes = []
        for q in data["quizzes"]:
            self.quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))
        print("저장된 데이터를 불러왔어요!")

    def show_menu(self):
        while True:
            print("\n===== 수도 퀴즈 게임 =====")
            print("1. 게임 시작")
            print("2. 최고 점수 보기")
            print("3. 종료")

            choice = input("선택: ").strip()

            if choice == "1":
                self.play()
            elif choice == "2":
                print(f"🏆 최고 점수는 {self.best_score}점이에요!")
            elif choice == "3":
                print("게임을 종료합니다. 안녕히 가세요! 👋")
                break
            else:
                print("1~3 사이로 입력해주세요! 😊")


game = QuizGame()
game.load_state()
game.show_menu()