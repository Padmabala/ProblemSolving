class StockSpanner:
    def __init__(self):
        self.stk=[]
        self.spanner=[]
        self.top=-1

    def next(self, price: int) -> int:
        if(len(self.stk)==0):
            self.stk.append([price,1])
            self.top+=1
        else:
            if(price>=self.stk[self.top][0]):
                span=1
                while(self.stk and price>=self.stk[self.top][0]):
                    span += self.stk[self.top][1]
                    self.stk.pop(self.top)
                    self.top-=1
                self.stk.append([price,span])
            else:
                self.stk.append([price,1])
            self.top += 1
        self.spanner.append(self.stk[self.top][1])
    def getSpanner(self):
        return self.spanner

S = StockSpanner()
S.next(31)
S.next(41)
S.next(48)
S.next(59)
S.next(79)
print(S.getSpanner())