from bs4 import BeautifulSoup
from urllib.request import urlopen as uop
import pandas as pd 
class report:
    def __init__(self,sno,state,csin,csfn,cured,death):
        self.sno=sno
        self.state=state
        self.csin=csin
        self.csfn=csfn
        self.cured=cured
        self.death=death
    def __repr__(self):
        return '{},{},{},{},{},{}'.format(self.sno,self.state,self.csin,self.csfn,self.cured,self.death)
    def search(self,st):
        for i in self.state:
            if st.lower()==self.state.lower():
                print(f'State/Union: {self.state}\nTotal Confirmed Cases(Indian): {self.csin}\nTotal Confirmed Cases(Foreigner): {self.csfn}\nCured/Discharged/Migrated: {self.cured}\nDeath: {self.death}')
                return 1
    
record=[]
data=[]
url='https://www.mohfw.gov.in'
wpage=uop(url)
content=wpage.read()
soup=BeautifulSoup(content,'lxml')
select=soup.findAll('div',{'id':'cases'})
for i in range(len(select)):
    select1=select[i].find('tbody').findAll('tr')

for j in range(len(select1)):
    data.append(select1[j].findAll('td'))

for k in range(len(data)-1):
    for l in range(0,6):
        if l==0:
            print(f'\nSl.No.:  {data[k][l].text}')
            sno=(data[k][l].text)
        elif l==1:
            print(f'State/Union:  {data[k][l].text}')
            state=(data[k][l].text)
        elif l==2:
            print(f'Total Confirmed Cases(Indian National):  {data[k][l].text}')
            csin=(data[k][l].text)
        elif l==3:
            print(f'Total Confirmed Cases(Foreign National):  {data[k][l].text}')
            csfn=(data[k][l].text)
        elif l==4:
            print(f'Cured/Discharged/Migrated:  {data[k][l].text}')
            cured=(data[k][l].text)
        else:
            print(f'Death:  {data[k][l].text}')
            death=(data[k][l].text)
    print('\n')
    record.append(report(sno=sno,state=state,csin=csin,csfn=csfn,cured=cured,death=death))

for k in range(len(data))[-1::]:
    for l in range(0,5):
        if l==0:
            print("\nTotal Number of CASES in India:\n")
        elif l==1:
            print(f'Total Confirmed Cases(Indian National):  {data[k][l].text}')
        elif l==2:
            print(f'Total Confirmed Cases(Foreign National):  {data[k][l].text[1:-1:]}')
        elif l==3:
            print(f'Cured/Discharged/Migrated:  {data[k][l].text[1:-1:]}')
        else:
            print(f'Death:  {data[k][l].text[1::]}')
 
SL=[i.sno for i in record]
State=[i.state for i in record]
Csin=[i.csin for i in record]
Csfn=[i.csfn for i in record]
Cured=[i.cured for i in record]
Death=[i.death for i in record]
Final={'Sl.No.':SL,'STATE':State,'TOTAL CONFIRMED CASES(INDIAN)':Csin,'TOTAL CONFIRMED CASES(FOREIGNER)':Csfn,'CURED/DISCHARGED/MIGRATED':Cured,'DEATH':Death}
df=pd.DataFrame(Final)
try:
    df.to_csv('Corona_Report.csv',index=False)
    print("\n\t.csv FILE CREATED.")
except:
    print("\n\t.csv FILE COULDN'T BE CREATED.")

a=input('\nDo you want to search by State[y/n]:')
while a=='y':
    f=0
    s=input("\nEnter the State:  ")
    k=[i.search(s) for i in record]
    for i in k:
        if i==1:
            f=1
    if f==0:
        print("\n\tSTATE NOT FOUND.")
    a=input('\nContinue Search[y/n]: ')