import datetime
import sys
import math
import scipy
import re
import pyqtgraph as pg
from scipy.interpolate import interp1d
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QDateTimeEdit, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from datetime import datetime, timedelta, time




class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)

        #butoane
        self.plus.clicked.connect(self.addrow)
        self.minus.clicked.connect(self.removerow)
        self.calculeaza.clicked.connect(self.calcul)
        self.exemplubutton.clicked.connect(self.gotoexemplu)
        self.homebutton.clicked.connect(self.gotohome)
        self.ajutorbutton.clicked.connect(self.gotoajutor)
        self.desprebutton.clicked.connect(self.gotodespre)

        #fundal
        fundal = QPixmap('fundal aplicatie.jpg')
        self.fundal.setPixmap(fundal)

        #formatarecoloanetabele
        self.tabelvalori.setColumnWidth(0,150)
        self.tabelvalori.setColumnWidth(1, 150)
        self.tabelvalori.setColumnWidth(2, 100)
        self.tabelrezultate.setColumnWidth(0, 150)
        self.tabelrezultate.setColumnWidth(1, 150)
        self.tabelrezultate.setColumnWidth(2, 100)

        #customizaregrafic
        self.graphWidget.setBackground('white')
        #pen = self.graphWidget.mkPen(color=(255, 0, 0), width=8, style=QtCore.Qt.DashLine)
        self.graphWidget.setLabel('bottom', 'Latitudine(φ)', units = 'grade, minute, secunde')
        self.graphWidget.setLabel('left', 'Longitudine(λ)', units = 'grade, minute, secunde')
        self.graphWidget.setXRange(28, 31)
        self.graphWidget.setYRange(43, 46)




#functii
    def gotodespre(self):
        widget.setCurrentWidget(despre)

    def gotoajutor(self):
        widget.setCurrentWidget(ajutor)

    def gotohome(self):
        widget.setCurrentWidget(first)

    def gotoexemplu(self):
        widget.setCurrentWidget(exemplu)

    def addrow(self):
        rowcount = self.tabelvalori.rowCount()
        self.tabelvalori.insertRow(rowcount)
        rowcount = self.tabelrezultate.rowCount()
        self.tabelrezultate.insertRow(rowcount)
        #setarecoloanaora
        #i = 0
        #for i in range (0, self.tabelvalori.rowCount()):
            #dateTime = QDateTimeEdit();
            #dateTime.setDisplayFormat("hh:mm");
            #dateTime.setFrame(False);
            #self.tabelvalori.setCellWidget(i, 2, dateTime)

        #for i in range (0, self.tabelrezultate.rowCount()):
            #dateTime = QDateTimeEdit();
            #dateTime.setDisplayFormat("hh:mm");
            #dateTime.setFrame(False);
            #self.tabelrezultate.setCellWidget(i, 2, dateTime)

        #for i in range (0, self.tabelvalori.rowCount()):
            #dateTime = QDateTimeEdit();
            #dateTime.setDisplayFormat("hh:mm");
            #dateTime.setFrame(False);
            #self.tabelvalori.setCellWidget(i, 11, dateTime)


    def removerow(self):
        if self.tabelvalori.rowCount() > 0:
            self.tabelvalori.removeRow(self.tabelvalori.rowCount() - 1)
        if self.tabelrezultate.rowCount() > 0:
            self.tabelrezultate.removeRow(self.tabelrezultate.rowCount() - 1)

    def calcul(self):
        #calcul d2022
        d2021 = 6 + (19/60)
        var = 6/60
        d2022 = d2021 + var
        self.d2022.setText(str(format(d2022, '.1f'))+'°')
        i = 0
        nrrows = self.tabelrezultate.rowCount()
        lambdas = []
        phis = []
        for i in range (0, nrrows):

            #phi si lambda
            lat = self.tabelvalori.item(i, 0)
            lat = lat.text()
            lon = self.tabelvalori.item(i, 1)
            lon = lon.text()
            self.tabelrezultate.setItem(i, 0, QtWidgets.QTableWidgetItem(str(lat)))
            self.tabelrezultate.setItem(i, 1, QtWidgets.QTableWidgetItem(str(lon)))
            lat = sum(float(x) / 60 ** n for n, x in enumerate(lat[:-1].split('-'))) * (
                1 if 'E' in lat[-1] else -1)
            lon = sum(float(x) / 60 ** n for n, x in enumerate(lon[:-1].split('-'))) * (
                1 if 'N' in lon[-1] else -1)
            phis.append(lat)
            lambdas.append(lon)

            #calculviteza
            vn = self.tabelvalori.item(i, 5)
            vl = self.tabelvalori.item(i, 4)
            f = self.tabelvalori.item(i, 12)
            vn = float(vn.text())
            vl = float(vl.text())
            f = float(f.text())
            if vn == 0:
                vn = vl*f
                self.tabelrezultate.setItem(i, 6, QtWidgets.QTableWidgetItem(str(format(vn, '.1f'))+'Nd'))
            else:
                self.tabelrezultate.setItem(i, 6, QtWidgets.QTableWidgetItem(str(format(vn, '.1f')) + 'Nd'))

            #calculvitezalaloch
            #vn = self.tabelvalori.item(i, 5)
            #vl = self.tabelvalori.item(i, 4)
            #f = self.tabelvalori.item(i, 12)
            #vn = float(vn.text())
            #vl = float(vl.text())
            #f = float(f.text())
            #if vl == 0:
                #vl = vn/f
                #self.tabelrezultate.setItem(i, 6, QtWidgets.QTableWidgetItem(str(format(vl, '.1f'))+'Nd'))
            #else:
                #self.tabelrezultate.setItem(i, 6, QtWidgets.QTableWidgetItem(str(format(vl, '.1f')) + 'Nd'))

            #calculora
            ora = self.tabelvalori.item(i, 2)
            ora = ora.text()
            deltat = self.tabelvalori.item(i, 11)
            deltat = int(deltat.text())
            if ora == '0':
                oraanterioara = self.tabelrezultate.item(i - 1, 2)
                oraanterioara = oraanterioara.text()
                oraanterioara = datetime.strptime(oraanterioara, '%H:%M:%S').time()
                delta = timedelta(minutes=deltat)
                oranoua = (datetime.combine(datetime(1,1,1),oraanterioara) + delta).time()
                self.tabelrezultate.setItem(i, 2, QtWidgets.QTableWidgetItem(str(oranoua)))
            else:
                ora = datetime.strptime(ora, '%H:%M:%S').time()
                self.tabelrezultate.setItem(i, 2, QtWidgets.QTableWidgetItem(str(ora)))

            #calculdistanta
            if i > 0:
               vitezaanterioara = self.tabelrezultate.item(i-1, 6)
               #vitezaanterioara = vitezaanterioara.text()
               #vitezaanterioara = vitezaanterioara.replace
               vitezaanterioara = float(vitezaanterioara.text().replace('Nd',''))
            if deltat > 0:
                m = (vitezaanterioara * deltat)/60
                self.tabelrezultate.setItem(i, 4, QtWidgets.QTableWidgetItem(str(format(m, '.1f')) + 'Mm'))
            elif deltat == 0:
                if i > 0:
                    oraanterioara = self.tabelrezultate.item(i - 1, 2)
                    oraanterioara = oraanterioara.text()
                    oraanterioara = datetime.strptime(oraanterioara, '%H:%M:%S').time()
                    oraactuala = self.tabelrezultate.item(i, 2)
                    oraactuala = oraactuala.text()
                    oraactuala = datetime.strptime(oraactuala, '%H:%M:%S').time()
                    deltat = (datetime.combine(datetime(1,1,1,0,0,0), oraactuala) - datetime.combine(datetime(1,1,1,0,0,0), oraanterioara))
                    minutes = (deltat.seconds//60)%60
                    hours = ((deltat.seconds)//3600)*60
                    deltat = minutes + hours
                    m = (vitezaanterioara*deltat)/60
                    self.tabelrezultate.setItem(i, 4, QtWidgets.QTableWidgetItem(str(format(m, '.1f'))+'Mm'))
                else:
                    m = 0
                    self.tabelrezultate.setItem(i, 4, QtWidgets.QTableWidgetItem(str(format(m, '.1f')) + 'Mm'))

            #calculdistantalaloc
            #cl = self.tabelvalori.item(i, 3)
            #cl = float(cl.text())
            #clanterior = self.tabelrezultate.item(i - 1, 3)
            #clanterior = float(clanterior.text())
            #if m == 0:
                #ml = clanterior - cl
                #self.tabelrezultate.setItem(i, 5, QtWidgets.QTableWidgetItem(str(format(ml, '.1f'))))
            #else:
            if i > 0:
                ml = m / f
                self.tabelrezultate.setItem(i, 5, QtWidgets.QTableWidgetItem(str(format(ml, '.1f'))))
            else:
                ml = 0
                self.tabelrezultate.setItem(i, 5, QtWidgets.QTableWidgetItem(str(format(ml, '.1f'))))

            #calculfactordecorectie
            #vn = self.tabelvalori.item(i, 5)
            #vl = self.tabelvalori.item(i, 4)
            #f = self.tabelvalori.item(i, 12)
            #vn = float(vn.text())
            #vl = float(vl.text())
            #f = float(f.text())
            #m= self.tabelrezultate.item(i, 4)
            #ml = self.tabelrezultate.item(i, 5)
            #m = float(m.text())
            #ml = float(ml.text())
            #if f == 0 and vn > 0 and vl > 0:
                #f = vn/vl
            #elif f == 0 and m > 0 and ml > 0:
                #f = m/ml


            #calcul citirelaloc
            cl = self.tabelvalori.item(i, 3)
            cl = float(cl.text())
            if cl == 0:
                clanterior = self.tabelrezultate.item(i-1, 3)
                clanterior = float(clanterior.text())
                cl = clanterior + ml
                self.tabelrezultate.setItem(i, 3, QtWidgets.QTableWidgetItem(str(format(cl, '.1f'))))
            else:
                self.tabelrezultate.setItem(i, 3, QtWidgets.QTableWidgetItem(str(format(cl, '.1f'))))

            #calculdrumadevarat
            da = self.tabelvalori.item(i, 6)
            da = float(da.text())
            dg = self.tabelvalori.item(i, 7)
            dg = float(dg.text())
            dm = self.tabelvalori.item(i, 9)
            dm = float(dm.text())

            if i < nrrows-1:
                if da == 0 and dg > 0:
                    deltag = self.tabelvalori.item(i, 10)
                    deltag = float(deltag.text())
                    da = dg + deltag
                    self.tabelrezultate.setItem(i, 7, QtWidgets.QTableWidgetItem(str(format(da, '.1f'))+'°'))
                elif da == 0 and dg == 0 and dm > 0:
                    da = dm + d2022
                    self.tabelrezultate.setItem(i, 7, QtWidgets.QTableWidgetItem(str(format(da, '.1f'))+'°'))
                elif da>0:
                    da = da
                    self.tabelrezultate.setItem(i, 7, QtWidgets.QTableWidgetItem(str(format(da, '.1f')) + '°'))
            elif i == nrrows-1:
                da == 0
                self.tabelrezultate.setItem(i, 7, QtWidgets.QTableWidgetItem(str(format(da, '.1f')) + '°'))
            #elif da == 0 and dg == 0 and dm == 0:
                #da = 0
                #self.tabelrezultate.setItem(i, 7, QtWidgets.QTableWidgetItem(str(format(da, '.1f')) + '°'))

            if da > 360:
                da = da-360
                self.tabelrezultate.setItem(i, 7, QtWidgets.QTableWidgetItem(str(format(da, '.1f')) + '°'))
            if da < 0:
                da = da+360
                self.tabelrezultate.setItem(i, 7, QtWidgets.QTableWidgetItem(str(format(da, '.1f')) + '°'))

            #calculcorectiegiro
            #dg = self.tabelvalori.item(i, 7)
            #dg = float(dg.text())
            #deltag = self.tabelvalori.item(i, 10)
            #deltag = float(deltag.text())
            #da = self.tabelvalori.item(i, 6)
            #da = float(da.text())
            #if deltag == 0:
                #deltag = da - dg

            #calculdrumgiro
            dg = self.tabelvalori.item(i, 7)
            dg = float(dg.text())
            deltag = self.tabelvalori.item(i, 10)
            deltag = float(deltag.text())

            if i < nrrows-1:
                if dg == 0:
                    dg = da - deltag
                    self.tabelrezultate.setItem(i, 8, QtWidgets.QTableWidgetItem(str(format(dg, '.1f'))+'°'))
            #elif dg == 0 and da == 0:
                #dg == 0
                #self.tabelrezultate.setItem(i, 8, QtWidgets.QTableWidgetItem(str(format(dg, '.1f')) + '°'))
                elif dg > 0:
                    dg = dg
                    self.tabelrezultate.setItem(i, 8, QtWidgets.QTableWidgetItem(str(format(dg, '.1f')) + '°'))
            elif i == nrrows-1:
                dg == 0
                self.tabelrezultate.setItem(i, 8, QtWidgets.QTableWidgetItem(str(format(dg, '.1f')) + '°'))

            if dg > 360:
                dg = dg-360
                self.tabelrezultate.setItem(i, 8, QtWidgets.QTableWidgetItem(str(format(dg, '.1f')) + '°'))
            if dg < 0:
                dg = dg + 360
                self.tabelrezultate.setItem(i, 8, QtWidgets.QTableWidgetItem(str(format(dg, '.1f')) + '°'))

            #calculdrummagnetic
            dm = self.tabelvalori.item(i, 9)
            dm = float(dm.text())

            if i < nrrows-1:
                if dm == 0:
                    dm = da - d2022
                    self.tabelrezultate.setItem(i, 10, QtWidgets.QTableWidgetItem(str(format(dm, '.1f')) + '°'))
            #elif dm == 0 and da == 0:
                #dm == 0
                #self.tabelrezultate.setItem(i, 10, QtWidgets.QTableWidgetItem(str(format(dm, '.1f')) + '°'))
                elif dm > 0:
                    dm = dm
                    self.tabelrezultate.setItem(i, 10, QtWidgets.QTableWidgetItem(str(format(dm, '.1f')) + '°'))
            elif i == nrrows-1:
                dm == 0
                self.tabelrezultate.setItem(i, 10, QtWidgets.QTableWidgetItem(str(format(dm, '.1f')) + '°'))

            if dm > 360:
                dm = dm-360
                self.tabelrezultate.setItem(i, 10, QtWidgets.QTableWidgetItem(str(format(dm, '.1f')) + '°'))
            if dm < 0:
                dm = dm+360
                self.tabelrezultate.setItem(i, 10, QtWidgets.QTableWidgetItem(str(format(dm, '.1f')) + '°'))


            #calculdeviatiemagnetica
            valoridm = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]
            valoricorespdm = [2.3, 2.3, 1.3, 1, 0.5, 0, -0.7, -1.5, -2, -2.7, -3.3, -3.7, -4, -4.3, -4, -3.7, -3.3, -2.5, -1.7, -1.7, -0.7, 0.3, 1.3, 2.7, 3.5, 4, 4.3, 4.5, 4.5, 4.3, 4, 3.7, 3.5, 3, 2.7, 2.5, 2.3 ]

            if i < nrrows-1:
                if dm in valoridm:
                    index = valoridm.index(dm)
                    deltamicc = valoricorespdm[index]
                    self.tabelrezultate.setItem(i, 11, QtWidgets.QTableWidgetItem(str(deltamicc)+'°'))
                else:
                    y_interp = interp1d(valoridm, valoricorespdm)
                    deltamicc = y_interp(dm)
                    self.tabelrezultate.setItem(i, 11, QtWidgets.QTableWidgetItem(str(format(deltamicc, '.1f'))+'°'))
            elif i == nrrows-1:
                deltamicc == 0
                self.tabelrezultate.setItem(i, 11, QtWidgets.QTableWidgetItem(str(deltamicc) + '°'))

            #calculcorectiecompas
            if i == nrrows-1:
                deltamarec = 0
                self.tabelrezultate.setItem(i, 12, QtWidgets.QTableWidgetItem(str(format(deltamarec, '.1f')) + '°'))
            elif i < nrrows-1:
                deltamarec = deltamicc + d2022
                self.tabelrezultate.setItem(i, 12, QtWidgets.QTableWidgetItem(str(format(deltamarec, '.1f'))+'°'))

            #calculdrumcompas
            dc = self.tabelvalori.item(i, 8)
            dc = float(dc.text())

            if i < nrrows-1:
                if dc == 0:
                    dc = da + deltamarec
                    self.tabelrezultate.setItem(i, 9, QtWidgets.QTableWidgetItem(str(format(dc, '.1f'))+'°'))
            #elif dc == 0 and da == 0:
                #dc == 0
                #self.tabelrezultate.setItem(i, 9, QtWidgets.QTableWidgetItem(str(format(dc, '.1f')) + '°'))
                elif dc > 0:
                    dc = dc
                    self.tabelrezultate.setItem(i, 9, QtWidgets.QTableWidgetItem(str(format(dc, '.1f')) + '°'))
            elif i == nrrows-1:
                dc = 0
                self.tabelrezultate.setItem(i, 9, QtWidgets.QTableWidgetItem(str(format(dc, '.1f')) + '°'))
            if dc > 360:
                dc = dc-360
                self.tabelrezultate.setItem(i, 9, QtWidgets.QTableWidgetItem(str(format(dc, '.1f')) + '°'))
            if dc < 0:
                dc = dc+360
                self.tabelrezultate.setItem(i, 9, QtWidgets.QTableWidgetItem(str(format(dc, '.1f')) + '°'))

        #plotaregrafic
        self.graphWidget.plot(x = phis, y = lambdas, pen ='r', width=8, style=QtCore.Qt.DashLine ,symbol = 'x', symbolBrush=0.2, symbolSize = 15)

class Exemplu(QDialog):
    def __init__(self):
        super(Exemplu, self).__init__()
        loadUi("exemplu.ui", self)
        self.exemplubutton.clicked.connect(self.gotoexemplu)
        self.homebutton.clicked.connect(self.gotohome)
        self.ajutorbutton.clicked.connect(self.gotoajutor)
        self.desprebutton.clicked.connect(self.gotodespre)

        #fundal
        fundal = QPixmap('fundal aplicatie.jpg')
        self.fundal.setPixmap(fundal)

        #pozagrafic
        pozagrafic = QPixmap('pozagrafic.png')
        self.pozagrafic.setPixmap(pozagrafic)

        #formatarecoloanetabele
        self.tabelvalori.setColumnWidth(0,150)
        self.tabelvalori.setColumnWidth(1, 150)
        self.tabelvalori.setColumnWidth(2, 100)
        self.tabelrezultate.setColumnWidth(0, 150)
        self.tabelrezultate.setColumnWidth(1, 150)
        self.tabelrezultate.setColumnWidth(2, 100)

#functii
    def gotodespre(self):
        widget.setCurrentWidget(despre)

    def gotoajutor(self):
        widget.setCurrentWidget(ajutor)

    def gotohome(self):
        widget.setCurrentWidget(first)

    def gotoexemplu(self):
        widget.setCurrentWidget(exemplu)

class Ajutor(QDialog):
    def __init__(self):
        super(Ajutor, self).__init__()
        loadUi("ajutor.ui", self)
        self.exemplubutton.clicked.connect(self.gotoexemplu)
        self.homebutton.clicked.connect(self.gotohome)
        self.ajutorbutton.clicked.connect(self.gotoajutor)
        self.desprebutton.clicked.connect(self.gotodespre)

        # fundal
        fundal = QPixmap('fundal aplicatie.jpg')
        self.fundal.setPixmap(fundal)

#functii
    def gotodespre(self):
        widget.setCurrentWidget(despre)

    def gotoajutor(self):
        widget.setCurrentWidget(ajutor)

    def gotohome(self):
        widget.setCurrentWidget(first)

    def gotoexemplu(self):
        widget.setCurrentWidget(exemplu)

class Despre(QDialog):
    def __init__(self):
        super(Despre, self).__init__()
        loadUi("despre.ui", self)
        self.exemplubutton_4.clicked.connect(self.gotoexemplu)
        self.homebutton_4.clicked.connect(self.gotohome)
        self.ajutorbutton_4.clicked.connect(self.gotoajutor)
        self.desprebutton_4.clicked.connect(self.gotodespre)

        # fundal
        fundal = QPixmap('fundal aplicatie.jpg')
        self.fundal.setPixmap(fundal)

#functii
    def gotodespre(self):
        widget.setCurrentWidget(despre)

    def gotoajutor(self):
        widget.setCurrentWidget(ajutor)

    def gotohome(self):
        widget.setCurrentWidget(first)

    def gotoexemplu(self):
        widget.setCurrentWidget(exemplu)



# main
app = QApplication(sys.argv)
first = MainWindow()
exemplu = Exemplu()
despre = Despre()
ajutor = Ajutor()
widget = QtWidgets.QStackedWidget()
widget.addWidget(first)
widget.addWidget(exemplu)
widget.addWidget(despre)
widget.addWidget(ajutor)
widget.setFixedHeight(900)
widget.setFixedWidth(1400)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Exiting')
