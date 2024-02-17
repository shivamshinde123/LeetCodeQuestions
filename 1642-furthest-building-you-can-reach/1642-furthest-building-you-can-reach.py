class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
#         can_reach = 0
#         for i in range(len(heights)-1):
#             print(f"i: {i}")
#             if heights[i] >= heights[i+1]:
#                 can_reach = i + 1
#                 print(f"{i}in if.......")
#             else:
#                 if bricks < heights[i+1] - heights[i]:
#                     ladders -= 1
#                     can_reach += 1
#                 else:
                    
#                 # if ladders > 0:
#                 #     print("in second if")
#                 #     ladders -= 1
#                 #     can_reach = i + 1
#                 # elif bricks >= heights[i+1] - heights[i]:
#                 #     print("in elif")
#                 #     bricks -= heights[i+1] - heights[i]
#                 #     can_reach = i + 1
#                 # else:
#                 #     break
            
                
                        
#         return can_reach 

        heap = []
        for i in range(len(heights)-1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1                        
                
                        
                