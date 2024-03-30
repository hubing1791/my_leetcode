# https://leetcode.cn/problems/candy/
# 2024-03-29
from typing import List

class Solution:
	
	def candy_wrong_v1(self, ratings: List[int]) -> int:
		result,tmp =1,1
		for index in range(1,len(ratings)):
			if ratings[index]>ratings[index-1]:
				tmp +=1
			else:
				tmp = 1
			result+=tmp
		return result
	
	def candy_shit(self, ratings: List[int]) -> int:
		result_list = [0]*len(ratings)
		location = []
		for index in range(1,len(ratings)-1):
			if ratings[index-1]>ratings[index] and ratings[index]<ratings[index+1]:
				result_list[index] =1
				location.append(index)
		for index in range(len(location)-1):
			left,right = location[index], location[index+1]
			for index_1 in range(left+1,right-1):
				if ratings[index_1]>ratings[index_1-1]:
					result_list[index_1] = result_list[index_1-1]+1
				elif ratings[index_1] == ratings[index_1-1]:
					result_list[index_1] = 1
				else:
					break
			for index_1 in range(right-1,left+1,-1):
				if ratings[index_1]>ratings[index_1+1]:
					result_list[index_1] = result_list[index_1+1]+1
				elif ratings[index_1] == ratings[index_1+1]:
					result_list[index_1] = 1
				else:
					break
		if len(location)>0:
			for index_1 in range(location[0],0,-1):
				if ratings[index_1]>ratings[index_1+1]:
					result_list[index_1] = result_list[index_1-1]+1
				elif ratings[index_1] == ratings[index_1-1]:
					result_list[index_1] = 1
				else:
					result_list[0]=1
					for index_1 in range(1,location[0]):
						if ratings[index_1]>ratings[index_1-1]:
							result_list[index_1] = result_list[index_1-1]+1
						elif ratings[index_1]==ratings[index_1-1]:
							result_list[index_1] = 1
						else:
							break
					break
			for index_1 in range(location[-1],len(ratings)):
				if ratings[index_1]>ratings[index_1-1]:
					result_list[index_1] = result_list[index_1-1]+1
				elif ratings[index_1] == ratings[index_1-1]:
					result_list[index_1] = 1
				else:
					result_list[-1]=1
					for index_1 in range(len(ratings)-2,location[-1],-1):
						if ratings[index_1]>ratings[index_1+1]:
							result_list[index_1] = result_list[index_1+1]+1
						elif ratings[index_1]==ratings[index_1-1]:
							result_list[index_1] = 1
						else:
							break
					break
			return sum(result_list)
	
	def candy_offical1(self, ratings: List[int]) -> int:
		length = len(ratings)
		results = [1]*length
		for i in range(1,length):
			if ratings[i]>ratings[i-1]:
				results[i] = results[i-1] + 1
		for i in range(length-2,-1,-1):
			results[i] = max(results[i+1] +1 if ratings[i] > ratings[i+1] else 1,results[i])
		return sum(results)
	
	def candy_offical2(self, ratings: List[int]) -> int:
		result,asc_num,desc_num,pre = 1,0,0,1
		for i in range(1,len(ratings)):
			if ratings[i] >= ratings[i-1]:
				desc_num = 0
				pre = 1 if ratings[i]==ratings[i-1] else pre + 1
				result+=pre
				asc_num = pre
			else:
				desc_num+=1
				# 当当前的递减序列长度和上一个递增序列等长时，需要把最近的递增序列的最后一个同学也并进递减序列中
				if desc_num == asc_num:
					desc_num += 1
				result += desc_num
				pre = 1
		return result


		
		
if __name__ == "__main__":
	test_cases = [
		[1,0,2],
		[1,2,2]
	]
	sol = Solution()
	sol.candy(test_cases[1])