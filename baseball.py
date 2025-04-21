import tkinter
import tkinter.messagebox as msgbox
import random

# 좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y    
    labelMouse["text"] = str(x) + "," + str(y)

def click_btnCheck():
    global count, btnCheck
    user_input = [entryLec1.get(), entryLec2.get(), entryLec3.get()]

    # 유효성 검사: 입력이 없거나 숫자가 아니거나 중복되었을 경우 무시
    if ("" in user_input) or not all(char.isdigit() for char in user_input):
        return
    if len(set(user_input)) != 3:
        return

    btnCheck["state"] = "disabled"  # 추가 입력 금지
    count += 1
    successGame = False

    #------------------- 과제 영역 시작 -----------------------#
    strike = 0
    ball = 0

    for i in range(3):
        if user_input[i] == answer[i]:
            strike += 1
        elif user_input[i] in answer:
            ball += 1

    if strike == 3:
        successGame = True

    if strike == 0 and ball == 0:
        output_str = "OUT"
    else:
        output_str = f"{strike}S {ball}B"

    btnCheck["text"] = output_str
    #------------------- 과제 영역 끝 -----------------------#

    if count == 10:
        response = msgbox.showerror("종료", "아쉽게도 모든 기회를 사용했습니다.\n정답은 " + ''.join(answer) + "입니다")
        if response:
            root.destroy()
    elif successGame:
        response = msgbox.showinfo("성공", "정답입니다!\n정답은 " + ''.join(answer) + "입니다")
        if response:
            root.destroy()
    else:
        nextGame()

def nextGame():
    global entryLec1, entryLec2, entryLec3, btnCheck
    labelCount = tkinter.Label(root, text=str(count) + "회", font=("맑은 고딕", 10))
    labelCount.place(x=15, y=15 + count * 25)

    entryLec1 = tkinter.Entry(width=2)
    entryLec2 = tkinter.Entry(width=2)
    entryLec3 = tkinter.Entry(width=2)

    entryLec1.place(x=60, y=15 + count * 25)
    entryLec2.place(x=90, y=15 + count * 25)
    entryLec3.place(x=120, y=15 + count * 25)

    btnCheck = tkinter.Button(root, text="확인", font=("Times New Roman", 10), command=click_btnCheck)
    btnCheck.place(x=150, y=15 + count * 25, width=70, height=20)

# 게임 창 설정
root = tkinter.Tk()
root.title("야구 게임")
root.geometry("250x270")
root.bind("<Motion>", mouseMove)

labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕", 10))
labelMouse.place(x=0, y=250)

count = 1

# 정답 생성: 0~9 사이의 서로 다른 3자리 숫자
digits = list("0123456789")
random.shuffle(digits)
answer = digits[:3]
print("정답:", ''.join(answer))  # 콘솔 출력용

nextGame()
root.mainloop()