class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        l=[]
        i=0
        while (i!=len(A[0])):
            x = [item[i] for item in A]
            if(x!=[]):
                l.append(x)
            i+=1
        return(l)
