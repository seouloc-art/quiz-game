# 🌍 나라/수도 퀴즈 게임

파이썬으로 만든 간단한 수도 맞히기 퀴즈 게임입니다!

## ✨ 기능
- 4지선다 나라/수도 퀴즈 출제
- 정답 입력 시 점수 계산 및 최종 결과 출력
- 최고 점수 자동 저장 및 갱신
- 새로운 퀴즈 추가하기
- 등록된 퀴즈 목록 보기
- JSON 파일로 데이터 저장 / 불러오기

## 📋 메뉴 구성
1. 게임 시작
2. 최고 점수 보기
3. 퀴즈 추가
4. 퀴즈 목록
5. 종료

## ▶️ 실행 방법
파이썬이 설치된 환경에서 아래 명령어를 실행하세요.

​```
python main.py
​```

## 💡 퀴즈 주제 선정 이유
평소 세계 여러 나라에 관심이 많았고, 나라와 수도는
누구나 한 번쯤 공부하는 친숙한 주제라 퀴즈로 만들기
적합하다고 생각해 선택했습니다.

## 📂 파일 구조

```
quiz-game/
├── main.py       # 게임 실행 및 핵심 로직 (Quiz, QuizGame 클래스)
├── README.md     # 프로젝트 설명 문서
└── state.json    # 퀴즈 데이터와 최고 점수 저장 파일
```

## 💾 데이터 파일 설명 (state.json)
- 게임에서 추가한 퀴즈와 최고 점수를 저장하는 파일입니다.
- UTF-8 인코딩으로 저장되어 한글이 깨지지 않습니다.
- 프로그램을 종료 후 다시 실행해도 데이터가 유지됩니다.

## 🎬 실행 화면

### 게임 실행
![게임 실행](images/play.png)

### 퀴즈 목록
![퀴즈 목록](images/list.png)

### 최고 점수 보기
![최고 점수](images/bestscore.png)

### 게임 점수 결과
![점수 결과](images/playscore.png)

## 🧰 Git 작업 증빙

### clone / pull
![git clone](images/git_clone.png)
![git clone2](images/git_clone2.png)

### 커밋 로그
![커밋 로그](images/git_log.png)

### 브랜치 / 병합 그래프
![브랜치 그래프](images/git_graph.png)

## 🏗️ 클래스(상자) 설명

### 📦 Quiz 클래스 — "문제 1개"를 담는 상자
- question : 문제 내용
- choices : 보기 4개
- answer : 정답 번호
→ 문제 하나의 정보를 한곳에 모아둡니다.

### 📦 QuizGame 클래스 — "게임 전체"를 움직이는 상자
- play() : 게임 진행
- add_quiz() : 문제 추가
- show_quiz_list() : 문제 목록 보기
- show_best_score() : 최고 점수 보기
- save_state() / load_state() : 저장 / 불러오기
→ 게임의 모든 기능을 담당합니다.

## 🔀 역할 나누기
- input_number() : 숫자 입력이 맞는지 검사 (입력 검증)
- QuizGame : 게임 진행
- Quiz + state.json : 데이터 저장
→ 각자 맡은 일이 달라서 수정하기 편해요!

## 💾 저장 흐름
1. 프로그램 시작 → load_state() 로 불러오기
2. 게임 끝 / 문제 추가 / 종료 → save_state() 로 저장
→ 껐다 켜도 점수와 문제가 그대로 남아요!

## 📌 커밋 규칙
- "기능 추가: 퀴즈 저장 기능" 처럼
  [무엇을 했는지] 를 짧게 적습니다.

## 💡 클래스를 쓴 이유
- 문제 정보를 Quiz 상자에 깔끔하게 모을 수 있어요.
- 문제를 여러 개 만들어도 똑같이 쓸 수 있어요. (재사용!)

## 📊 변경 영향도
- Quiz 를 고치면 → 문제 저장/불러오기에 영향
- QuizGame 을 고치면 → 게임 진행에 영향

## ⚙️ 종료·시그널 처리 (#11)

- Ctrl+C(KeyboardInterrupt)나 EOF 입력 시에도 save_state()로 안전하게 저장돼요.
- SIGTERM 같은 강제 종료까지 저장하려면 signal 모듈을 쓸 수 있어요 (예시):

```python
import signal
def _handle_sigterm(signum, frame):
    game.save_state()
    raise SystemExit(0)
signal.signal(signal.SIGTERM, _handle_sigterm)
```
> Windows는 SIGTERM 지원이 제한적이라, 기본은 Ctrl+C 처리를 사용해요.

## 💾 백업·복원 (#17)

- **자동 백업:** save_state() 저장 전에 기존 state.json을 state.json.bak으로 복사해요.
- **자동 복구:** 파일이 깨지면 load_state()가 기본 퀴즈로 복원해요.
- **수동 복원:** `copy state.json.bak state.json` (Windows) 로 되돌려요.

## 📊 대량 데이터 성능 (#16)

- 퀴즈 1000개 이상이면 JSON 전체를 읽고 쓰므로 I/O·메모리가 선형 증가해요.
- 목록 검색은 리스트라서 O(n)이에요.
- **개선 방안:** 목록 페이징(20개씩), 딕셔너리 인덱스, 대용량 시 SQLite 전환 검토.

