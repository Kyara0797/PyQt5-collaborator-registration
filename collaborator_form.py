import pandas as pd
import sys
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView,QLabel
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont 

df=pd.DataFrame(columns=["Name", "LastName","Profession", "Salary","Net salary"])

def create_app():
    app= QApplication(sys.argv)
    windows = QWidget()
    windows.setWindowTitle("Collaborator Registration")
    windows.resize(800,600)

    layout_principal=QVBoxLayout()
    layout_principal.addSpacing(15)
    
    titulo = QLabel("Collaborator Registration System")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setFont(QFont("Arial", 18, QFont.Bold))
    layout_principal.addWidget(titulo)

    layout_principal.addSpacing(15)

    layout_formulario=QHBoxLayout()
    
    name_input=QLineEdit()
    name_input.setFixedHeight(40) 
    name_input.setPlaceholderText("Name")
    layout_formulario.addWidget(name_input)
    
    last_name_input=QLineEdit()
    last_name_input.setFixedHeight(40) 
    last_name_input.setPlaceholderText("Last Name")
    layout_formulario.addWidget(last_name_input)
    
    profession_input=QLineEdit()
    profession_input.setFixedHeight(40) 
    profession_input.setPlaceholderText("Profession")
    layout_formulario.addWidget(profession_input)
    
    salary_input=QLineEdit()
    salary_input.setFixedHeight(40) 
    salary_input.setPlaceholderText("Salary")
    layout_formulario.addWidget(salary_input)
    
    layout_principal.addLayout(layout_formulario)
    
    layout_buttons=QHBoxLayout()
    
    add_button=QPushButton("Add Collaborator")
    add_button.setFixedHeight(40) 
    layout_buttons.addWidget(add_button)
   
    export_button=QPushButton("Export Excel")
    export_button.setFixedHeight(40) 
    layout_buttons.addWidget(export_button)
    
    layout_principal.addLayout(layout_buttons)

    tabla=QTableWidget()
    tabla.setColumnCount(5)
    tabla.setHorizontalHeaderLabels(
        ["Name","Last Name","Profession","Salary","Net salary"]
    )
    tabla.horizontalHeader().setStretchLastSection(True)
    tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    layout_principal.addWidget(tabla)
   
    
    
    windows.setLayout(layout_principal)
    windows.show()


    def add_data():
        name=name_input.text()
        last_name=last_name_input.text()
        profession=profession_input.text()

        salary=float(salary_input.text())
        
        if salary>0 and salary<=1000:
            net_salary=salary*0.8
        elif salary>1000 and salary<=4000:
            net_salary=salary*0.75
        else:
            net_salary=salary*0.65
        
        nueva_fila={
            "Name":name,
            "Last Name":last_name,
            "Profession":profession, 
            "Salary": salary, 
            "Net Salary": net_salary
        }
        
        global df
        df.loc[len(df)] = nueva_fila
        
        fila = tabla.rowCount()
        tabla.insertRow(fila)
        tabla.setItem(fila, 0, QTableWidgetItem(name))
        tabla.setItem(fila, 1, QTableWidgetItem(last_name))
        tabla.setItem(fila, 2, QTableWidgetItem(profession))
        tabla.setItem(fila, 3, QTableWidgetItem(f"{salary:.2f}"))
        tabla.setItem(fila, 4, QTableWidgetItem(f"{net_salary:.2f}"))
        
        tabla.resizeRowsToContents()
        
        name_input.clear()
        last_name_input.clear()
        profession_input.clear()
        salary_input.clear()

    def export_excel():
        if os.path.exists('data_collaborators.xlsx'):
            os.remove('data_collaborators.xlsx')
        
        df.to_excel('data_collaborators.xlsx', index=False, engine='openpyxl')
    
    
    export_button.clicked.connect(export_excel)
    add_button.clicked.connect(add_data)


    windows.show()
    sys.exit(app.exec_())

create_app()