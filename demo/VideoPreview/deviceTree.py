from qtpy import QtWidgets

class DeviceTree(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(DeviceTree, self).__init__(parent)
        self.setHeaderLabels(['设备树'])  # 设置列标题

    def add_device(self, name):
        # 创建一个 QTreeWidgetItem 对象
        item = QtWidgets.QTreeWidgetItem(self)
        item.setText(0, name)  # 设备名称


