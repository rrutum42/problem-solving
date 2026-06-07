class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stk = []

        for idx, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                stk_temp, stk_idx = stk.pop()
                answer[stk_idx] = idx- stk_idx
            stk.append((temp,idx))
        
        return answer

'''
monotonically increasing stk

store temp, idx in stack
for each next temp, check if the temp is greater than stk top
if yes then 
    while next temp > stk top temp:
        temp, idx = pop stk 
        update answers[idx] = next temp idx = idx
stk.append(temp,idx)

[1,2,1,3]
stk = [(1,0)]
curr = 2

stk = []
answers[0] = 1-0 = 1
stk = [(2,1)]

curr = 1
stk = [(2,1),(1,2)]

curr = 3
stk = [(2,1)]
answers[2] = 3-2 = 1
stk = []
answers[1] = 3-1 = 2
stk = [(3,3)]
'''
        


        