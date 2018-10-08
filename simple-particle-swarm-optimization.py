# Forked from Nathan A. Rooy's repository

# IMPORT DEPENDENCIES --------------------------------------------------------------------------------------------------

import random
import math

from matplotlib import pyplot as plt

# IMPORT GUI DEPENDENCIES ----------------------------------------------------------------------------------------------

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from maingui import Ui_MainWindow   # Main page of the GUI

# COST FUNCTION --------------------------------------------------------------------------------------------------------

# function we are attempting to optimize (minimize)
def func1(x):
    total = 0
    for i in range(len(x)):
        total += x[i] ** 2
    return total

# MAIN -----------------------------------------------------------------------------------------------------------------

# global definitions
globalBestPos = []
globalBestErr = 0
bestCostsX = []
bestCostsY = []
positionsX = []
positionsY = []

class Particle:
    global positionsX
    global positionsY

    def __init__(self, x0):
        self.position_i = []          # particle position
        self.velocity_i = []          # particle velocity
        self.pos_best_i = []          # best position individual
        self.err_best_i = -1          # best error individual
        self.err_i = -1               # error individual

        for i in range(0, num_dimensions):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(x0[i])

    # evaluate current fitness
    def evaluate(self, costFunc):
        self.err_i = costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i
            self.err_best_i = self.err_i
                    
    # update new particle velocity
    def update_velocity(self, pos_best_g, w, c1, c2):
        # w = 0.5       # constant inertia weight (how much to weigh the previous velocity)
        # c1 = 1        # cognitive constant
        # c2 = 2        # social constant
        
        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()
            
            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0, num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]
            
            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = bounds[i][0]

        try:
            positionsX.append(self.position_i[0])
            positionsY.append(self.position_i[1])
        except IndexError:
            pass

class PSO():
    def __init__(self, costFunc, x0, bounds, num_particles, maxiter, w, c1, c2):
        global num_dimensions
        global globalBestPos
        global globalBestErr

        num_dimensions = len(x0)
        err_best_g = -1                   # best error for group
        pos_best_g = []                   # best position for group

        # establish the swarm
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(x0))

        # begin optimization loop
        i = 0
        while i < maxiter:
            #print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, num_particles):
                swarm[j].evaluate(costFunc)

                # determine if current particle is the best (globally)
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position_i)
                    err_best_g = float(swarm[j].err_i)

            # cycle through swarm and update velocities and position
            for j in range(0, num_particles):
                swarm[j].update_velocity(pos_best_g, w, c1, c2)
                swarm[j].update_position(bounds)
            i += 1

            bestCostsX.append(pos_best_g[0])
            bestCostsY.append(pos_best_g[1])

        globalBestErr = err_best_g
        globalBestPos = pos_best_g

        # print final results to console
        print("FINAL:")
        print("Global Best Position:")
        print(pos_best_g)
        print("Global Best Error:")
        print(err_best_g)

        # plot best costs
        self.plotBestCosts(bestCostsX, bestCostsY, pos_best_g)

    def plotBestCosts(self, bestCostsX, bestCostsY, pos_best_g):
        plt.scatter(positionsX, positionsY, color = 'b', label='Individual Best', marker = '.', linewidths = 1)
        plt.scatter(bestCostsX, bestCostsY, color = 'r', label='Global Best', marker = '.', linewidths = 3)
        plt.scatter(pos_best_g[0], pos_best_g[1], color = 'k', label='Global Best', marker = 'x', linewidths = 7)

        plt.title('Particle Swarm Optimization')
        plt.ylabel('Y axis')
        plt.xlabel('X axis')

        plt.show()

if __name__ == "__PSO__":
    main()

# GUI ------------------------------------------------------------------------------------------------------------------
class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionPreset_Inputs.triggered.connect(self.preset_inputs)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionGroup_members.triggered.connect(self.show_members)
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.pushButton.clicked.connect(self.on_click)   # Connect "Run" button to function on_click()
        self.ui.pushButton_2.clicked.connect(self.close)
        self.show()

    @pyqtSlot()     # A decorator to link signals
    def on_click(self):
        initial       = self.ui.lineEdit.text()
        bounds        = self.ui.lineEdit_2.text()
        num_particles = self.ui.lineEdit_3.text()
        maxiter       = self.ui.lineEdit_4.text()
        w             = self.ui.lineEdit_5.text()
        c1            = self.ui.lineEdit_6.text()
        c2            = self.ui.lineEdit_7.text()

        # Convert to list of int type
        initial = list(map(int, initial.strip().split(',')))
        bounds = list(map(int, bounds.strip().split(',')))

        # Convert bounds to a list of list
        valueSize = len(initial)
        tempList = []
        tempBound = []
        for index, value in enumerate(bounds):
            tempList.append(value)
            if (index + 1) % valueSize == 0:
                tempBound.append(tempList)
                tempList = []
        bounds = tempBound

        # Convert to int or float
        num_particles = int(num_particles)
        maxiter = int(maxiter)
        w = float(w)
        c1 = int(c1)
        c2 = int(c2)

        PSO(func1, initial, bounds, num_particles, maxiter, w, c1, c2)
        QMessageBox.question(self, 'Result', "Global Best Position: " + str(globalBestPos)
                             + "\nGlobal Best Error: " + str(globalBestErr),
                             QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def preset_inputs(self):
        self.ui.lineEdit.setText("5, 5")
        self.ui.lineEdit_2.setText("-10, 10, -10, 10")
        self.ui.lineEdit_3.setText("15")
        self.ui.lineEdit_4.setText("30")
        self.ui.lineEdit_5.setText("0.5")
        self.ui.lineEdit_6.setText("1")
        self.ui.lineEdit_7.setText("2")

    @pyqtSlot()
    def show_members(self):
        QMessageBox.question(self, 'Members', "Made by:\nAkash Kumar (3312016009001091)",
                             QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def help(self):
        QMessageBox.question(self, 'Help', "Use comma separated values for inputs."
                                           "\nUse Preset Inputs option from the Menu to use predefined values\n",
                             QMessageBox.Ok, QMessageBox.Ok)

# RUN ------------------------------------------------------------------------------------------------------------------

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

# initial=[5,5]               # initial starting location [x1,x2...]
# bounds=[(-10,10),(-10,10)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
# PSO(func1,initial,bounds,num_particles=15,maxiter=30)

# END ------------------------------------------------------------------------------------------------------------------
