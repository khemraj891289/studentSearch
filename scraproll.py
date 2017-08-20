import requests
from BeautifulSoup import BeautifulSoup
dp = ['BSBE','AE','CHY','CHE','CE','CSE','ECO','EE','ES','IME','MDes','ME','MSE','MTH','NT','PHY']
f= open("roll.json","w+")
for i in dp:
    y = 27
    tq = 0
    while y >= 27:
        if(tq == 0):
            url = 'http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchStudRoll.jsp?selstudrol=&selstuddep='+i+'&selstudnam='
        else:
            url = 'http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchStudRoll.jsp?recpos='+str(tq)+'&selstudrol=&selstuddep='+i+'&selstudnam='
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html)
        table = soup.find('table', attrs={'cellspacing': 1})
        j = 0
        y = 0
        if not table:
            continue
        for row in table:
            #print row
            if(j%2 == 1 and j > 2):
                p = row.find('a')
                p=p.text
                f.write('%s\n'%p)
                print p
            j = j +1
            y = y + 1
        print j
        tq = tq +12 
        print y, tq
f.close()