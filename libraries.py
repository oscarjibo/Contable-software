# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 22:00:54 2022

@author: oscar
"""

import tkinter as tk
from pandastable import Table, TableModel
import numpy as np
import numpy_financial as npf
import pathlib
import os
from PyQt5 import QtCore
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QTableView)
from PyQt5.QtCore import (QAbstractTableModel, Qt)
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QLCDNumber
from PyQt5.uic import loadUi
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from datetime import date
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, \
                            QPushButton, QItemDelegate, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5 import QtGui


import subprocess
import os.path
import inspect
import pathlib