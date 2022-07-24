/*
 *	https://https://www.algospot.com/judge/problem/read/FENCE
 *	책 "알고리즘 문제 해결 전략 1" / 구종만 저 / 인사이트 / p. 195

 *	Aaaaiiiiiee
 *	2020/02/07
 */
#include <iostream>
#include <algorithm>
using namespace std;

//#define LOCAL

int* height;
int N;				// 판자 갯수

int FindMaxSizeSquare();

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int C;	cin >> C;
	while(C--)
	{
		/* Init Data */
		cin >> N;
		height = new int[N];
		for(int i=0; i<N; i++)
			cin >> height[i];

		/* Print Result */
		cout << FindMaxSizeSquare() << endl;

		delete[]height;
	}

	return 0;
}

int FindMaxSizeSquare()
{
	int* sorted_height = new int[N];
	copy(height, height + N, sorted_height);
	sort(sorted_height, sorted_height + N);

	int ret = 0;
	for(int cur_height_idx = 0; cur_height_idx < N; cur_height_idx++)
	{
		auto cur_height = sorted_height[cur_height_idx];

		// Find place cut-off in Variable max_wid
		int max_wid = 0, past_cut_idx = -1;
		for(int num = 0; num < N; num++)
			if(height[num] - sorted_height[cur_height_idx] < 0)
			{
				max_wid = max(max_wid, num - (past_cut_idx + 1));
				past_cut_idx = num;
			}
		max_wid = max(max_wid, N - (past_cut_idx + 1));

		// Calculate
		int cur_size_max = cur_height * max_wid;
		ret = max(ret, cur_size_max);
	}

	delete[]sorted_height;

	return ret;
}
