class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        answer = " "
        if len(s) == 0:
            return 0
        is_negative = False
        if s[0] == "-":
            is_negative = True
            s = s.replace("-","",1)
        elif s[0] == "+":
            s = s.replace("+","",1)
        for i in range(len(s)):
            try:   
                y = int(s[i])
                answer+=s[i]
            except:
                break
        if len(answer) == 1:
            return 0
        elif is_negative:
            answer = answer.replace(" ","-")
        else:
            answer = answer.replace(" ","")
        answer = int(answer)
        if answer >2**31 -1:
            answer = 2**31 -1
        elif answer < -2**31:
            answer = -2**31
        return answer
        