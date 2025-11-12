class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Brute force solution - Time Limit Exceeded
        # n = len(nums)

        # count = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if sum(nums[i:j+1]) == k:
        #             count += 1

        # return count

        # ********************* --- APPROACH 2  ---- ************************
        # This variable will store the total count of valid subarrays
        count = 0
        
        # This variable will keep track of the running sum of elements as we go through the array
        prefix_sum = 0
        
        # This dictionary will record how often each prefix_sum value has occurred
        # It starts with {0: 1} because a sum of 0 is considered to appear once before any numbers are added
        sum_frequency = {}
        sum_frequency[0] = 1
        
        # Loop through each number in the array
        for num in nums:
            # Update the running (prefix) sum by adding the current number
            prefix_sum = prefix_sum + num
            
            # Calculate what the prefix sum would have been if there was a subarray ending here that sums to k
            difference = prefix_sum - k
            
            # Check if we've ever seen this difference before
            if difference in sum_frequency:
                # If yes, add the count of times we've seen it to the current total
                count = count + sum_frequency[difference]
            # If not, do nothing (just move on)
            
            # Now update the sum_frequency dictionary to include the current prefix_sum
            if prefix_sum in sum_frequency:
                # If we've seen this prefix_sum before, add one to its count
                sum_frequency[prefix_sum] = sum_frequency[prefix_sum] + 1
            else:
                # If we're seeing this prefix_sum for the first time, set its count to 1
                sum_frequency[prefix_sum] = 1
            # Move to the next number in nums
        # After the loop, return the total number of subarrays found
        return count


