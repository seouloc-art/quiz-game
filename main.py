import json
import os
import shutil


def input_number(prompt, min_value, max_value):
    """min_value~max_value 사이의 숫자만 받을 때까지 반복"""
    while True:
        user_input = input(prompt).strip()  # 앞뒤 공백 제거

        if user_input == "":                 # 빈 입력
            print("입력이 비어 있어요. 다시 입력해주세요! 😊")
            continue
        if not user_input.isdigit():         # 숫자가 아님 (abc 등)
            print("숫자만 입력해주세요! 😊")
            continue

        number = int(user_input)
        if number < min_value or number > max_value:  # 범위 밖
            print(f"{min_value}~{max_value} 사이로 입력해주세요! 😊")
            continue

        return number  # 검증 통과!


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
        self.played = False  # 퀴즈를 한 번이라도 풀었는지

    def setup_quizzes(self):
        self.quizzes = []
        self.quizzes.append(Quiz("호주의 수도는?", ["시드니", "캔버라", "멜버른", "브리즈번"], 2))
        self.quizzes.append(Quiz("터키의 수도는?", ["이스탄불", "앙카라", "이즈미르", "안탈리아"], 2))
        self.quizzes.append(Quiz("브라질의 수도는?", ["리우데자네이루", "상파울루", "브라질리아", "살바도르"], 3))
        self.quizzes.append(Quiz("캐나다의 수도는?", ["토론토", "밴쿠버", "몬트리올", "오타와"], 4))
        self.quizzes.append(Quiz("뉴질랜드의 수도는?", ["오클랜드", "웰링턴", "크라이스트처치", "해밀턴"], 2))

    def play(self):
        if not self.quizzes:  # 퀴즈가 없는 경우
            print("풀 수 있는 퀴즈가 없어요! 먼저 퀴즈를 추가해주세요. 😊")
            return

        self.score = 0
        for quiz in self.quizzes:
            print("\n" + quiz.question)
            for i in range(len(quiz.choices)):
                print(f"{i + 1}. {quiz.choices[i]}")
            user_answer = input_number("정답 번호: ", 1, 4)  # 공통 함수 사용!
            if user_answer == quiz.answer:
                print("정답입니다! 🎉")
                self.score += 1
            else:
                print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")

        self.played = True
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
            # 💾 기존 파일이 있으면 .bak으로 백업!
            if os.path.exists("state.json"):
                try:
                    shutil.copy("state.json", "state.json.bak")
                except OSError:
                    print("⚠️ 백업 파일 생성에 실패했어요. (백업 건너뜀)")
        try:
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError:
            print("⚠️ 저장 중 문제가 발생했어요. (저장 실패)")

    def load_state(self):
        if not os.path.exists("state.json"):  # 파일이 없는 경우
            print("저장 파일이 없어서 기본 퀴즈로 시작해요!")
            self.setup_quizzes()
            return
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            self.best_score = data["best_score"]
            self.quizzes = []
            for q in data["quizzes"]:
                self.quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))
            print("저장된 데이터를 불러왔어요!")
        except (json.JSONDecodeError, KeyError, OSError):  # 파일 손상/오류
            print("⚠️ 저장 파일이 손상되어 기본 퀴즈로 복구합니다!")
            self.setup_quizzes()

    def add_quiz(self):
        print("\n===== 퀴즈 추가 =====")
        question = input("질문을 입력하세요: ").strip()
        while question == "":  # 빈 질문 방지
            print("질문은 비워둘 수 없어요! 😊")
            question = input("질문을 입력하세요: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"{i}번 선택지: ").strip()
            while choice == "":  # 빈 선택지 방지
                print("선택지는 비워둘 수 없어요! 😊")
                choice = input(f"{i}번 선택지: ").strip()
            choices.append(choice)

        answer = input_number("정답 번호(1~4): ", 1, 4)  # 숫자로 받음!
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()  # 추가 후 바로 저장
        print("퀴즈가 추가되었어요! 💾")

    def show_quiz_list(self):
        print("\n===== 퀴즈 목록 =====")
        if not self.quizzes:  # 퀴즈가 없는 경우
            print("등록된 퀴즈가 없어요! 😊")
            return
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"{idx}. {quiz.question}")

    def show_best_score(self):
        if not self.played and self.best_score == 0:  # 아직 안 풀었을 때
            print("아직 퀴즈를 풀지 않았어요! 먼저 게임을 해보세요. 😊")
        else:
            print(f"🏆 최고 점수는 {self.best_score}점이에요!")

    def show_menu(self):
        while True:
            print("\n===== 수도 퀴즈 게임 =====")
            print("1. 게임 시작")
            print("2. 최고 점수 보기")
            print("3. 퀴즈 추가")
            print("4. 퀴즈 목록")
            print("5. 종료")

            choice = input_number("선택: ", 1, 5)  # 공통 함수 사용!

            if choice == 1:
                self.play()
            elif choice == 2:
                self.show_best_score()
            elif choice == 3:
                self.add_quiz()
            elif choice == 4:
                self.show_quiz_list()
            elif choice == 5:
                print("게임을 종료합니다. 안녕히 가세요! 👋")
                self.save_state()
                break


# 프로그램 실행 (Ctrl+C / EOFError 안전 처리)
if __name__ == "__main__":
    game = QuizGame()
    try:
        game.load_state()
        game.show_menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\n프로그램을 안전하게 종료합니다. 저장할게요! 💾👋")
        game.save_state()