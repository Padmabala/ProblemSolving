class Solution:
    def deepCopy(self,l):
        if(type(l)==list):
            ret=[]
            for i in l:
                ret.append(self.deepCopy(i))
        else:
            if(type(l)!=list):
                ret=l
        return ret
    def floodFill(self, image, sr, sc, newColor):
        hash={}
        que=[]
        que.append([sr,sc])
        rows=len(image)
        cols=len(image[0])
        mImage=self.deepCopy(image)
        hash[sr + sc] = []
        # mImage=[[].append(image[i]) for i in range(len(image))]
        while(len(que)>0):
            sr=que[0][0]
            sc=que[0][1]
            parent=image[sr][sc]
            mImage[sr][sc]=newColor

            prev=sr-1
            if ((prev + sc) not in hash):
                hash[prev+sc]=[]
            if([prev,sc] not in hash[prev+sc]):
                if(prev>=0 and [prev, sc] not in que):
                    if(image[prev][sc]==parent):
                        que.append([prev, sc])
                        mImage[prev][sc]=newColor
                        # hash[prev + sc].append([prev,sc])
            next=sr+1
            if ((next + sc) not in hash):
                hash[next+sc]=[]
            if([next,sc] not in hash[next+sc]):
                if(next<rows and [next,sc] not in que):
                    if(image[next][sc]==parent):
                        que.append([next,sc])
                        mImage[next][sc]=newColor
                        # hash[next + sc].append([next, sc])
            prev=sc-1
            if ((sr+prev) not in hash):
                hash[sr+prev]=[]
            if([sr,prev] not in hash[sr+prev]):
                if(prev>=0 and [sr,prev] not in que):
                    if(image[sr][prev]==parent):
                        que.append([sr,prev])
                        mImage[sr][prev]=newColor
                        # hash[sr+prev].append([sr,prev])
            next=sc+1
            if ((sr+next) not in hash):
                hash[sr+next]=[]
            if([sr,next] not in hash[sr+next]):
                if(next<cols and [sr,next] not in que):
                    if(image[sr][next]==parent):
                        que.append([sr,next])
                        mImage[sr][next]=newColor
                        # hash[sr + prev].append([sr, next])
            hash[sr+sc].append([sr,sc])
            que.pop(0)
        return mImage
s=Solution()
print(s.floodFill([[0,0,0],[0,0,0]],0,0,2))




