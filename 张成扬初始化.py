import tkinter
import pickle

# 创建窗口
window = tkinter.Tk()
window.title("计算器")
# 记录算式
expstr = ""
history_label_obj_list = []
try:
    with open('history.pkl', 'rb') as f:
        data = f.read()
      
        if data:
            history_label_obj_list = pickle.loads(data)
except FileNotFoundError:
    pass