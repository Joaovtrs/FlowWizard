from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator, QFont
from PySide6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListView,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from system import system


def configure_button(btn):
    btn.setMinimumSize(150, 30)
    btn.setMaximumSize(150, 30)
    btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class ViewNodes(QFrame):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.setFrameShape(QFrame.Panel)

        # =====================================================================
        # Main grid

        self.grid = QVBoxLayout(self)

        self.lbl_title = QLabel('Conexões', self)
        self.lbl_title.setAlignment(Qt.AlignHCenter)
        self.lbl_title.setFont(QFont('Times', 20))

        self.separator_title = QFrame(self)
        self.separator_title.setFrameShape(QFrame.HLine)

        # =====================================================================
        # Table grid

        self.table_widget = QWidget(self)
        self.grid_2 = QHBoxLayout(self.table_widget)
        self.grid_2.setContentsMargins(0, 0, 0, 0)

        self.nodes_table = NodesTable(self.func_update, self)

        self.options_widget = OptionsWidget(self.func_update, self)
        self.nodes_table.options_widget = self.options_widget

        self.grid_2.addWidget(self.nodes_table)
        self.grid_2.addWidget(self.options_widget)

        # =====================================================================

        self.grid.addWidget(self.lbl_title)
        self.grid.addWidget(self.separator_title)
        self.grid.addWidget(self.table_widget)

    def update_(self):
        self.nodes_table.update_()
        self.options_widget.update_()


class NodesTable(QTableWidget):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update
        self.options_widget = None

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalHeader().setVisible(False)

        self.cellDoubleClicked.connect(self.func_cell_clicked)

        self.update_()

    def update_(self):
        self.clear()

        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(
            [
                'Nome',
                'Cota (m)',
                'Pressão (m.c.a.)',
                'Trechos Conectados',
            ]
        )
        self.setColumnWidth(0, 250)
        self.setColumnWidth(1, 250)
        self.setColumnWidth(2, 250)
        self.setColumnWidth(3, 250)

        self.setRowCount(len(system.circuit.nodes))
        for i, node in enumerate(system.circuit.nodes):
            self.add_item(i, 0, str(node.name))
            self.add_item(i, 1, str(node.elevation))
            self.add_item(i, 2, str(node.pressure))
            self.add_item(i, 3, '')

    def add_item(self, col, line, item):
        item = QTableWidgetItem(item)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setItem(col, line, item)

    def func_cell_clicked(self, row, column):
        self.options_widget.node_options = system.circuit.nodes[row]
        self.func_update()


class OptionsWidget(QFrame):
    def __init__(self, func_update, parent=None):
        super().__init__(parent)

        self.func_update = func_update

        self.node_options = None

        self.setFrameShape(QFrame.Panel)
        self.setMinimumWidth(500)
        self.setMaximumWidth(500)

        # =====================================================================
        # Main grid

        self.grid = QVBoxLayout(self)

        self.lbl_title = QLabel('Configurações', self)
        self.lbl_title.setAlignment(Qt.AlignLeft)
        self.lbl_title.setFont(QFont('Times', 15))

        self.spacer = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        # =====================================================================
        # Info grid

        self.widget_info = QWidget(self)
        self.grid_info = QGridLayout(self.widget_info)
        self.grid_info.setVerticalSpacing(20)

        self.lbl_name = QLabel('Nome:', self.widget_info)
        self.txt_name = QLabel('', self.widget_info)

        self.lbl_elevation = QLabel('Cota (m):', self.widget_info)
        self.txt_elevation = QLineEdit(self.widget_info)
        self.txt_elevation.setValidator(QDoubleValidator(self))

        self.lbl_pressure = QLabel('Pressão (m.c.a.):', self.widget_info)
        self.txt_pressure = QLabel('', self.widget_info)

        self.lbl_pipes = QLabel('Trechos conectados:', self.widget_info)
        self.txt_pipes = QListView(self.widget_info)

        self.box_is_consumption = QCheckBox(self.widget_info)
        self.lbl_is_consumption = QLabel('Ponto de consumo', self.widget_info)

        self.box_is_supply = QCheckBox(self.widget_info)
        self.lbl_is_supply = QLabel('Ponto de fornecimento', self.widget_info)

        self.grid_info.addWidget(self.lbl_name, 0, 0)
        self.grid_info.addWidget(self.txt_name, 0, 1)
        self.grid_info.addWidget(self.lbl_elevation, 1, 0)
        self.grid_info.addWidget(self.txt_elevation, 1, 1)
        self.grid_info.addWidget(self.lbl_pressure, 2, 0)
        self.grid_info.addWidget(self.txt_pressure, 2, 1)
        self.grid_info.addWidget(self.lbl_pipes, 3, 0)
        self.grid_info.addWidget(self.txt_pipes, 3, 1)
        self.grid_info.addWidget(self.box_is_consumption, 4, 0)
        self.grid_info.addWidget(self.lbl_is_consumption, 4, 1)
        self.grid_info.addWidget(self.box_is_supply, 5, 0)
        self.grid_info.addWidget(self.lbl_is_supply, 5, 1)

        # =====================================================================
        # Buttons grid

        self.widget_btns = QWidget(self)
        self.widget_btns.setMaximumHeight(50)
        self.grid_btns = QHBoxLayout(self.widget_btns)

        self.btn_add = QPushButton('Adicionar conexão', self.widget_btns)
        configure_button(self.btn_add)

        self.btn_remove = QPushButton('Excluir conexão', self.widget_btns)
        configure_button(self.btn_remove)

        self.btn_save = QPushButton('Salvar Alterações', self.widget_btns)
        configure_button(self.btn_save)

        self.grid_btns.addWidget(self.btn_add)
        self.grid_btns.addWidget(self.btn_remove)
        self.grid_btns.addWidget(self.btn_save)

        # =====================================================================

        self.grid.addWidget(self.lbl_title)
        self.grid.addWidget(self.widget_info)
        self.grid.addItem(self.spacer)
        self.grid.addWidget(self.widget_btns)

        self.btn_add.clicked.connect(self.add_func)
        self.btn_save.clicked.connect(self.save_func)

    def update_(self):
        if self.node_options is None:
            self.txt_name.setText('')
            self.txt_elevation.setText('')
            self.txt_pressure.setText('')
            self.box_is_consumption.setChecked(False)
            self.box_is_supply.setChecked(False)
        else:
            self.txt_name.setText(str(self.node_options.name))
            self.txt_elevation.setText(
                f'{self.node_options.elevation}'.replace('.', ',')
            )
            self.txt_pressure.setText(
                f'{self.node_options.pressure:.2f}'.replace('.', ',')
            )
            self.box_is_consumption.setChecked(
                self.node_options.is_consumption
            )
            self.box_is_supply.setChecked(self.node_options.is_supply)

    def pop_up(self, texto):
        pop_up = QMessageBox(self)
        pop_up.setWindowTitle('Aviso')
        pop_up.setText(texto)
        pop_up.setIcon(QMessageBox.Question)
        pop_up.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        pop_up.setButtonText(QMessageBox.No, 'Não')
        pop_up.setButtonText(QMessageBox.Yes, 'Sim')
        pop_up.setDefaultButton(QMessageBox.No)

        return pop_up.exec()

    def add_func(self):
        system.circuit.add_node()
        self.func_update()

    def save_func(self):
        if self.node_options is not None:
            resp = self.pop_up(
                f'Deseja salvar as alterações da conexão {self.node_options.name}'
            )

            if resp == QMessageBox.Yes:
                pass
