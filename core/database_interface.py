import dll_connect
from dll_connect import _COMPONENT, _PROJECT, _PRODUCT, arraySize
from ctypes import *

import sqlite3

class __updateData():

    def updateCount(self, table,  id_, count):
        dbConnect = sqlite3.connect('../db/RIKOR.db')
        cursor = dbConnect.cursor()

        cursor.execute(f'UPDATE {table} SET COUNT=? WHERE ID=?', (count, id_))

        dbConnect.commit()
        dbConnect.close()

class getData():

    loadedData = dict()

    dataStructs = {
        'components':       (_COMPONENT * arraySize)(),
        'projects':         (_PROJECT * arraySize)(),
        'products':         (_PRODUCT * arraySize)()}

    def __getComponent(*argv):
        returnArgs = [
            c_uint(argv[0]),
            argv[1].encode(),
            argv[2].encode(),
            c_uint(argv[3])]

        return dll_connect.GET_COMPONENT(*returnArgs)

    def __getProject(*argv):
        returnArgs = [
            c_uint(argv[0]),
            argv[1].encode(),
            getData.dataStructs['components'][argv[2]-1],
            getData.dataStructs['components'][argv[3]-1],
            getData.dataStructs['components'][argv[4]-1],
            c_uint(argv[5]),
            getData.dataStructs['components'][argv[6]-1],
            c_float(argv[7])]

        return dll_connect.GET_PROJECT(*returnArgs)

    def __getProduct(*argv):
        returnArgs = [
            c_uint(argv[0]),
            getData.dataStructs['projects'][argv[1]-1],
            c_uint(argv[2])]

        return dll_connect.GET_PRODUCT(*returnArgs)

    @classmethod
    def getData(cls):

        dbConnect = sqlite3.connect('../db/RIKOR.db')
        cursor = dbConnect.cursor()

        for table in ['COMPONENTS', 'PROJECTS', 'PRODUCTS']:
            cursor.execute(f'SELECT * FROM {table}')
            cls.loadedData[table.lower()] = cursor.fetchall()

        getFunctions = {
            'components':   cls.__getComponent,
            'projects':     cls.__getProject,
            'products':     cls.__getProduct}

        for table in cls.loadedData.keys():
            for i, row in zip(
            range(len(cls.loadedData[table])),
            cls.loadedData[table]):
                cls.dataStructs[table][i] = getFunctions[table](*row)

        localData = dll_connect.GET_DATA(
            cls.dataStructs['components'],
            cls.dataStructs['projects'],
            cls.dataStructs['products'])

        dbConnect.close()

        return localData

    def getLastId(self, ArrayName):
        lastId = 0

        Arrays = {
            'COMPONENTS':   self.DATA.COMPONENTS,
            'PROJECTS':     self.DATA.PROJECTS,
            'PRODUCTS':     self.DATA.PRODUCTS}

        Array256 = Arrays[ArrayName]

        for i in range(arraySize):
            if Array256[i].ID == 0:
                break
            lastId += 1

        return lastId

    def getNewData(self, project, count):
        idLst = [
            project.PROCESSOR.ID,
            project.VIDEOCARD.ID,
            project.RAM.ID,
            project.STORAGE_DEVICE.ID]

        countLst = [
            project.PROCESSOR.COUNT - count,
            project.VIDEOCARD.COUNT - count,
            project.RAM.COUNT - (count * project.RAM_COUNT),
            project.STORAGE_DEVICE.COUNT - count]

        return [idLst, countLst]

class addData(__updateData, getData):

    def addComponent(self, *argv):
        self.__insertData('COMPONENTS', *argv)

    def addProject(self, *argv):
        self.__insertData('PROJECTS', *argv)

    def addProduct(self, *argv):
        argv = list(argv)
        newData = self.getNewData(argv[1], argv[2])

        for id_i, count_i in zip(newData[0], newData[1]):
            self.__updateData('COMPONENTS', id_i, count_i)

        argv[1] = argv[1].ID
        self.__insertData('PRODUCTS', *argv)

    def __insertData(sefl, *argv):
        dbConnect = sqlite3.connect('../db/RIKOR.db')
        cursor = dbConnect.cursor()

        sql = f'INSERT INTO {argv[0]} VALUES({str("?,"*(len(argv)-1))[:-1]})'
        cursor.execute(sql, tuple(argv[1:]))

        dbConnect.commit()
        dbConnect.close()

    def __updateData(self, table,  id_, count):
        super().updateCount(table,  id_, count)

    def getNewData(self, project, count):
        return super().getNewData(project, count)

    def __init__(self):
        self.COMPONENT = self.addComponent
        self.PROJECT = self.addProject
        self.PRODUCT = self.addProduct

class deleteData():

    def deleteProduct(self, id_):
        dbConnect = sqlite3.connect('../db/RIKOR.db')
        cursor = dbConnect.cursor()

        cursor.execute("DELETE FROM PRODUCTS WHERE ID=?", (id_,))

        dbConnect.commit()
        dbConnect.close()

class connect(getData, __updateData, deleteData):

    def __init__(self):
        self.DATA = connect.getData()
        self.ADD = addData()
        self.UPDATE = self.updateCount
        self.DELETE = self.deleteProduct

    @classmethod
    def getData(cls):
        return super().getData()

    def updateCount(self, table, id_, count):
        super().updateCount(table, id_, count)

    def deleteProduct(self, id_):
        super().deleteProduct(id_)