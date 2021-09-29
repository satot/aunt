class Template:
	def binary_search(self, array) -> int:
	    def condition(value) -> bool:
	        pass
	
	    # could be [0, n], [1, n] etc. Depends on problem
	    left, right = min(search_space), max(search_space) 
	    while left < right:
	        mid = left + (right - left) // 2
	        if condition(mid):
	            right = mid
	        else:
	            left = mid + 1
	    return left


class Problem1:
	def __init__(self, fn):
		self.__fn = fn

	def isBadVersion(self, n) -> bool:
		return (n >= self.__fn)
	
	def firstBadVersion(self, n) -> int:
		left, right = 1, n
		while left < right:
			mid = (left + right)//2
			print("mid:", mid)
			if self.isBadVersion(mid):
				right = mid
			else:
				left = mid + 1
		return left
	
a = Problem1(38).firstBadVersion(100)
print(a)
