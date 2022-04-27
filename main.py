# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from sympy.solvers import solve
from sympy import Symbol

from fpdf import FPDF


class Problemer:
    length = 0
    Amount = 0
    operations = ["+", "-", "*"]
    variables = ["a", "b", "c", "y", "m", "n"]
    equation = []
    answers = []

    def __init__(self, lenth=10, N=5):
        self.length = lenth
        self.Amount = N

    def arggiver(self, Num, eqflag, var):
        storage = []
        old = '-'
        flag = 0
        if Num == 0:
            if eqflag:
                storage.append("0")
                storage.append("=")
            else:
                storage.append("0")
            return storage
        for j in range(Num):
            coefficient = random.randint(1, 30)
            if not flag and random.randint(0, 100) > 49:
                storage.append(str(coefficient) + var)
                flag = 1
            else:
                flag = 0
                storage.append(str(coefficient))
            if j != Num - 1:
                rem = random.choice(self.operations)
                if old == rem == '*':
                    rem = random.choice(self.operations[:2])
                old = rem
                storage.append(rem)
        if eqflag:
            storage.append("=")

        return storage

    def checkvalid(self, choice):
        for l in range(len(self.equation)):
            if self.equation[0] == '0':
                self.equation[0] = str(random.randint(1, 25)) + choice
            if self.equation[-1] == '0':
                self.equation[-1] = str(random.randint(1, 25)) + choice

    def generator(self):
        counter = 0
        arrayofeq = []

        for i in range(self.Amount):
            flag = 0
            leftsideN = random.randint(0, self.length)
            rightsideN = self.length - leftsideN
            choice = random.choice(self.variables)
            self.equation = self.arggiver(leftsideN, 1, choice)

            part = self.arggiver(rightsideN, 0, choice)
            self.equation += part
            self.checkvalid(choice)
            for i in self.equation:
                if choice in i:
                    flag = 1
                    break

            if not flag:
                n = random.randrange(0, len(self.equation), 2)
                self.equation[n] += choice
            strequ = self.stringgiver()
            arrayofeq.append(strequ)
            self.answers.append(self.Solver(choice))
        return arrayofeq

    def printer(self):
        print(self.equation)

    def stringgiver(self):
        str = ''
        for i in self.equation:
            str += i
            str += ' '
        return str

    def makepdf(self):
        answ = []
        pdf = FPDF()
        pdf2 = FPDF()
        pdf2.add_page()
        pdf2.set_font("Arial", size=15)
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        answ = self.generator()
        x = 0
        for i in answ:
            pdf.cell(0, 20, i,0,1 )
            x += 15
        for i in self.answers:
            pdf2.cell(0, 20, str(i), 0, 1)
        pdf2.output('answers.pdf','F')
        pdf.output('tuto2.pdf', 'F')

    def Solver(self, choice):
        reforged = []
        arr = []
        for i in range(len(self.equation)):
            if self.equation[i] != '=':
                reforged.append(self.equation[i])
            else:
                k = i
                arr = self.equation[(k + 1):]
                break
        reforged.append('-')
        reforged.append("(")
        reforged += arr
        reforged.append(')')

        st = ''
        for i in reforged:
            if choice not in i:
                st += i
            else:
                index = i.find(choice)
                fin = i[:index] + '*' + i[index:]
                st += fin
        v = Symbol(choice)
        return solve(st, v)


if __name__ == '__main__':
    eq = Problemer(3, 13)
    eq.makepdf()
