import sys
import os
import csv
import sqlite3
from datetime import date, datetime

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QTabWidget, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QComboBox, QListWidget, QListWidgetItem, QLineEdit,
    QDateEdit, QSpinBox, QSlider, QPushButton, QMessageBox, QFormLayout,
    QDialogButtonBox, QFileDialog, QTableWidget, QTableWidgetItem, QProgressBar
)
from PyQt6.QtCore import Qt, QDate, QTimer, QRectF
from PyQt6.QtGui import QPainter, QColor, QFont, QPixmap, QIcon, QAction


folder = os.path.dirname(os.path.abspath(__file__))
dbfile = os.path.join(folder, "goals.db")
pic = os.path.join(folder, "logo.png")


names = {
    "day": "каждый день",
    "month": "на месяц",
    "long": "долгосрочные"
}


def to_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def get_cat(d):
    days = (d - date.today()).days
    if days <= 1:
        return "day"
    if days <= 30:
        return "month"
    return "long"


db = sqlite3.connect(dbfile)
db.row_factory = sqlite3.Row
db.execute("CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, deadline TEXT, difficulty INTEGER, done INTEGER DEFAULT 0, created TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, goal_name TEXT, action TEXT, moment TEXT)")
db.commit()


class Grafik(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = {"day": [0, 0], "month": [0, 0], "long": [0, 0]}
        self.setMinimumHeight(300)

    def calc(self, goals):
        self.data = {"day": [0, 0], "month": [0, 0], "long": [0, 0]}

        for g in goals:
            k = get_cat(to_date(g["deadline"]))
            self.data[k][0] = self.data[k][0] + 1

            if g["done"]:
                self.data[k][1] = self.data[k][1] + 1

        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()
        p.fillRect(0, 0, w, h, QColor("#fbfbfb"))

        f = QFont("Arial", 13)
        f.setBold(True)
        p.setFont(f)
        p.setPen(QColor("#333"))
        p.drawText(0, 12, w, 30, Qt.AlignmentFlag.AlignCenter, "статистика")

        total = 0
        for k in self.data:
            total = total + self.data[k][0]

        if total == 0:
            p.drawText(0, 0, w, h, Qt.AlignmentFlag.AlignCenter, "пока пусто")
            return

        left = 60
        right = 30
        top = 70
        bottom = 55
        cw = w - left - right
        ch = h - top - bottom

        if cw <= 20 or ch <= 20:
            return

        base = top + ch

        maxv = 1
        for k in self.data:
            if self.data[k][0] > maxv:
                maxv = self.data[k][0]

        p.setPen(QColor("#999"))
        p.drawLine(left, base, left + cw, base)

        labels = {"day": "каждый день", "month": "на месяц", "long": "долгосрочные"}
        gw = cw / 3.0
        bw = gw * 0.18
        gap = gw * 0.06

        i = 0
        for k in ["day", "month", "long"]:
            cx = left + gw * i + gw / 2.0
            done = self.data[k][1]
            rest = self.data[k][0] - done

            dh = ch * done / float(maxv)
            rh = ch * rest / float(maxv)
            x1 = cx - bw - gap / 2.0
            x2 = cx + gap / 2.0

            p.setPen(Qt.PenStyle.NoPen)
            p.setBrush(QColor("#4caf50"))
            p.drawRect(QRectF(x1, base - dh, bw, dh))

            p.setBrush(QColor("#e57373"))
            p.drawRect(QRectF(x2, base - rh, bw, rh))

            p.setPen(QColor("#333"))
            p.setFont(QFont("Arial", 9))
            p.drawText(QRectF(left + gw * i, base + 6, gw, 25),
                       Qt.AlignmentFlag.AlignCenter, labels[k])

            i = i + 1


class Spisok(QWidget):
    def __init__(self, win, cat):
        super().__init__()
        self.win = win
        self.cat = cat

        lay = QVBoxLayout(self)

        top = QHBoxLayout()
        top.addWidget(QLabel("сортировать:"))

        self.sort = QComboBox()
        self.sort.addItems(["по дедлайну", "по сложности", "по названию", "по статусу"])
        top.addWidget(self.sort)
        top.addStretch()

        self.lbl = QLabel("")
        top.addWidget(self.lbl)
        lay.addLayout(top)

        self.spisok = QListWidget()
        lay.addWidget(self.spisok)

        bottom = QHBoxLayout()
        self.btn = QPushButton("удалить")
        bottom.addWidget(self.btn)
        bottom.addStretch()
        lay.addLayout(bottom)

        self.sort.currentIndexChanged.connect(self.reload)
        self.spisok.itemChanged.connect(self.check)
        self.spisok.itemDoubleClicked.connect(self.dbl)
        self.btn.clicked.connect(self.del_)

        self.reload()

    def key(self, g):
        s = self.sort.currentText()

        if s == "по дедлайну":
            return g["deadline"]
        if s == "по сложности":
            return -g["difficulty"]
        if s == "по названию":
            return g["name"].lower()
        return g["done"]

    def reload(self):
        self.spisok.blockSignals(True)
        self.spisok.clear()

        res = [g for g in self.win.goals
               if self.cat == "all" or get_cat(to_date(g["deadline"])) == self.cat]
        res.sort(key=self.key)

        for g in res:
            text = g["name"] + "  |  до " + g["deadline"] + "  |  " + str(g["difficulty"]) + "/10"
            it = QListWidgetItem(text)
            it.setData(Qt.ItemDataRole.UserRole, g["id"])
            it.setFlags(it.flags() | Qt.ItemFlag.ItemIsUserCheckable)

            if g["done"]:
                it.setCheckState(Qt.CheckState.Checked)
            else:
                it.setCheckState(Qt.CheckState.Unchecked)

            self.spisok.addItem(it)

        self.lbl.setText("целей: " + str(len(res)))
        self.spisok.blockSignals(False)

    def check(self, it):
        self.win.done(it.data(Qt.ItemDataRole.UserRole), it.checkState() == Qt.CheckState.Checked)

    def dbl(self, it):
        self.win.edit(it.data(Qt.ItemDataRole.UserRole))

    def del_(self):
        it = self.spisok.currentItem()

        if it is None:
            QMessageBox.information(self, "удаление", "выбери цель")
            return

        answer = QMessageBox.question(self, "удаление", "удалить?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer == QMessageBox.StandardButton.Yes:
            self.win.remove(it.data(Qt.ItemDataRole.UserRole))


class Stat(QWidget):
    def __init__(self, win):
        super().__init__()

        lay = QVBoxLayout(self)

        self.lbl = QLabel("")
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        f = self.lbl.font()
        f.setPointSize(12)
        f.setBold(True)
        self.lbl.setFont(f)
        lay.addWidget(self.lbl)

        self.bar = QProgressBar()
        self.bar.setRange(0, 100)
        lay.addWidget(self.bar)

        self.graf = Grafik()
        lay.addWidget(self.graf)
        lay.addStretch()

    def reload(self, goals):
        total = len(goals)
        done = 0

        for g in goals:
            if g["done"]:
                done = done + 1

        pr = 0
        if total > 0:
            pr = int(round(done * 100.0 / total))

        self.lbl.setText("всего: " + str(total) + "    выполнено: " + str(done) + "    (" + str(pr) + "%)")
        self.bar.setValue(pr)
        self.graf.calc(goals)


class NewGoal(QWidget):
    def __init__(self, win):
        super().__init__()
        self.win = win

        lay = QVBoxLayout(self)

        form = QFormLayout()

        self.name = QLineEdit()
        form.addRow("цель:", self.name)

        self.date = QDateEdit()
        self.date.setCalendarPopup(True)
        self.date.setMinimumDate(QDate.currentDate())
        self.date.setDate(QDate.currentDate().addDays(1))
        form.addRow("дедлайн:", self.date)

        self.diff = QSpinBox()
        self.diff.setRange(1, 10)
        self.diff.setValue(5)
        form.addRow("сложность (1-10):", self.diff)

        lay.addLayout(form)

        self.lbl = QLabel("")
        lay.addWidget(self.lbl)

        self.btn = QPushButton("создать цель")
        lay.addWidget(self.btn)
        lay.addStretch()

        self.btn.clicked.connect(self.add)
        self.date.dateChanged.connect(self.show_cat)

        self.show_cat()

    def show_cat(self, *args):
        cat = get_cat(self.date.date().toPyDate())
        self.lbl.setText("раздел: " + names[cat])

    def add(self):
        name = self.name.text().strip()

        if name == "":
            QMessageBox.warning(self, "ошибка", "пусто")
            return

        d = self.date.date().toPyDate()

        if d < date.today():
            QMessageBox.warning(self, "ошибка", "дата прошла")
            return

        cat = get_cat(d)
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        db.execute("INSERT INTO goals (name, deadline, difficulty, done, created) VALUES (?, ?, ?, 0, ?)",
                   (name, d.strftime("%Y-%m-%d"), self.diff.value(), now))
        db.execute("INSERT INTO events (goal_name, action, moment) VALUES (?, ?, ?)",
                   (name, "создана", now))
        db.commit()

        self.win.reload()
        self.name.clear()

        QMessageBox.information(self, "готово", "цель добавлена в раздел: " + names[cat])


class ChangeGoal(QDialog):
    def __init__(self, parent=None, g=None):
        super().__init__(parent)

        if g is None:
            self.setWindowTitle("новая цель")
        else:
            self.setWindowTitle("изменить")

        self.setMinimumWidth(420)

        lay = QVBoxLayout(self)
        form = QFormLayout()

        self.name = QLineEdit()
        form.addRow("цель:", self.name)

        self.date = QDateEdit()
        self.date.setCalendarPopup(True)
        self.date.setMinimumDate(QDate.currentDate())
        self.date.setDate(QDate.currentDate().addDays(1))
        form.addRow("дедлайн:", self.date)

        d = 5
        if g is not None:
            d = g["difficulty"]

        self.sl = QSlider(Qt.Orientation.Horizontal)
        self.sl.setRange(1, 10)
        self.sl.setValue(d)
        form.addRow("сложность:", self.sl)

        self.diff = QSpinBox()
        self.diff.setRange(1, 10)
        self.diff.setValue(d)
        form.addRow("", self.diff)

        lay.addLayout(form)

        self.lbl = QLabel("")
        lay.addWidget(self.lbl)

        btns = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        btns.accepted.connect(self.check)
        btns.rejected.connect(self.reject)
        lay.addWidget(btns)

        self.sl.valueChanged.connect(self.diff.setValue)
        self.diff.valueChanged.connect(self.sl.setValue)
        self.date.dateChanged.connect(self.show_cat)

        if g is not None:
            self.name.setText(g["name"])
            self.date.setDate(QDate.fromString(g["deadline"], "yyyy-MM-dd"))

        self.show_cat()

    def show_cat(self, *args):
        cat = get_cat(self.date.date().toPyDate())
        self.lbl.setText("раздел: " + names[cat])

    def check(self):
        if self.name.text().strip() == "":
            QMessageBox.warning(self, "ошибка", "пусто")
            return

        if self.date.date().toPyDate() < date.today():
            QMessageBox.warning(self, "ошибка", "дата прошла")
            return

        self.accept()

    def get(self):
        d = self.date.date().toPyDate()
        return self.name.text().strip(), d.strftime("%Y-%m-%d"), self.diff.value()


class History(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("история")
        self.resize(620, 400)

        lay = QVBoxLayout(self)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["когда", "цель", "действие"])
        lay.addWidget(self.table)

        btns = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        btns.rejected.connect(self.accept)
        lay.addWidget(btns)

        rows = db.execute("SELECT * FROM events ORDER BY id DESC").fetchall()
        self.table.setRowCount(len(rows))

        for i in range(len(rows)):
            self.table.setItem(i, 0, QTableWidgetItem(rows[i]["moment"]))
            self.table.setItem(i, 1, QTableWidgetItem(rows[i]["goal_name"]))
            self.table.setItem(i, 2, QTableWidgetItem(rows[i]["action"]))


class Win(QMainWindow):
    def __init__(self):
        super().__init__()

        self.goals = []

        self.setWindowTitle("мои цели")
        self.resize(980, 720)

        if os.path.exists(pic):
            self.setWindowIcon(QIcon(pic))

        self.menu()
        self.ui()

        self.reload()

    def act(self, text, slot):
        a = QAction(text, self)
        a.triggered.connect(slot)
        return a

    def menu(self):
        m = self.menuBar()

        f = m.addMenu("файл")
        f.addAction(self.act("экспорт", self.export))
        f.addAction(self.act("импорт", self.import_))
        f.addAction(self.act("отчёт", self.report))
        f.addSeparator()
        f.addAction(self.act("выход", self.close))

        h = m.addMenu("справка")
        h.addAction(self.act("история", self.history))
        h.addAction(self.act("о программе", self.about))

    def ui(self):
        central = QWidget()
        lay = QVBoxLayout(central)

        top = QHBoxLayout()

        if os.path.exists(pic):
            p = QLabel()
            p.setPixmap(QPixmap(pic).scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio))
            top.addWidget(p)

        title = QLabel("мои цели")
        title.setFont(QFont("Arial", 18))
        top.addWidget(title)
        top.addStretch()

        lay.addLayout(top)

        self.tabs = QTabWidget()

        goals_tab = QWidget()
        goals_lay = QVBoxLayout(goals_tab)
        inner = QTabWidget()

        self.spiski = [Spisok(self, "all"), Spisok(self, "day"),
                       Spisok(self, "month"), Spisok(self, "long")]
        titles = ["все", "каждый день", "на месяц", "долгосрочные"]

        for i in range(len(self.spiski)):
            inner.addTab(self.spiski[i], titles[i])

        goals_lay.addWidget(inner)
        self.tabs.addTab(goals_tab, "цели")

        self.stat = Stat(self)
        self.tabs.addTab(self.stat, "статистика")

        self.new = NewGoal(self)
        self.tabs.addTab(self.new, "создание")

        lay.addWidget(self.tabs)
        self.setCentralWidget(central)

    def reload(self):
        rows = db.execute("SELECT * FROM goals ORDER BY id").fetchall()

        self.goals = []
        for r in rows:
            self.goals.append({
                "id": r["id"],
                "name": r["name"],
                "deadline": r["deadline"],
                "difficulty": r["difficulty"],
                "done": bool(r["done"])
            })

        for s in self.spiski:
            s.reload()

        self.stat.reload(self.goals)

        done = 0
        for g in self.goals:
            if g["done"]:
                done = done + 1

        self.statusBar().showMessage("целей: " + str(len(self.goals)) + ", выполнено: " + str(done))

    def done(self, gid, value):
        row = db.execute("SELECT name FROM goals WHERE id = ?", (gid,)).fetchone()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        db.execute("UPDATE goals SET done = ? WHERE id = ?", (int(value), gid))
        db.execute("INSERT INTO events (goal_name, action, moment) VALUES (?, ?, ?)",
                   (row["name"], "выполнена" if value else "снова в работе", now))
        db.commit()

        QTimer.singleShot(0, self.reload)

    def remove(self, gid):
        row = db.execute("SELECT name FROM goals WHERE id = ?", (gid,)).fetchone()
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        db.execute("DELETE FROM goals WHERE id = ?", (gid,))
        db.execute("INSERT INTO events (goal_name, action, moment) VALUES (?, ?, ?)",
                   (row["name"], "удалена", now))
        db.commit()

        self.reload()

    def edit(self, gid):
        g = None
        for x in self.goals:
            if x["id"] == gid:
                g = x
                break

        if g is None:
            return

        dlg = ChangeGoal(self, g)

        if dlg.exec() == QDialog.DialogCode.Accepted:
            name, deadline, diff = dlg.get()
            now = datetime.now().strftime("%Y-%m-%d %H:%M")

            db.execute("UPDATE goals SET name = ?, deadline = ?, difficulty = ? WHERE id = ?",
                       (name, deadline, diff, gid))
            db.execute("INSERT INTO events (goal_name, action, moment) VALUES (?, ?, ?)",
                       (name, "изменена", now))
            db.commit()

            self.reload()

    def history(self):
        History(self).exec()

    def about(self):
        box = QMessageBox(self)
        box.setWindowTitle("о программе")
        box.setText("мои цели\nпроект на PyQt6")

        if os.path.exists(pic):
            box.setIconPixmap(QPixmap(pic).scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio))

        box.exec()

    def export(self):
        path, _ = QFileDialog.getSaveFileName(self, "экспорт", "goals.csv", "CSV (*.csv)")

        if path == "":
            return

        try:
            f = open(path, "w", encoding="utf-8", newline="")
            w = csv.writer(f)
            w.writerow(["цель", "дедлайн", "сложность", "выполнено"])

            for g in self.goals:
                if g["done"]:
                    st = "да"
                else:
                    st = "нет"

                w.writerow([g["name"], g["deadline"], g["difficulty"], st])

            f.close()
            QMessageBox.information(self, "экспорт", "готово")
        except Exception:
            QMessageBox.warning(self, "ошибка", "не вышло")

    def import_(self):
        path, _ = QFileDialog.getOpenFileName(self, "импорт", "", "CSV (*.csv)")

        if path == "":
            return

        try:
            f = open(path, "r", encoding="utf-8")
            rows = list(csv.reader(f))
            f.close()
        except:
            QMessageBox.warning(self, "ошибка", "не вышло")
            return

        n = 0

        for row in rows[1:]:
            if len(row) < 3 or row[0].strip() == "":
                continue

            try:
                to_date(row[1].strip())
            except:
                continue

            try:
                diff = int(row[2])
            except:
                diff = 5

            if diff < 1:
                diff = 1
            if diff > 10:
                diff = 10

            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            name = row[0].strip()

            db.execute("INSERT INTO goals (name, deadline, difficulty, done, created) VALUES (?, ?, ?, 0, ?)",
                       (name, row[1].strip(), diff, now))
            db.execute("INSERT INTO events (goal_name, action, moment) VALUES (?, ?, ?)",
                       (name, "импорт", now))
            n = n + 1

        db.commit()
        self.reload()

        QMessageBox.information(self, "импорт", "добавлено: " + str(n))

    def report(self):
        path, _ = QFileDialog.getSaveFileName(self, "отчёт", "report.txt", "TXT (*.txt)")

        if path == "":
            return

        done = 0
        for g in self.goals:
            if g["done"]:
                done = done + 1

        lines = []
        lines.append("отчёт")
        lines.append("дата: " + str(date.today()))
        lines.append("всего: " + str(len(self.goals)))
        lines.append("выполнено: " + str(done))
        lines.append("")

        for g in self.goals:
            if g["done"]:
                st = "готово"
            else:
                st = "не готово"

            lines.append(g["name"] + " | " + g["deadline"] + " | " + str(g["difficulty"]) + " | " + st)

        try:
            f = open(path, "w", encoding="utf-8")
            f.write("\n".join(lines))
            f.close()
            QMessageBox.information(self, "отчёт", "готово")
        except:
            QMessageBox.warning(self, "ошибка", "не вышло")

    def closeEvent(self, event):
        answer = QMessageBox.question(self, "выход", "закрыть программу?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if answer == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    w = Win()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()