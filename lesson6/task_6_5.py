class Stationery:
    title = "Уроки рисования"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("рисовать ручкой удобно на плотной бумаге")


class Pencil(Stationery):
    def draw(self):
        print("карандаши для рисования и черчения отличаются мягкостью грифеля")


class Handle(Stationery):
    def draw(self):
        print("маркер подходит для рисования на больших ватманах")


st = Stationery()
st.draw()

p_n = Pen()
p_n.draw()

p_l = Pencil()
p_l.draw()

p_l = Handle()
p_l.draw()
