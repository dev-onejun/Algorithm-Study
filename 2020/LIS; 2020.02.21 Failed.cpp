/*
   cache 저장 값이 잘못되어 있음.
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//#define LOCAL

// S : 수열 S.	result : 탐색 과정의 부분수열
vector<int> S, result;

/*
   int LIS(const int& n)
   *	완전탐색
   *	const int& n : 현재까지 탐색한 수열 S의 index
 */
int LIS(const int& n);

const int SEQUENCE_NUM = 500;
int cache[SEQUENCE_NUM];
/*
   int memoizedLIS(const int& n)
   *	Memoization
 */
int memoizedLIS(const int& n);

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int C;	cin >> C;
	while(C--)
	{
		// Init Data
		fill(cache, cache + SEQUENCE_NUM, -1);
		int N;	cin >> N;
		for(int i=0; i<N; i++)
		{
			int input;	cin >> input;
			S.push_back(input);
		}
		result.push_back(0);

		// Print Searched Result
		//cout << LIS(0) << endl;
		//cout << memoizedLIS(0) << endl;
		int maxLen = 0;
		for(int begin = 0; begin < N; begin++)
		{
			maxLen = max(maxLen, memoizedLIS(begin));
			result.clear();	result.push_back(0);
			fill(cache, cache + SEQUENCE_NUM, -1);
		}
		cout << maxLen << endl;
	
		S.clear();	result.clear();
	}

	return 0;
}

int LIS(const int& n)
{
	// 기저사례 : 수열 S의 마지막에 도달했을 때
	if(n == S.size())
		return result.size() - 1;

	// Calculate Answer
	int max_size = -1;
	// 부분수열의 마지막 수보다, S[n]의 값이 더 크면
	if(result[result.size() - 1] < S[n])
	{
		// S[n]을 넣고 탐색
		result.push_back(S[n]);
		max_size = LIS(n + 1);
		result.pop_back();
	}
	// S[n]을 안 넣는 경우
	max_size = max(max_size, LIS(n + 1));

	return max_size;
}
int memoizedLIS(const int& n)
{
	if(n == S.size())
		return result.size() - 1;

	// Memoization
	int& ref = cache[n];
	if(ref != -1)	return ref;

	int max_size = -1;
	if(result[result.size() - 1] < S[n])
	{
		result.push_back(S[n]);
		max_size = memoizedLIS(n + 1);
		result.pop_back();
	}
	max_size = max(max_size, memoizedLIS(n + 1));
	return ref = max_size;
}
