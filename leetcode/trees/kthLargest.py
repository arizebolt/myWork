from ast import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.nums = nums
        self.k = k
    def add(self, val: int) -> int:

            self.nums.append(val)
            self.nums.sort()
            l = len(self.nums)
            if l == 1:
                return self.nums[-1]
            if l == 2 and self.k == 2:
                return self.nums[-2]
            if l == 2 and self.k == 1:
                return self.nums[-1]        
            else:
                return self.nums[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)