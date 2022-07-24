#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define LOCAL

string w, filename;
int cache[26];

int WildCard(string::iterator w_it, string::iterator f_it);

int main(void)
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	int C;	cin >> C;
	while(C--)
	{
		// Init Data
		fill(cache, cache + 26, -1);
		// 입력 부분에서 w가 **인 것은 *로 만들어주자? **가 올 수 있는가?
		cin >> w;
		int n;	cin >> n;
		vector<string> result;
		for(int i=0; i<n; i++)
		{
			cin >> filename;
			// Make Result
			if(WildCard(w.begin(), filename.begin()))
				result.push_back(filename);
		}

		// Print Result
		sort(result.begin(), result.end());
		for(string e : result)
			cout << e << endl;
	}
	return 0;
}

int WildCard(string::iterator w_it, string::iterator f_it)
{
	// 기저사례
	if(w_it == w.end())	return 1;
	if(*w_it == *f_it)
	{
		if(w_it + 1 == w.end())		return 1;
		if(f_it + 1 == filename.end())
			if(*w_it == '*')
				return 1;
			else
				return 0;

		return WildCard(w_it + 1, f_it + 1);
	}
	else if(*w_it != *f_it)
		return 0;

	if(w_it + 1 == w.end())				return 1;
	else if(f_it + 1 == filename.end())	return 0;

	if(*w_it == '?')	return WildCard(w_it + 1, f_it + 1);

	int idx = *(w_it + 1) - 'a';
	
	// Memoization
	int& ret = cache[idx];
	if(ret != -1)	return ret;

	// 답 계산
	for(string::iterator margin_f = f_it + 1; margin_f != filename.end(); margin_f++)
		if(*(w_it + 1) == *margin_f)
			return ret = WildCard(w_it + 2, margin_f + 1);
	
	return ret = false;
}
