import pandas as pd
class santhosh:
    def won_party(self,file):
        self.file=pd.read_csv(file)
        state=[]
        for i in range(len(self.file['state'])):
            st=self.file['state'][i]
            if st not in state:
                    party=[]
                    votes=[]
                    for j in range(i,len(self.file['party'])):
                        if st!=self.file['state'][j]:break
                        if self.file['won'][j]==True:
                            party.append(self.file['party'][j])
                            votes.append(self.file['votes'][j])
                    if party and votes:
                        rev=[]
                        vot=[]
                        for ss in range(len(party)):
                            p=party[ss]
                            vt=votes[ss]
                            if p not in rev:
                                for vv in range(ss+1,len(party)):
                                    if p== party[vv]:
                                        vt+=votes[vv]
                            rev.append(p)
                            vot.append(vt)
                        ind=vot.index(max(vot))
                        print("State:{} Winning party:{}".format(st,rev[ind]))
                        state.append(st)

s=santhosh()
s.won_party('C:/Users/vjrs1/PycharmProjects/mysql/governors_county_candidate.csv')
