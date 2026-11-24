class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = [] # Will store the time it takes for fleet leaders to reach the target
        
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # If the stack is not empty and the current car takes LESS than or EQUAL 
            # time compared to the fleet ahead of it, it merges into that fleet.
            if stack and time_to_target <= stack[-1]:
                continue
            
            # Otherwise, it forms a new fleet
            stack.append(time_to_target)
            
        return len(stack)