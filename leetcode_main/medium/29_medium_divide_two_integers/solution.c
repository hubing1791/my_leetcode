//看的别人的解答没有写，把别人解答冗余去了下
//https://leetcode-cn.com/problems/divide-two-integers/submissions/

#define INT_MAX 0X7FFFFFFF
#define INT_MIN 0X80000000

int divide(int dividend, int divisor)
{
	int result = 0;	 // 存放结果值
	if(dividend == 0)   // 特殊情况判断
		return 0;
	else if(dividend == INT_MIN && divisor == -1)   // 被除数为INT_MIN的两种特殊情况
		return INT_MAX;
	else if(dividend == INT_MIN && divisor == 1)
		return INT_MIN;
	else if(dividend == INT_MIN && divisor == INT_MIN)  // 除数为INT_MIN，就这两种情况
		return 1;
	else if(divisor == INT_MIN)
		return 0;

	bool negative = (dividend ^ divisor) < 0;	   // 判断结果是否为负数

	if(dividend == INT_MIN)		 // 若被除数为INT_MIN，先减一次，在再进行运算
	{
		dividend += abs(divisor);
		result++;
	}
	int t = abs(dividend);
	int d = abs(divisor);

	for(int i = 31; i >= 0; i--)
	{
		if((t >> i) >= d)
		{
			result += 1 << i;
			t -= d << i;
		}
	}
	return negative ? -result : result;
}