from asciiTable import AsciiTable
import threading,time,re,requests,os
links=[]
table=AsciiTable()
# echo "# codescalers2019linkcheck" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/omarelsheekh/codescalers2019linkcheck.git
# git push -u origin master
class MyThread(threading.Thread):
    def run(self):
        link=links[len(links)-1]
        try:
            req = requests.head(link)
            linkStatCode = req.status_code
            statSring = ""
            if linkStatCode == 200:
                statSring = "valid link"
            else:
                statSring = "bad request"
            table.addRow([link + " ", linkStatCode, statSring])
        except:
            table.addRow([link +" ",-1,"connection error"])

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if ".html" in fullPath:
                allFiles.append(fullPath)

    return allFiles


if __name__ == '__main__':
    regex = r"href=[\'\"]?([^\'\" >]+)"
    # test_str = ("<!DOCTYPE html>\n"
    #             "<html>\n"
    #             "<body>\n\n"
    #             "<h2>HTML Links</h2>\n"
    #             "<p><a href=\"https://www.w3schools.com/html233/\">Visit our HTML tutorial</a></p>\n"
    #             "<a href=\"https://www.w3schools.com/html/\">Visit our HTML tutorial</a>\n\n"
    #             "</body>\n"
    #             "</html>")
    table.setTitles(["link", "req code", "statue"])
    directory="codescalers.com"
    for d in getListOfFiles(directory):
        fileStr=open(d).read()
        matches = re.finditer(regex, fileStr, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                link=match.group(groupNum)
                if "http" in link or "https" in link:
                    links.append(link)
                    th = MyThread()
                    th.start()


    while len(table.table) != len(links)+1:
        # just wait
        time.sleep(.001)
    print(table.printTable())