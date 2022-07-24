#include <iostream>
#include <limits>
using namespace std;

#define LOCAL

// 입력이 32비트 부호 있는 정수의 모든 갑승ㄹ 가질 수 있으므로
// 인위적인 최소치는 64비트여야 한다.
const long long NEGINF = numeric_limits<long long>::min();
int n, m, A[100], B[100];
int cache[101][101];

// min(A[indexA], B[indexB]), max(A[indexA], B[indexB])로 시작하는
// 합친 증가 부분 수열의 최대 길이를 반환한다.
// 단 indexA == indexB == -1 혹은 A[indexA] != B[indexB]라고 가정한다.
int jlis(int indexA, int indexB)
{
	// Memoization
	int& ret = cache[indexA + 1][indexB + 1];
	if(ret != -1)	return ret;

	// A[indexA], B[indexB]가 이미 존재하므로 2개는 항상 있다.
	ret = 2;
	long long a = (indexA == -1 ? NEGINF : A[indexA]);
	long long b = (indexB == -1 ? NEGINF : B[indexB]);
	long long maxElement = max(a, b);
	// 다음 원소를 찾는다.
	for(int nextA = indexA + 1; nextA < n; nextA++)
		if(maxElement < A[nextA])
			ret = max(ret, jlis(nextA, indexB) + 1);
	for(int nextB = indexB + 1; nextB < m; nextB++)
		if(maxElement < B[nextB])
			ret = max(ret, jlis(indexA, nextB) + 1);
	
	return ret;
}

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int C;	cin >> C;
	while(C--)
	{
		fill(A, A + 100, -1);
		fill(B, B + 100, -1);
		fill(&cache[0][0], &cache[101][101], -1);
		cin >> n >> m;
		for(int i=0; i<n; i++)
			cin >> A[i];
		for(int i=0; i<m; i++)
			cin >> B[i];

		cout << jlis(-1, -1) - 2 << endl;
	}

	return 0;
}
