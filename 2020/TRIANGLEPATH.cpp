#include <iostream>
#include <algorithm>
using namespace std;

#define LOCAL

int n;
int** triangle;
int** cache;

/*
   int searchMax(const int&, const int&)
   *	완전탐색
 */
int searchMax(const int& wid, const int& len);
/*
   int memoizedSearch(const int&, const int&)
   *	Memoization
 */
int memoizedSearch(const int&, const int&);

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int C;	cin >> C;
	while(C--)
	{
		/* Init Data */
		cin >> n;
		triangle = new int*[n];
		cache = new int*[n];
		for(int i=0; i<n; i++)
		{
			triangle[i] = new int[n];
			cache[i] = new int[n];
			fill(&triangle[i][0], &triangle[i][n], -1);
			fill(&cache[i][0], &cache[i][n], -1);

			for(int j=0; j<i+1; j++)
				cin >> triangle[i][j];
		}

		/* Print Result */
		//cout << searchMax(0, 0) << endl;
		cout << memoizedSearch(0, 0) << endl;

		/* Free Memory */
		for(int i=0; i<n; i++)
			delete triangle[i];
		delete[]triangle;
	}

	return 0;
}

int searchMax(const int& wid, const int& len)
{
	// 기저사례 : trianglepath의 depth가 최대치일때
	if(wid == n)	return 0;

	return triangle[wid][len] + max(searchMax(wid + 1, len), searchMax(wid + 1, len + 1));
}

int memoizedSearch(const int& wid, const int& len)
{
	if(wid == n)	return 0;

	// Memoization
	int& ref = cache[wid][len];
	if(ref != -1)	return ref;

	// Calculate Answer
	return ref = triangle[wid][len] +
		max(memoizedSearch(wid + 1, len), memoizedSearch(wid + 1, len + 1));
}
