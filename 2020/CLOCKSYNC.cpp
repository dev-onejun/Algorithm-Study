/*
*	https://www.algospot.com/judge/problem/read/CLOCKSYNC
*	책 "알고리즘 문제 해결 전략 1" / 구종만 저 / 인사이트 / p.168

*	Aaaaiiiiiee
*	2020.02.05
*/
#include <iostream>
#include <algorithm>
using namespace std;

#define INF 987654321
#define CLOCKNUMBER 16
#define SWITCHNUMBER 10
enum { TWELEVE, THREE, SIX, NINE };

/*
*	const char linked[i][j]
*	= 'x' : i번 스위치와 j번 시계가 연결되어 있다.
*	= '.' : i번 스위치와 j번 시계가 연결되어 있지 않다.
*/
const char linked[SWITCHNUMBER][CLOCKNUMBER + 1] = {
	"xxx.............",
	"...x...x.x.x....",
	"....x.....x...xx",
	"x...xxxx........",
	"......xxx.x.x...",
	"x.x...........xx",
	"...x..........xx",
	"....xx.x......xx",
	".xxxxx..........",
	"...xxx...x...x.."
};


int SwitchCount(int*, int);
bool isAllTweleve(int* cur_clock);
void push(int* cur_clock, int switch_number);

int main(void)
{
	int C;	cin >> C;
	while (C--)
	{
		/* Init Variable */
		int* clock = new int[CLOCKNUMBER];
		for (int i = 0; i < CLOCKNUMBER; i++)
		{
			cin >> clock[i];

			/* Make Data */
			clock[i] /= 3;	clock[i] %= 4;
		}

		/* Search and Print Result */
		cout << SwitchCount(clock, 0) << endl;

		/* Memory Free */
		delete[]clock;
	}

	return 0;
}

int SwitchCount(int* clock, int switch_number)
{
	if (switch_number == SWITCHNUMBER)
		return isAllTweleve(clock) ? 0 : INF;

	int ret = INF;
	for (int cnt = 0; cnt < 4; cnt++)
	{
		ret = min(ret, cnt + SwitchCount(clock, switch_number + 1));
		push(clock, switch_number);
	}
	
	return ret;
}

bool isAllTweleve(int* cur_clock)
{
	for (int index = 0; index < CLOCKNUMBER; index++)
		if (cur_clock[index] != TWELEVE)
			return false;
	return true;
}

void push(int* cur_clock, int switch_number)
{
	for(int clock = 0; clock < CLOCKNUMBER; clock++)
		if (linked[switch_number][clock] == 'x')
		{
			cur_clock[clock]++;
			cur_clock[clock] %= 4;
		}
}