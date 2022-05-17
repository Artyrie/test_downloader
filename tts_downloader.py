import tkinter
from tkinter import *
from tkinter import filedialog
from tts_image_autosave import *


# 기본 윈도우 설정
window = tkinter.Tk()
window.title("TTS Downloader")
window.geometry("480x120+100+100")
window.resizable(False, False)


# 변수
json_path_var = tkinter.StringVar()
json_path = Label(window, textvariable=json_path_var, bg='white', width=59)
save_path_var = tkinter.StringVar()
save_path = Label(window, textvariable=save_path_var, bg='white', width=59)


# Json 파일 찾기
def open_json():
    window.filename = filedialog.askopenfilename(initialdir='./json', title='파일선택',
                                                 filetypes=(('Json Files', '*.json'),))
    json_path_var.set(window.filename)


def save_folder():
    save_path_var.set(filedialog.askdirectory(parent=window, initialdir='/', title='폴더선택'))


def progress():
    download_image(json_path_var.get(), save_path_var.get())
    window.destroy()


# 위젯
json_btn = Button(window, text = "파일열기", command=open_json)
save_folder_btn = Button(window, text = "폴더선택", command=save_folder)
progress_btn = Button(window, text = "실행", command=progress, width=30)
text_notice_json = Label(window, text='추출할 Json 파일을 선택해 주세요.')
text_notice_save = Label(window, text='저장할 폴더를 선택해 주세요.')

# 컴포넌트 정리
text_notice_json.grid(row=0, columnspan=2)
json_path.grid(row=1, column=0, sticky='ew')
json_btn.grid(row=1, column=1, sticky='ew')
text_notice_save.grid(row=2, columnspan=2)
save_path.grid(row=3, column=0, sticky='ew')
save_folder_btn.grid(row=3, column=1, sticky='ew')
progress_btn.grid(row=4, columnspan=2)
window.mainloop()