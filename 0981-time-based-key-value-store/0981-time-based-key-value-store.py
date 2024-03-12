class TimeMap:

    # APPROACH 1: TIME LIMITED EXCEEDED
#     def __init__(self):
#         self.store = dict()  # The required data structure is a nested dictionary i.e., dictionary with dictionary
#         self.timestamps = list() # This will saves all the timestamps encountered

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.store[timestamp] = dict()
#         self.store[timestamp][key] = value
#         self.timestamps.append(timestamp)
        
#     def get(self, key: str, timestamp: int) -> str:
        
#         if timestamp < self.timestamps[0]:
#             return ""

#         if timestamp in self.timestamps:
#             req_timestamp = timestamp
#         else:
#             left, right = 0, len(self.timestamps) - 1
            
#             while left <= right:
#                 mid = (left + right) // 2
#                 mid_value = self.timestamps[mid]
                
#                 if mid_value < timestamp:
#                     left = mid + 1
                    
#                 if mid_value > timestamp:
#                     right = mid 
                    
#             req_timestamp = self.timestamps[right]
            
        
#         if key not in self.store[req_timestamp]:
#             return ""
#         else:
#             return self.store[req_timestamp][key]


        ## APPROACH 2
        def __init__(self):
        # Initialize an empty dictionary to store key-value pairs.
            self.tmdict = {}

        def set(self, key: str, value: str, timestamp: int) -> None:
            #self.tmdict[key] = self.tmdict.get(key,[]) + [[value,timestamp]] -> This takes O(n)
            # If the key is not in the dictionary, create a new list for it.
            # Otherwise, append the new value & timestamp to the existing list -> This takes O(1)
            if key not in self.tmdict:
                self.tmdict[key] = [(value, timestamp)]
            else:
                self.tmdict[key].append((value, int(timestamp)))

        def get(self, key: str, timestamp: int) -> str:
            res = ""
            # If the key is not in the dictionary, return an empty string.
            if key not in self.tmdict:
               return res
            else:
                # Retrieve the list of values & timestamps for the key
                t = -1
                pairs = self.tmdict.get(key,[]) #self.tmdict[key]
                # If there's only one pair & its timestamp is <= to the given timestamp,
                # return its value.
                if len(pairs) == 1 and pairs[0][1] <= timestamp:
                    return pairs[0][0]
                # If the given timestamp is < the first timestamp in the list,
                # return an empty string because there's no valid value for this timestamp.
                if timestamp < self.tmdict[key][0][1]:
                    return res
                # Use binary search to find the value with the largest timestamp that is <= to the given timestamp.
                left,right = 0, len(pairs)-1

                while left <= right:
                    midindex = (left+right)//2
                    if pairs[midindex][1] > timestamp:
                        right = midindex -1
                    else:
                        res = pairs[midindex][0]
                        left = midindex + 1
                return res 
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)