/*
*	https://www.algospot.com/judge/problem/read/PICNIC
*	책 "알고리즘 문제 해결 전략 1" / 구종만 저 / 인사이트 / p.150

*	Aaaaiiiiiee
*	4C2 * 2C2 / 2! 형태의 pair별 중복을 골라내지 못함. 확통을 이용해 2!을 임의로 나눠주는 방식으로 풀이함.
*/
#include <iostream>
using namespace std;

int result;
bool** friends;
int N;	// 학생 수
int C, M;	// C : 테스트케이스 수, M : 친구 쌍의 수
bool* students;

int Factorial(int n);
void MakeFriends(int n);

int main(void)
{
	// Init
	cin >> C;
	while (C--)
	{
		cin >> N >> M;

		friends = new bool*[N];
		for (int i = 0; i < N; i++)
		{
			friends[i] = new bool[N];
			fill(&friends[i][0], &friends[i][N], false);
		}
		students = new bool[N];
		fill(&students[0], &students[N], true);

		for (int i = 0; i < M; i++)
		{
			int row, col;	cin >> row >> col;
			friends[row][col] = friends[col][row] = true;
		}

		// Calculate
		MakeFriends(N);
		// Print Result
		cout << result / Factorial(N / 2) << endl;

		// 메모리 초기화
		for (int i = 0; i < N; i++)
			delete friends[i];
		delete[]friends;
		delete[]students;

		// 전역변수 초기화
		result = 0;
	}

	return 0;
}

void MakeFriends(int n)
{
	// 기저조건 : 학생 수가 0이면, true
	if (n == 0) { result++; return; }

	for (int i = 0; i < N; i++)
		for (int j = i + 1; j < N; j++)
			if (students[i] && students[j] && friends[i][j])
			{
				friends[i][j] = friends[j][i] = false;
				students[i] = students[j] = false;

				MakeFriends(n - 2);

				friends[i][j] = friends[j][i] = true;
				students[i] = students[j] = true;
			}
}

int Factorial(int n)
{
	if (n == 1) return 1;
	return n * Factorial(n - 1);
}