        
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p,s in pair:
            stack.append((target-p)/s)
            # If the new car’s time is less than or equal to the time before it,
            # it catches up and merges with that fleet → pop it from the stack. 
            if len(stack) >=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)
'''
[10,8,0,5,3]
[2,4,1,1,3]

miles to travel 
[2,4,12,7,9]
time taken(hrs) to travel the miles
[1,1,12,7,3]

time taken = (target -position)/speed


'''
        