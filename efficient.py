import time
import tracemalloc
import sys

align1 = ""
align2 = ""
cost = 0.0
class Solution:
    
    def __init__(self,fileName):
        self.file=fileName
        




    def readFile(self):
        f = open(self.file)
        lines = f.read().splitlines()
        str_idxs=[]
        self.delta =30
        self.alpha={
            "{}_{}".format("A", "A"): 0,
            "{}_{}".format("A","C"):110,
            "{}_{}".format("A", "G"): 48,
            "{}_{}".format("A", "T"): 94,
            "{}_{}".format("C", "C"): 0,
             "{}_{}".format("C","A"):110,
            "{}_{}".format("C", "G"): 118,
            "{}_{}".format("C", "T"): 48,
            "{}_{}".format("G", "G"): 0,
            "{}_{}".format("G", "A"): 48,
            "{}_{}".format("G", "C"): 118,
            "{}_{}".format("G", "T"): 110,
            "{}_{}".format("T", "T"): 0,
            "{}_{}".format("T", "A"): 94,
            "{}_{}".format("T", "C"): 48,
            "{}_{}".format("T", "G"): 110}
        for i,line in enumerate(lines):
            if line.isalpha():
                str_idxs.append(i)

        return [[lines[str_idxs[0]],lines[str_idxs[0]+1:str_idxs[1]]],[lines[str_idxs[1]],lines[str_idxs[1]+1:]]]

    def inputStringGenerator(self,obj):
        baseString = obj[0]
        operations = obj[1]
        debug=[]
        if not operations:
            return baseString,""
        for idx in operations:
            idx = int(idx)
            curr = baseString[:idx+1]+ baseString+ baseString[idx+1:]
            baseString = curr
            debug.append(baseString)
        return baseString,debug

    def matrixGenertaor(self,x,y):
        dp = []
        m=len(x)
        n=len(y)
        for i in range(m + 1):
            dp.append([0] * (n + 1))
        for i in range(m + 1):
            dp[i][0] = self.delta * i
        for i in range(n + 1):
            dp[0][i] = self.delta * i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                    dp[i][j] = min(
                    dp[i][j - 1] + self.delta,
                    dp[i - 1][j] + self.delta,
                    dp[i - 1][j - 1] +self.alpha["{}_{}".format(x[i-1],y[j-1])])
        return dp

    def get_y_mid(self,scoreL, scoreR):
        max_index = 0
        max_score = float('Inf')
        for i, (l, r) in enumerate(zip(scoreL, scoreR[::-1])):
            if sum([l, r]) < max_score:
                max_score = sum([l, r])
                max_index = i
        return max_index

    # gets the last line of the Needleman-Wunsch matrix
    def NWScore(self, seq1, seq2):
        len1 = len(seq1) + 1
        len2 = len(seq2) + 1
        last_line = [0] * (len2)
        current_line = [0] * (len2)

        for j in range(1, len2):
            last_line[j] = last_line[j - 1] + self.delta

        for i in range(1, len1):
            current_line[0] = self.delta + last_line[0]
            for j in range(1, len2):
                current_line[j] = min(last_line[j - 1] + self.alpha["{}_{}".format(seq1[i - 1], seq2[j - 1])],
                                      last_line[j] + self.delta,
                                      current_line[j - 1] + self.delta)

            last_line = current_line
            current_line = [0] * (len2)

        return last_line
    def advancedSolver(self,x,y):
        global align1, align2, cost
        len1 = len(x)
        len2 = len(y)

        if len1 <= 2 or len2 <= 2:
            aligned_seq1, aligned_seq2, cos = self.basicSolver( x, y)
            align1 += aligned_seq1
            align2 += aligned_seq2
            cost += cos
        else:

            xmid = len1 // 2
            scoreL = self.NWScore( x[:xmid], y)
            scoreR = self.NWScore( x[xmid:][::-1], y[::-1])
            ymid = self.get_y_mid(scoreL, scoreR)
            self.advancedSolver( x[:xmid], y[:ymid])
            self.advancedSolver( x[xmid:], y[ymid:])
            # aligned_seq1 = rowLeft + rowRight
            # aligned_seq2 = columnUp + columnDown

        # return aligned_seq1, aligned_seq2, cost


    def basicSolver(self,x,y):
        dp = self.matrixGenertaor(x,y)
        m = len(x)
        n = len(y)
        l= m + n
        i = m
        j = n
        xptr = l
        yptr = l
        xalligned=[""]*(l+1)
        yalligned =[""]*(l+1)
        while (i > 0 and j > 0):
            if (x[i - 1] == y[j - 1]):
                xalligned[xptr] = x[i - 1]
                yalligned[yptr] = y[j - 1]
                xptr -= 1
                yptr -= 1
                i -= 1
                j -= 1
            elif (dp[i - 1][j - 1] + self.alpha["{}_{}".format(x[i-1],y[j-1])]) == dp[i][j]:
                xalligned[xptr] = x[i - 1]
                yalligned[yptr] = y[j - 1]
                xptr -= 1
                yptr -= 1
                i -= 1
                j -= 1
            elif (dp[i - 1][j] + self.delta == dp[i][j]):
                xalligned[xptr] = x[i - 1]
                yalligned[yptr] = '_'
                xptr -= 1
                yptr -= 1
                i-=1

            elif (dp[i][j - 1] + self.delta == dp[i][j]):
                xalligned[xptr] = '_'
                yalligned[yptr] = y[j-1]
                xptr -= 1
                yptr -= 1
                j -= 1

        while (xptr > 0):
            if (i > 0):
                i-=1
                xalligned[xptr] = x[i]
            else :
                xalligned[xptr] = '_'
            if (j > 0):
                j -= 1
                yalligned[xptr] = y[j]
            else:
                yalligned[xptr] = '_'
            xptr -= 1

        id = 1
        for i in range(1,l,1):
             if (yalligned[i]=='_' and xalligned[i]!='_')or(yalligned[i]!='_' and xalligned[i]=='_')or (yalligned[i]!='_' and xalligned[i]!='_') :
                 id=i
                 break
        a=("".join(xalligned[id:]))
        b=("".join(yalligned[id:]))
        # print(dp[-1][-1])
        return a,b, dp[-1][-1]


obj = Solution(sys.argv[1])

x=(obj.readFile())
str1,d1 = obj.inputStringGenerator(x[0])
str2,d2 = obj.inputStringGenerator(x[1])
tracemalloc.start()
t0 = time.time()
obj.advancedSolver(str1,str2)
t1 = time.time()
current, peak = tracemalloc.get_traced_memory()
z = peak / 10**3
w = (t1-t0)/ 10**3
w = format(w, '.8f')
tracemalloc.stop()
f = open("output.txt", "w")
f.write(align1[:50]+" "+align1[-50:]+'\n'+align2[:50]+" "+align2[-50:]+'\n'+str(cost)+'\n'+str(w)+'\n'+str(z))
f.close()
