class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array nums to the right by k steps in-place.
        """
        n = len(nums)          # Get the length of the array
        k = k % n              # Handle cases where k > n (rotation cycles)

        # Save the last k elements to a temporary array
        # Example: nums = [1,2,3,4,5,6,7], k = 3 → temp = [5,6,7]
        temp = nums[-k:]

        # Shift the first n-k elements to the right by k positions
        # Loop backwards so that we don't overwrite elements before shifting
        for i in range(n - k - 1, -1, -1):  
            nums[i + k] = nums[i]   # Place each element i into its shifted position

        # Copy the saved last k elements into the first k positions
        # Final composition of rotated array
        for i in range(k):
            nums[i] = temp[i]
