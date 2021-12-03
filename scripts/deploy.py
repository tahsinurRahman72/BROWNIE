import csv
from brownie import accounts, SetIndividual

rows=[]

def sendIndividualData(i):
     return rows[i]

def prepData():
     file = open("F:\\RESEARCH\\inc1.csv")
     _csvReads = csv.reader(file)
     header = next(_csvReads)

     for row in _csvReads:
          rows.append(row)
     file.close()
     
def deploy_setIndividual():
     # prepData()
     account = accounts[0]
     genesisCommit = SetIndividual.deploy({"from": account})
     print(genesisCommit)
     # for i in range(1,len(rows)):
     #      val=sendIndividualData(i)
     #      setIndiv = genesisCommit.commitIndividual(val[0], round(float(val[1])), 
     #                                                round(float(val[2])), round(float(val[3])), 
     #                                                round(float(val[4])), round(float(val[5])), 
     #                                                round(float(val[6])), {"from": account})
          
     setIndiv = genesisCommit.commitIndividual(1, 257436, 1567216, 1309780, 1196430, 1824709, 0, {"from": account})
     setIndiv.wait(1)
     print(setIndiv)

     countCheck = genesisCommit.retrieve()
     print(countCheck)

def main():
    deploy_setIndividual()

