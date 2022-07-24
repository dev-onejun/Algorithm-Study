#include <iostream>
#include <string>
#include "Karatsuba.hpp"
using namespace std;

#define LOCAL

int hugs(const string&, const string&);

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int C;	cin >> C;
	while(C--)
	{
		string members, fans;
		cin >> members >> fans;

		cout << hugs(members, fans) << endl;
	}

	return 0;
}

int hugs(const string& members, const string& fans)
{
	int N = members.size(),	M = fans.size();
	vector<int> A(N), B(M);
	for(int i=0; i<N; i++)	A[i] = (members[i] == 'M');
	for(int i=0; i<M; i++)	B[M-i-1] = (fans[i] == 'M');

	// Karatsuba 알고리즘에서 자리올림은 생략한다.
	vector<int> C = Karatsuba(A, B);
	int allHugs = 0;
	for(int i=N-1; i<M; i++)
		if(C[i] == 0)
			allHugs++;
	return allHugs;
}
