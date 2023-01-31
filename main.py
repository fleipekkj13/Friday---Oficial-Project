import eel
eel.init("web", allowed_extensions=['.js', '.html'])


@eel.expose
def main_window():
    print("Olá mundo!")
    eel.start("main.html")

@eel.expose
def main_login():
    eel.start("frist_login.html",size=(1240, 740), position=(0,0))
main_login()
