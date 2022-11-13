import tkinter as tk

app = tk.Tk()
app.title("wrod recognition")
app.geometry("{w}x{h}+{x}+{y}".format(w=300, h=300, x=300, y=300))
app['bg'] = 'white'

label = tk.Label(app, text="SEULKI", fg='white')
label.pack()

app.mainloop()
