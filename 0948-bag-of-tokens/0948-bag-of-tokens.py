class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while l <= r:
        # Option 1: We have enough power to gain a score (move left pointer up)
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                max_score = max(max_score, score)
        
        # Option 2: Not enough power, but we have a score to trade for max power (move right pointer down)
            elif score > 0 and l < r:
                power += tokens[r]
                score -= 1
                r -= 1
            
        # Option 3: We can't buy anything and can't trade points; we are stuck
            else:
                break

        return max_score