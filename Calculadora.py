import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 200)

        self.init_ui()

    def init_ui(self):
        self.resultado_label = QLabel(self)
        self.resultado_label.setText("Resultado:")
        self.resultado_edit = QLineEdit(self)

        self.btn_suma = QPushButton("+", self)
        self.btn_resta = QPushButton("-", self)
        self.btn_multiplicacion = QPushButton("*", self)
        self.btn_division = QPushButton("/", self)

        self.btn_suma.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.restar)
        self.btn_multiplicacion.clicked.connect(self.multiplicar)
        self.btn_division.clicked.connect(self.dividir)

        layout = QVBoxLayout(self)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.resultado_edit)
        layout.addWidget(self.btn_suma)
        layout.addWidget(self.btn_resta)
        layout.addWidget(self.btn_multiplicacion)
        layout.addWidget(self.btn_division)

    def sumar(self):
        resultado = 0
        try:
            num1 = float(self.resultado_edit.text())
            resultado = num1 + float(self.resultado_edit.text())
        except ValueError:
            pass
        self.resultado_edit.setText(str(resultado))

    def restar(self):
        resultado = 0
        try:
            num1 = float(self.resultado_edit.text())
            resultado = num1 - float(self.resultado_edit.text())
        except ValueError:
            pass
        self.resultado_edit.setText(str(resultado))

    def multiplicar(self):
        resultado = 0
        try:
            num1 = float(self.resultado_edit.text())
            resultado = num1 * float(self.resultado_edit.text())
        except ValueError:
            pass
        self.resultado_edit.setText(str(resultado))

    def dividir(self):
        resultado = 0
        try:
            num1 = float(self.resultado_edit.text())
            num2 = float(self.resultado_edit.text())
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        except ValueError:
            pass
        self.resultado_edit.setText(str(resultado))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
