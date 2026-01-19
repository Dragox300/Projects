import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

def solve_expression(expr):
    try:
        result = eval(expr)
        return str(result)
    except Exception as e:
        return "Error"
class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.last_input = None
        self.input_line = QLineEdit(self)
        self.input_line.setPlaceholderText('Enter expression')
        layout.addWidget(self.input_line)

        self.result_label = QLabel('Result: ', self)
        layout.addWidget(self.result_label)

        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_result)
        layout.addWidget(self.calculate_button)

        self.steps_button = QPushButton('Show Steps', self)
        self.steps_button.clicked.connect(self.show_steps)
        layout.addWidget(self.steps_button)

        self.setLayout(layout)

    def calculate_result(self):
        expr = self.input_line.text()
        self.last_input = expr
        result = solve_expression(expr)
        self.result_label.setText(f'Result: {result}')
    def show_steps(self):
        if self.last_input is None:
            self.result_label.setText('Result: No previous input')
            return
        operators = set('+-*/')
        Numbers = list()
        operators_list = list()
        for char in self.last_input:
            if char not in '0123456789. ' and char not in operators:
                self.result_label.setText('Result: Steps not available for this expression')
                return
            elif char in operators:
                operators_list.append(char)
                self.last_input = self.last_input[1:]
            else:
                num = ''
                while char in '0123456789.':
                    num += char
                    if len(self.last_input) > 1:
                        self.last_input = self.last_input[1:]
                        char = self.last_input[0]
                    else:
                        break
                Numbers.append(float(num))
            
        steps = list()
        count = 1
        while operators_list:
            for i, op in enumerate(operators_list):
                if op in '*/':
                    if op == '*':
                        res = Numbers[i] * Numbers[i+1]
                    else:
                        res = Numbers[i] / Numbers[i+1]
                    steps.append(f"Step {count} = {Numbers[i]} {op} {Numbers[i+1]} = {res}")
                    Numbers[i] = res
                    Numbers.pop(i+1)
                    operators_list.pop(i)
                    count += 1
                    break
            else:
                op = operators_list[0]
                if op == '+':
                    res = Numbers[0] + Numbers[1]
                else:
                    res = Numbers[0] - Numbers[1]
                steps.append(f"Step {count} = {Numbers[0]} {op} {Numbers[1]} = {res}")
                Numbers[0] = res
                Numbers.pop(1)
                operators_list.pop(0)
                count += 1
        steps.append(f"Final Result: {Numbers[0]}")
        self.result_label.setText(f'Result: {steps}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = SimpleCalculator()
    calculator.show()
    sys.exit(app.exec_())

    

