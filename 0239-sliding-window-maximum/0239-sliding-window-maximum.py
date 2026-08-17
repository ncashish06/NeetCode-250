class Solution:
    # Date Solved: 16 August 2026, Sunday
    # NC150
    # Refer: codestorywithMIK
    # Approach: Using Deque
    # Time: O(n) as every element is added(pushed) and popped only once
    # Space: O(k), excluding the output list
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        deq = deque()  # will store indices

        result = []

        for i in range(n):
            # remove the max elements from front which are out of window size
            while deq and deq[0] <= i - k:
                deq.popleft()

            # we maintain the deque in descending order
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

            deq.append(i)

            # Only when the window size first gets equal or greater than k
            # front will have the max element (dequeue is maintained in descending order)
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result
