import requests
from BeautifulSoup import BeautifulSoup
# fp = open('roll.json')
fp = open('finalr.json')
# f= open("finalr.json","w+")
# for p in fp:
#     p = p.strip()
#     # print p.isdigit()
#     if(p.isdigit()):
#         i = int(p)
#         if(i<=170830 and i>=170001):
#             continue
#         elif(i<=160832 and i>=160001):
#             continue
#         elif(i<= 150845 and i>=150001):
#             continue
#         elif(i<= 14832 and i>=14001):
#             continue
#         elif(i<= 13819 and i>=13001):
#             continue
#         elif(i<= 12837 and i>=12001):
#             continue
#         elif(i<= 11833 and i>=11001):
#             continue
#         elif(i<= 10829 and i>=10001):
#             continue
#         else:
#             f.write('%s\n'%p)
#     else:
#         f.write('%s\n'%p)
# f.close()
f= open("data.json","w+")
f.write('[') 
data = ''
# for i in range(1, 2):
for i in fp:
        i = str(i).strip()
        url = "https://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes.jsp?typ=stud&numtxt="+i+"&sbm=Y"
        response = requests.get(url)
        html = response.content
        data = ''
        soup = BeautifulSoup(html)
        table = soup.find('td', attrs={'class': 'TableContent'})
        j = 0
        data = data + '{'
        if not table:
            continue
        for row in table:
                j = j + 1
                #if(j==2):
                 #       print row.text.strip()
                  #      data = data + row.text.strip()
                if(j==3):
                        #print row.strip()
                        data = data + '"r":"'+row.strip()+'",'
                if(j==8):
                        #print row.text
                        data = data + '"n":"'+row.text.split(':')[1]+'",'
                if(j==10):
                        #print row.text
                        data = data + '"p":"'+row.text.split(':')[1]+'",'
                if(j==12):
                        #print row.text
                        dep = row.text.split(':')[1]
                        #data = data + row.text
                        if(dep=='AEROSPACE ENGG.'):
                              data = data + '"d":"AE",'
                        if(dep=='BIOL.SCI. AND BIO.ENGG.'):
                              data = data + '"d":"BSBE",'
                        if(dep=='CHEMICAL ENGG.'):
                              data = data + '"d":"CHE",'
                        if(dep=='CHEMISTRY'):
                              data = data + '"d":"CHY",'
                        if(dep=='CIVIL ENGG.'):
                              data = data + '"d":"CE",'
                        if(dep=='COMPUTER SCIENCE & ENGG.'):
                              data = data + '"d":"CSE",'
                        if(dep=='ECONOMICS'):
                              data = data + '"d":"ECO",'
                        if(dep=='ELECTRICAL ENGG.'):
                              data = data + '"d":"EE",'
                        if(dep=='MECHANICAL ENGINEERING'):
                              data = data + '"d":"ME",'
                        if(dep=='MATERIALS SCIENCE & ENGG.'):
                              data = data + '"d":"MSE",'
                        if(dep=='MATHEMATICS'):
                              data = data + '"d":"MTH",'
                        if(dep=='PHYSICS'):
                              data = data + '"d":"PHY",'
                        if(dep=='IND. & MANAGEMENT ENGG.'):
                              data = data + '"d":"IME",'
                        if(dep=='MASTER OF DESIGN'):
                              data = data + '"d":"MDes",'
                        if(dep=='EARTH SCIENCES'):
                              data = data + '"d":"ES",'
                        if(dep=='NUC. ENGG.& TECH PROG.'):
                              data = data + '"d":"NT",'
                if(j==14):
                        #print row.text.split(':')[0]
                        data = data + '"h":"'+ row.text.split(':')[1]+'",'
                if(j==16):
                        #print row.text.split('@')[0]
                        data = data + '"e":"'+ row.text.split('@')[0].split(':')[1]+'",'
                if(j==18):
                        #print row.text.split('<')[0]
                        data = data + '"b":"'+ row.text.split('<')[0].split(':')[1]+'",'
                if(j==20):
                        #print row.text.split('C')[0]
                        data = data + '"g":"'+ row.text.split('C')[0].split(':')[1]+'",'
                if(j==22):
                        ad = row.split('<br>')[4]
                        if(ad == 'Not Available'):
                                data = data + '"c":"Not Available",'
                                #print 'State:',ad2[ln-2]
                                data = data + '"s":"Not Available",'
                                #print 'Address:',ad
                                data = data + '"ad":"Not Available"'
                        else:
                                ad2 = ad.split(',')
                                ln = len(ad2)
                                #print 'City:',ad
                                #print data
                                data = data + '"c":"'+ad2[ln-3]+'",'
                                #print 'State:',ad2[ln-2]
                                data = data + '"s":"'+ad2[ln-2]+'"'
                                #print 'Address:',ad
                                #data = data + '"ad":"'+ad+'"'

        print i
        data = data + '},'
        f.write(data) 

data = data + ']'

f.write(data)                   
f.close()
