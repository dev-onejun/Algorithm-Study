#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define LOCAL

// 와일드카드 패턴 w가 문자열 s에 대응되는지 여부를 반환한다.
bool match(const string&, const string&);

/*
   int cache[101][101]
   *	-1은 아직 답이 계산되지 않았음을 의미한다.(초기값)
   *	1은 해당 입력들이 서로 대응됨을 의미한다.
   *	0은 해당 입력들이 서로 대응되지 않음을 의미한다.
 */
int cache[101][101];
string W, S;
// 와일다카드 패턴 W[w..]가 문자열 S[s..]에 대응되는지 여부를 반환한다.
bool matchMemoized(int w, int s);

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int C;	cin >> C;
	while(C--)
	{
		string w, s;
		cin >> w;
		int n;	cin >> n;
		vector<string> result;
		while(n--)
		{
			cin >> s;
			if(match(w, s))
				result.push_back(s);
		}
		sort(result.begin(), result.end());
		for(string e : result)
			cout << e << endl;
	}

	return 0;
}

bool match(const string& w, const string& s)
{
<<<<<<< HEAD
	// w[pos]와 s[pos]를 맞춰나간다.
	int pos = 0;
	while(pos < s.size() && pos < w.size() &&
			(w[pos] == '?' || w[pos] == s[pos]))
			pos++;

	// 더이상 대응할 수 없으면, 왜 while문이 끝났는지 확인한다.
	
	// 2) 패턴 끝에 도달해서 끝난 경우 : 문자열도 끝났어야 대응된 것(True)이다.
	if(pos == w.size())
		return pos == s.size();
	// 4) *를 만나서 끝난 경우 : *에 몇 글자를 대응해야 할 지 재귀호출을 하며 확인한다.
	if(w[pos] == '*')
		for(int skip = 0; pos + skip <= s.size(); skip++)
			if(match(w.substr(pos + 1), s.substr(pos + skip)))
					return true;

	// 이 외의 경우에는 모두 대응되지 않는다.
	return false;
}

bool matchMemoized(int w, int s)
{
	// 메모이제이션
	int& ret = cache[w][s];
=======
	// 기저사례
	if(*w_it == *f_it)
	{
		if(w_it + 1 == w.end() && f_it + 1 != filename.end())
			return 1;
		if(f_it + 1 == filename.end())
			if(*w_it == '*')
				return 1;
			else
				return 0;

		return WildCard(w_it + 1, f_it + 1);
	}
	else if (*w_it == '?')	return WildCard(w_it + 1, f_it + 1);
	else if(*w_it != '*' && *w_it != *f_it)	return 0;

	//if (w_it == w.end())	return 1;

	if(w_it + 1 == w.end())				return 1;
	else if(f_it + 1 == filename.end())	return 0;

	int idx = *(w_it + 1) - 'a';
	
	// Memoization
	int& ret = cache[idx];
>>>>>>> 3779db14a360beac353e113b344f769c152e533c
	if(ret != -1)	return ret;

	// W[w]와 S[s]를 맞춰나간다.
	while(s < S.size() && w < W.size() &&
			(W[w] == '?' || W[w] == S[s]))	{w++;	s++;}

	// 더이상 대응할 수 없으면 왜 while문이 끝났는지 확인한다.

	// 2) 패턴 끝에 도달해서 끝난 경우 : 문자열도 끝났어야 참
	if(w == W.size())	return ret = (s == S.size());
	// 4) *를 만나서 끝난 경우 : *에 몇 글자를 대응해야 할 지 재귀호출하면서 확인한다.
	if(W[w] == '*')
		for(int skip = 0; skip + s <= S.size(); skip++)
			if(matchMemoized(w + 1, s + skip))
				return ret = 1;

	// 3) 이 외의 경우에는 모두 대응되지 않는다.
	return ret = 0;
}
