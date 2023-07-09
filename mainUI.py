import tkinter as tk
from tkinter import font
from tkinter import ttk
import main as m


def get_info():
    api_key = api_box.get()
    userName = userName_box.get()
    region = drop_down.get()
    info = m.get_player_info(userName, api_key, region)
    for key,value in info.items():
        res_label.insert(tk.END,f"{key}: {value}\n")

    res_label.insert(tk.END,'---------------------------------------\n')
    res_label.config(state='disabled')
    api_box.delete(0,tk.END)

root = tk.Tk()
root.title('League Data Crawling API')
root.geometry('800x800')
root.iconbitmap('icon.ico')
italic_font = font.Font(slant='italic', size=11)
frame = tk.Frame(root)
frame.pack()

# text wrap
root = tk.LabelFrame(frame, text="Version 1.0")
root.grid(row=0, column=0)
res_frame = tk.LabelFrame(frame, text="Info: ")
res_frame.grid(row=4,column=0)
# enter api
api_label = tk.Label(root, font=('System', 15), text="Riot's API key: ")
api_label.grid(row=0, column=0)
api_box = tk.Entry(root, font=('System', 12))
api_box.grid(row=0, column=1, sticky='W')
api_message = tk.Label(root, font=italic_font, text='For the key, get at developer.riotgames.com')
api_message.grid(row=0, column=2, columnspan=10)  # set it own column span
# enter username
userName_label = tk.Label(root, font=('System', 15), text="User name: ")
userName_label.grid(row=1, column=0, sticky='W', pady=(10, 0))
userName_box = tk.Entry(root, font=('System', 12))
userName_box.grid(row=1, column=1, sticky='W', pady=(10, 0))

# choose region
options = ['--Select-- ', 'BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'PH2', 'RU', 'SG2', 'TH2',
           'TR1', 'TW2',
           'VN2']
region_label = tk.Label(root, font=('System', 15), text="Select region: ")
region_label.grid(row=1, column=2, sticky='W', padx=0, pady=(10, 0))
selected_option = tk.StringVar()
drop_down = ttk.Combobox(root, textvariable=selected_option, values=options)
drop_down.grid(row=1, column=3, sticky='W', pady=(10, 0))

# click button
button = tk.Button(root, text="Go!", fg='#F96167', bg='#f9e795', command=get_info)
button.grid(row=3, column=1, sticky='NSEW', pady=(25, 0))


# label to display result
res_label = tk.Text(res_frame)
res_label.grid(row=4,column=0)

if __name__ == '__main__':
    root.mainloop()
