/*
*	https://www.algospot.com/judge/problem/read/FESTIVAL
*	책 "알고리즘 문제 해결 전략 1" / 구종만 저 / 인사이트 / pp.6~7

*	Aaaaiiiiiee
*/
#include <iostream>
#include <vector>
using namespace std;

vector<int> cost;	// Cost of hall for each days.

int main(void)
{
	int C;					// The number of testcase
	int N, L;				// N : The number of rentable.	L : Team, already reserved.
	vector<double> result;		// Answer of each testcase.

	cin >> C;
	while(C--)
	{
		/* Input Data */
		cin >> N >> L;
		for (int i = 0; i < N; i++)
		{
			int tmp;	cin >> tmp;
			cost.push_back(tmp);
		}

		/* Algorithm. View All. */
		double min = 987654321.0;
		/* Sum L, L+1, L+2, ... N */
		for (int i = L; i <= N; i++)
		{
			double average = 0;
			/* Set start point 0 to N-i enable to search */
			for (int j = 0; j <= N - i; j++)
			{
				/* Sum cost[k] until k < j */
				for (int k = j; k - j < i; k++)
					average += cost[k];
				average /= i;

				/* Find MIN */
				min = min > average ? average : min;
			}
		}
		result.push_back(min);

		/* Initialize Variable */
		cost.clear();
	}

	/* Print Result */
	for (double e : result)
		printf("%.12f\n", e);

	return 0;
}