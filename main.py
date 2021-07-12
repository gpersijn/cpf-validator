import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import InterfaceGrafica2.Aula148.deisgn2 as design2
from InterfaceGrafica2.Aula148.Validador_cpf import validador_cpf
from ProjetoCPF.CPF.Gerador2CPF import gerar_cpf


class GeraValidaCPF(QMainWindow, design2.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)  # Leva ao layout criado

        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
           gerar_cpf()
        )

    def valida_cpf(self):
        cpf = str(self.inputValidaCPF.text())
        self.labelRetorno.setText(
            str(validador_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    geravalida = GeraValidaCPF()
    geravalida.show()
    qt.exec_()
