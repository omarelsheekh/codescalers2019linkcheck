class AsciiTable:
    def __init__(self):
        self.table=["empty row"]
    def addRow(self,r):
        self.table.append(r)
    def setTitles(self,r):
        self.table[0]=r
    def getTitles(self):
        return self.table[0]
    def getRow(self,id):
        for i in self.table:
            if i[0]==id:
                return i
        return None
    def maxWidth(self):
        colNum=len(self.table[0])
        colWidth=[]
        while colNum>0:
            colWidth.append(0)
            colNum-=1

        for r in self.table:
            colNum = len(colWidth) - 1
            while colNum>=0:
                if len(str(r[colNum])) > colWidth[colNum]:
                    colWidth[colNum]=len(r[colNum])
                colNum-=1
        return colWidth
    def printDashLine(self):
        line = "+"
        mWidth = self.maxWidth()
        for i in mWidth:
            for j in range(0,i):
                line += "-"
            line+="+"
        return line
    def printTable(self):
        table=self.printDashLine()+"\n"
        mWidth=self.maxWidth()
        for r in self.table:
            cNum=0
            for c in r:
                c=str(c)
                table+="|"+c
                for s in range(0,mWidth[cNum]-len(c)):
                    table+=" "
                cNum+=1
            table+="|\n"+self.printDashLine()+"\n"
        return table

if __name__ == '__main__':
    ta=AsciiTable()
    ta.setTitles(["id","name","Date"])
    ta.addRow(["1", "omar", "15-9-1998"])
    ta.addRow(["5", "ahmed", "1-1-1990"])
    print(ta.maxWidth())
    print(ta.printTable())


