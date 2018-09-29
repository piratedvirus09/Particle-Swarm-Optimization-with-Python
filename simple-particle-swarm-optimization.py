#   Forked from Nathan A. Rooy's repository

# IMPORT DEPENDENCIES

import random
import math

# IMPORT GUI DEPENDENCIES
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from maingui import Ui_MainWindow   # Main page of the GUI

# COST FUNCTION

# function we are attempting to optimize (minimize)
def func1(x,y):
    total=0
    for i in range(len(x)):
        total+=x[i]**2 + y[i]**2
    return total

# MAIN

class Particle:
    def __init__(self, x0, y0):
        self.position_i_x = []  # particle position
        self.position_i_y = []
        self.velocity_i_x = []  # particle velocity
        self.velocity_i_y = []
        self.pos_best_i_x = []  # best position individual
        self.pos_best_i_y = []
        self.err_best_i = -1  # best error individual
        self.err_i = -1  # error individual

        for i in range(0, num_dimensions):
            self.velocity_i_x.append(random.uniform(-1, 1))
            self.position_i_x.append(x0[i])
            self.velocity_i_y.append(random.uniform(-1, 1))
            self.position_i_y.append(x0[i])

    # evaluate current fitness
    def evaluate(self, costFunc):
        self.err_i = costFunc(self.position_i_x, self.position_i_y)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i_x = self.position_i_x
            self.pos_best_i_y = self.position_i_y
            self.err_best_i = self.err_i

    # update new particle velocity
    def update_velocity(self, pos_best_g_x, pos_best_g_y):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 1  # cognative constant
        c2 = 2  # social constant

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.pos_best_i_x[i] - self.position_i_x[i])
            vel_social = c2 * r2 * (pos_best_g_x[i] - self.position_i_x[i])
            self.velocity_i_x[i] = w * self.velocity_i_x[i] + vel_cognitive + vel_social

            vel_cognitive = c1 * r1 * (self.pos_best_i_y[i] - self.position_i_y[i])
            vel_social = c2 * r2 * (pos_best_g_y[i] - self.position_i_y[i])
            self.velocity_i_y[i] = w * self.velocity_i_y[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self, bounds_x, bounds_y):
        for i in range(0, num_dimensions):
            self.position_i_x[i] = self.position_i_x[i] + self.velocity_i_x[i]
            self.position_i_y[i] = self.position_i_y[i] + self.velocity_i_y[i]

            # adjust maximum position if necessary
            if self.position_i_x[i] > bounds_x[i][1]:
                self.position_i_x[i] = bounds_x[i][1]

            if self.position_i_y[i] > bounds_y[i][1]:
                self.position_i_y[i] = bounds_y[i][1]

            # plt.plot(self.position_i_x,self.position_i_y)

            # adjust minimum position if neseccary
            if self.position_i_x[i] < bounds_x[i][0]:
                self.position_i_x[i] = bounds_x[i][0]

            if self.position_i_y[i] < bounds_y[i][0]:
                self.position_i_y[i] = bounds_y[i][0]

            # plt.plot(self.position_i_x, self.position_i_y)

globalBestPosX = []
globalBestPosY = []
globalBestErr = 0


class PSO():
    def __init__(self, costFunc, x0, y0, bounds_x, bounds_y, num_particles, maxiter):
        global num_dimensions
        global globalBestPosX
        global globalBestPosY
        global globalBestErr

        num_dimensions = len(x0)
        err_best_g = -1  # best error for group
        pos_best_g_x = []  # best position for group
        pos_best_g_y = []

        # establish the swarm
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(x0, y0))

        # begin optimization loop
        i = 0
        while i < maxiter:
            # print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, num_particles):
                swarm[j].evaluate(costFunc)

                # determine if current particle is the best (globally)
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g_x = list(swarm[j].position_i_x)
                    pos_best_g_y = list(swarm[j].position_i_y)
                    err_best_g = float(swarm[j].err_i)

            # cycle through swarm and update velocities and position
            for j in range(0, num_particles):
                swarm[j].update_velocity(pos_best_g_x, pos_best_g_y)
                swarm[j].update_position(bounds_x, bounds_y)
            i += 1


        globalBestErr = err_best_g
        globalBestPosX = pos_best_g_x
        globalBestPosY = pos_best_g_y

        # print final results
        print('FINAL:')
        print('X: ')
        print(pos_best_g_x)
        print('Y: ')
        print(pos_best_g_y)
        print(err_best_g)

if __name__ == "__PSO__":
    main()

# RUN
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
        initial_x      = self.ui.lineEdit.text()
        initial_y      = self.ui.lineEdit_2.text()
        bounds_x       = self.ui.lineEdit_3.text()
        bounds_y       = self.ui.lineEdit_4.text()
        num_particles = self.ui.lineEdit_5.text()
        maxiter       = self.ui.lineEdit_6.text()

        # Convert to list of int type
        initial_x = list(map(int, initial_x.strip().split(',')))
        initial_y = list(map(int, initial_y.strip().split(',')))
        bounds_x = list(map(int, bounds_x.strip().split(',')))
        bounds_y = list(map(int, bounds_y.strip().split(',')))

        # Convert bounds to a list of list
        bounds_x = self.formatBounds(bounds_x, initial_x)
        bounds_y = self.formatBounds(bounds_y, initial_y)

        # Convert to int
        num_particles = int(num_particles)
        maxiter = int(maxiter)

        PSO(func1, initial_x, initial_y, bounds_x, bounds_y, num_particles, maxiter)
        QMessageBox.question(self, 'Result', "Global Best Position (X): " + str(globalBestPosX) + "\nGlobal Best Position (Y): " + str(globalBestPosY) + "\nGlobal Best Error: " + str(globalBestErr), QMessageBox.Ok, QMessageBox.Ok)

    def formatBounds(self, bounds, initial):
        valueSize = len(initial)
        tempList = []
        tempBound = []
        for index, value in enumerate(bounds):
            tempList.append(value)
            if (index + 1) % valueSize == 0:
                tempBound.append(tempList)
                tempList = []
        bounds = tempBound
        return bounds

    @pyqtSlot()
    def preset_inputs(self):
        self.ui.lineEdit.setText("5, 5")
        self.ui.lineEdit_2.setText("5, 5")
        self.ui.lineEdit_3.setText("-10, 10, -10, 10")
        self.ui.lineEdit_4.setText("-10, 10, -10, 10")
        self.ui.lineEdit_5.setText("15")
        self.ui.lineEdit_6.setText("30")

    @pyqtSlot()
    def show_members(self):
        QMessageBox.question(self, 'Members', "Made by:\nAkash Kumar (3312016009001091)\nArijit Roy (3312016009001066)", QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def help(self):
        QMessageBox.question(self, 'Help', "Use comma separated values for inputs.\nUse Preset Inputs option from the Menu to use predefined values\n", QMessageBox.Ok, QMessageBox.Ok)



app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

# initial=[5,5]               # initial starting location [x1,x2...]
# bounds=[(-10,10),(-10,10)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
# PSO(func1,initial,bounds,num_particles=15,maxiter=30)
# END
