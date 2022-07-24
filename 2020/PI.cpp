#include <iostream>
#include <string>
using namespace std;

#define LOCAL
#define INF 987654321

int N;					// 원주율 길이
string pi;				// 원주율
int cache[10000];

/*
   int PI(n)
   *	n번째 자리에서, 최소 난이도 반환
 */
int PI(const int& n);
/*
	int checkDifficulty(n, c)
	*	원주율을 n부터 앞으로 c개를 끊었을 때, 최소 난이도를 계산해서 반환
 */
int checkDifficulty(const int& n, const int& c);

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int C;	cin >> C;
	while(C--)
	{
		// Init Data
		fill(&cache[0], &cache[10000], INF);
		cin >> pi;	N = pi.size();

		// Print Result
		cout << PI(0) << endl;
	}

	return 0;
}

int PI(const int& n)
{
	if(n == N)
		return 0;
	else if(n > N)
		return INF;

	// Memoization
	int& ret = cache[n];
	if(ret != INF)	return ret;

//	ret = min(ret, PI(n + 3) + checkDifficulty(n, 3));
//	ret = min(ret, PI(n + 4) + checkDifficulty(n, 4));
//	ret = min(ret, PI(n + 5) + checkDifficulty(n, 5));
	for(int cut = 3; cut <= 5; cut++)
		ret = min(ret, PI(n + cut) + checkDifficulty(n, cut));
	
	return ret;
}

int checkDifficulty(const int& n, const int& c)
{
	string M = pi.substr(n, c);
	
	// 난이도 1
	if(M == string(M.size(), M[0]))	return 1;

	// 등차수열인지 검사
	bool progressive = true;
	for(int i=0; i<M.size() - 1; i++)
		if(M[i+1] - M[i] != M[1] - M[0])
			progressive = false;

	// 등차수열이고 공차가 1 혹은 -1이면, 난이도 2
	if(progressive && abs(M[1] - M[0]) == 1)
		return 2;

	// 두 수가 번갈아 등장하는지 확인
	bool alternating = true;
	for(int i=0; i<M.size(); i++)
		if(M[i] != M[i%2])
			alternating = false;
	
	// 난이도 4
	if(alternating) return 4;
	// 난이도 5
	if(progressive)	return 5;
	// 난이도 10
	return 10;
}

//int checkDifficulty(const int& n, const int& c)
//{
//	// 모든 숫자가 같을 때
//	bool flag = true;
//	for(int i=(n+1)-c+1; i < (n+1); i++)
//		if(pi[i] != pi[i-1])
//			flag = false;
//	if(flag)	return 1;
//
//	// 숫자가 1씩 단조 증가하거나 단조 감소할 때
//	flag = true;
//	for(int i=(n+1)-c+1; i < (n+1); i++)
//		if(pi[i-1] + 1 != pi[i] || pi[i-1] - 1 != pi[i])
//			flag = false;
//	if(flag)	return 2;
//
//	// 두 개의 숫자가 번갈아가며 나타날 때
//	flag = true;
//	for(int i=(n+1)-c+1; i + 1 < (n+1); i++)
//		if(pi[i-1] != pi[i+1])
//			flag = false;
//	if(flag)	return 4;
//
//	// 숫자가 등차 수열을 이룰 때
//	flag = true;
//	for(int i=(n+1)-c+1; i + 1 < (n+1); i++)
//		if(pi[i-1] - pi[i] == pi[i] - pi[i+1])
//			flag = false;
//	if(flag)	return 5;
//
//	// 이 외의 모든 경우
//	return 10;
//}
