#include <vector>
#include <iostream>
using namespace std;

// num[]의 자릿수 올림을 처리한다.
void normalize(vector<int>& num)
{
	num.push_back(0);
	//자릿수 올림을 처리한다.
	for(int i=0; i+1 < num.size(); i++)
	{
		if(num[i] < 0)
		{
			int borrow = (abs(num[i]) + 9) / 10;
			num[i+1] -= borrow;
			num[i] += borrow * 10;
		}
		else
		{
			num[i+1] += num[i] / 10;
			num[i] %= 10;
		}
	}
}

// a += b*(10^k);를 구현한다.
void addTo(vector<int>& a, const vector<int>& b, int k)
{
	vector<int> c(max<int>(a.size(), b.size()));
	int cn = c.size();
	for(int i=0; i<cn; i++)
	{
		if(i >= a.size())		c[i] = b[i+k];
		else if(i >= b.size())	c[i] = a[i];
		else					c[i] = a[i] + b[i + k];
	}
	normalize(c);
	a = c;
}
// a -= b;를 구현한다. a>=b를 가정한다.
void subFrom(vector<int>& a, const vector<int>& b)
{
	int bn = b.size();
	for(int i=0; i<bn; i++)
		a[i] -= b[i];
	normalize(a);
}

vector<int> multiply(const vector<int>& a, const vector<int>& b)
{
	vector<int> c(a.size() + b.size() + 1, 0);
	for(int i=0; i<a.size(); i++)
		for(int j=0; j<b.size(); j++)
			c[i+j] += a[i] * b[j];
	normalize(c);
	return c;
}

// 2개의 긴 정수의 곱을 반환한다.
vector<int> Karatsuba(const vector<int>& a, const vector<int>& b)
{
	int an = a.size(), bn = b.size();
	// a가 b보다 짧을 경우 둘을 바꾼다.
	if(an < bn)	return Karatsuba(b, a);

	// 기저사례 : a나 b가 비어 있는 경우
	if(an == 0 || bn == 0)	return vector<int>();
	// 기저사례 : a가 비교적 짧은 경우 O(n^2) 곱셈으로 변경한다.
	if(an <= 50)	return multiply(a, b);

	int half = an / 2;
	// a와 b를 밑에서 half 자리와 나머지로 분리한다.
	vector<int> a0(a.begin(), a.begin() + half);
	vector<int> a1(a.begin() + half, a.end());
	vector<int> b0(b.begin(), b.begin() + min<int>(b.size(), half));
	vector<int> b1(b.begin() + min<int>(b.size(), half), b.end());

	// z2 = a1 * b1;
	vector<int> z2 = Karatsuba(a1, b1);
	// z0 = a0 * b0;
	vector<int> z0 = Karatsuba(a0, b0);
	// a0 = a0 + a1;	b0 = b0 + b1
	addTo(a0, a1, 0);	addTo(b0, b1, 0);
	// z1 = (a0*b0) - z0 - z2
	vector<int> z1 = Karatsuba(a0, b0);
	subFrom(z1, z0);
	subFrom(z1, z2);

	// ret = zo + z1 * 10^half + z2 * 10^(half*2)
	vector<int> ret;
	addTo(ret, z0, 0);
	addTo(ret, z1, half);
	addTo(ret, z2, half + half);
	return ret;
}
