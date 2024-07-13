from PyQt5 import QtCore, QtGui, QtWidgets

import sys
sys.path.append('../core')

from dll_connect import arraySize, charset
from database_interface import connect

sys.path.pop()

version = "RIKOR APA 2.8.12"

def listFill(object):
    array = object.data[object.table]

    if object.table == 'готовые изделия':
        count = object.RIKOR.getLastId('PRODUCTS')

        for i in range(count):
            item = array[i].PROJECT.NAME
            if item == None:
                break
            object.listWidget.addItem(item.decode(charset))
    else:
        counts = [
            object.RIKOR.getLastId('COMPONENTS'),
            object.RIKOR.getLastId('PROJECTS')]
        count = max(counts)

        for i in range(count):
            item = array[i].NAME
            if item == None:
                break
            object.listWidget.addItem(item.decode(charset))

def onActiveItem(object):

    selectedItemText = object.listWidget.currentItem().text()
    data = object.data[object.table]

    if object.table == 'готовые изделия':
        productCount = object.RIKOR.getLastId('PRODUCTS')
        for i in range(productCount):
            name = data[i].PROJECT.NAME.decode(charset)
            if name == selectedItemText:
                object.infoLabel.setText(
                    f'имя:\t\t{name}\nколичество:\t{data[i].COUNT}')
                break
    else:
        counts = [
            object.RIKOR.getLastId('COMPONENTS'),
            object.RIKOR.getLastId('PROJECTS')]
        count = max(counts)

        for i in range(count):
            if data[i].NAME.decode(charset) == selectedItemText:
                if str(type(data[i])) == "<class 'dll_connect._COMPONENT'>":
                    types = {
                        'PROCESSOR':        'процессор',
                        'VIDEOCARD':        'видеокарта',
                        'RAM':              'ОЗУ',
                        'STORAGE_DEVICE':   'хранилище'}
                    object.infoLabel.setText((
                        f'имя:\t\t{data[i].NAME.decode(charset)}\n'
                        f'тип:\t\t{types[data[i].TYPE.decode(charset)]}\n'
                        f'количество:\t{data[i].COUNT}'))
                else:
                    object.infoLabel.setText((
                        f'имя:\t\t{data[i].NAME.decode(charset)}\n'
                        f'процессор:\t{data[i].PROCESSOR.NAME.decode(charset)}\n'
                        f'видеокарта:\t{data[i].VIDEOCARD.NAME.decode(charset)}\n'
                        f'ОЗУ:\t\t{data[i].RAM.NAME.decode(charset)} x {data[i].RAM_COUNT}\n'
                        f'хранилище:\t{data[i].STORAGE_DEVICE.NAME.decode(charset)}\n'
                        f'стоимость:\t{data[i].PRICE}'))
                break
def _switchContextMenu(object):
    if object.table == 'готовые изделия':
        object.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        object.listWidget.customContextMenuRequested.connect(object.deleteContextMenu)
    else:
        object.listWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)

def deleteContextMenu(object):
    if object.RIKOR.getLastId('PRODUCTS') > 0:
        menu = QtWidgets.QMenu()
        menu.addAction('Удалить')
        menu.triggered.connect(object.deleteProduct)
        menu.exec_(QtGui.QCursor.pos())

def deleteProduct(object):
    productsCount = object.RIKOR.getLastId('PRODUCTS')

    for i in range(productsCount):
        product = object.RIKOR.DATA.PRODUCTS[i]
        productName = product.PROJECT.NAME.decode(charset)
        selectedProductName = object.listWidget.currentItem().text()

        if selectedProductName == productName:
            id_ = product.ID
            break

    object.RIKOR.DELETE(id_)
    object.reload()

def _changeTable(object):
    object.listWidget.clear()
    object.listFill()
    object.tableLabel.setText(object.table)

    object._switchContextMenu()

def nextTable(object):
    if object.table == 'готовые изделия':
        object.table = object.tables[0]
    else:
        _index = object.tables.index(object.table)
        object.table = object.tables[_index+1]

    object._changeTable()

def backTable(object):
    if object.table == 'комплектующие':
        object.table = object.tables[2]
    else:
        _index = object.tables.index(object.table)
        object.table = object.tables[_index-1]

    object._changeTable()

def reload(object):
        object.RIKOR = connect()
        DATA = object.RIKOR.DATA
        object.data = {
            'комплектующие':            DATA.COMPONENTS,
            'выпускаемая продукция':    DATA.PROJECTS,
            'готовые изделия':          DATA.PRODUCTS}
        object.listWidget.clear()
        object.listFill()

def addComponent(object):
    name = object.nameLine.text()

    try:
        name[0]
    except:
        object.message("Поля заполнены неверно")
    else:
        count = int(object.countLine.text())

        if object.typeBox.isEnabled():
            types = {
                'процессор':    'PROCESSOR',
                'видеокарта':   'VIDEOCARD',
                'ОЗУ':          'RAM',
                'хранилище':    'STORAGE_DEVICE'}

            id_ = object.data.getLastId('COMPONENTS')+1
            type = object.typeBox.currentText()
            type = types[type]

            object.data.ADD.COMPONENT(id_, type, name, count)

        else:
            count += object.count
            object.data.UPDATE('COMPONENTS', object.id_, count)

        object.message("Запись успешно создана")
        object.clearFields()
        object.data = connect()

def changeComponentNameValue(object):
    text = object.nameLine.text()
    componentsCount = object.data.getLastId('COMPONENTS')

    for i in range(componentsCount):
        components = object.data.DATA.COMPONENTS
        componentName = components[i].NAME.decode(charset)

        if componentName == text:
            object.typeBox.setEnabled(False)
            object.id_ = components[i].ID
            object.count = components[i].COUNT
            break

        object.typeBox.setEnabled(True)

def addProject(object):
    name = object.nameLine.text()
    ramCount = object.spinCount.value()
    price = object.priceLine.text()

    try:
        name[0]
        0/int(ramCount)
        0/float(price)
    except:
        object.message("Поля заполнены неверно")
    else:
        projectsCount = object.data.getLastId('PROJECTS')
        for i in range(projectsCount):
            projectName = object.data.DATA.PROJECTS[i].NAME.decode(charset)
            if name == projectName:
                object.message("Проект уже существует")
                break
        else:
            id_ = object.data.getLastId('PROJECTS')+1
            processor = object.processorBox.currentData().ID
            videocard = object.videocardBox.currentData().ID
            ram = object.ramBox.currentData().ID
            ramCount = int(ramCount)
            storage = object.storageBox.currentData().ID
            price = float(price)

            object.data.ADD.PROJECT(
                id_,name,processor,videocard,ram,ramCount,storage,price)

            object.message("Запись успешно создана")
            object.clearFields()
        object.data = connect()

def fillComponentBoxes(object):
    for i in range(object.data.getLastId('COMPONENTS')):
        boxes = {
        'PROCESSOR':            object.processorBox,
        'VIDEOCARD':            object.videocardBox,
        'RAM':                  object.ramBox,
        'STORAGE_DEVICE':       object.storageBox}

        component = object.data.DATA.COMPONENTS[i]
        componentType = component.TYPE.decode(charset)
        componentName = component.NAME.decode(charset)
        boxes[componentType].addItem(componentName, component)

def addProduct(object):
    project = object.projectBox.currentData()
    count = int(object.countLine.text())

    productsCount = object.data.getLastId('PRODUCTS')
    projectName = project.NAME.decode(charset)

    new = True
    transaction = True

    for i in range(productsCount):
        product = object.data.DATA.PRODUCTS[i]
        projectName_i = product.PROJECT.NAME.decode(charset)

        if projectName == projectName_i:
            new = False
            break

    if new:
        id_ = object.data.getLastId('PRODUCTS')+1
        object.data.ADD.PRODUCT(id_, project, count)
        object.message("Запись успешно создана")

    else:
        id_ = product.ID
        count_ = product.COUNT + count
        object.data.UPDATE('PRODUCTS', id_, count_)
        newData = object.data.getNewData(project, count)

        for count_i in newData[1]:
            if count_i <= 0:
                object.message("Недостаточно компонентов")
                transaction = False
                break

        if transaction:
            for id_i, count_i in zip(newData[0], newData[1]):
                object.data.UPDATE('COMPONENTS', id_i, count_i)
            object.message("Запись успешно создана")

    object.clearFields()

    object.data = connect()
    object.fillProjectBox()

def fillProjectBox(object):
    object.projectBox.clear()

    for i in range(object.data.getLastId('PROJECTS')):
        item = object.data.DATA.PROJECTS[i]
        project = item.NAME.decode(charset)
        object.projectBox.addItem(project, item)

def changeSliderValue(object):
    object.countLine.setText(str(object.countSlider.value()+1))

def changeLineValue(object):
    text = object.countLine.text()

    try:
        object.countSlider.setValue(int(text)-1)
    except:
        if len(text) >= 1:
            object.countLine.setText(text[:-1])
        else:
            object.countLine.setText('1')
    else:
        if int(text) > 100:
            object.countLine.setText('100')

def changeLineValueBlock(object):
    try:
        object.countSlider.setValue(int(object.countLine.text())-1)
    except:
        object.countSlider.setValue(0)
    else:
        inputCount = int(object.countLine.text())
        project = object.projectBox.currentData()
        counts = [
            project.PROCESSOR.COUNT,
            project.VIDEOCARD.COUNT,
            round(project.RAM.COUNT / project.RAM_COUNT),
            project.STORAGE_DEVICE.COUNT]

        if inputCount > min(counts):
            object.countSlider.setValue(min(counts)-1)

    object.changeSliderValue()

def changeProjectBoxValue(object):
    object.countSlider.setValue(0)

def message(object, messageType):
    messageWindow = QtWidgets.QMessageBox()
    messageWindow.setWindowTitle(version)
    messageWindow.setText(messageType)

    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap("../images/rikor_ico.ico"),
        QtGui.QIcon.Normal,
        QtGui.QIcon.Off)
    messageWindow.setWindowIcon(icon)

    messageWindow.exec_()