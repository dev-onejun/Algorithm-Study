#include <iostream>
using namespace std;

#define LOCAL

enum{INIT, TRUE, FALSE};

int** map;
int** cache;
int n;

// 참조적 투명함수. Memoization 이용.
int JumpGame(int y, int x);

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int C;	cin >> C;
	while(C--)
	{
		// Init Data
		cin >> n;
		map = new int*[n];	cache = new int*[n];
		for(int i=0; i<n; i++)
		{
			map[i] = new int[n];	cache[i] = new int[n];
			for(int j=0; j<n; j++)
				cin >> map[i][j];
			fill(cache[i], cache[i] + n, INIT);
		}

		// Print Result
		cout << (JumpGame(0, 0) == TRUE ? "YES" : "NO") << endl;

		// Memory Free
		for(int i=0; i<n; i++)
		{
			delete map[i];
			delete cache[i];
		}
		delete[]map;	delete[]cache;
	}

	return 0;
}

int JumpGame(int y, int x)
{
	// 기저사례
	if(y < 0 || y >= n)					return FALSE;
	else if(x < 0 | x >= n)				return FALSE;
	else if(x == (n-1) && y == (n-1))	return TRUE;

	// (y, x)에 대해 답을 구한적이 있으면 곧장 반환
	int& ret = cache[y][x];
	if(ret != INIT)
	{
		cout << "a" << endl;
		return ret;
	}

	// 답을 계산
	ret = (JumpGame(y + map[y][x], x) == TRUE)
		|| (JumpGame(y, x + map[y][x]) == TRUE);
	return ret;
}
