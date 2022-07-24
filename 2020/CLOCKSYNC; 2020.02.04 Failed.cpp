/*
*	https://www.algospot.com/judge/problem/read/CLOCKSYNC
*	책 "알고리즘 문제 해결 전략 1" / 구종만 저 / 인사이트 / p.168

*	Aaaaiiiiiee
*	2020.02.04
*/
#define _SCL_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

#define CLOCKNUMBER 16
#define SWITCHNUMBER 10
enum { TWELEVE, THREE, SIX, NINE };

const int switch_move[10][5] = {
	{0,	1,	2,	-1,	-1},
	{3,	7,	9,	11,	-1},
	{4,	10,	14,	15,	-1},
	{0,	4,	5,	6,	7},
	{6,	7,	8,	10,	12},
	{0,	2,	14,	15,	-1},
	{3,	14,	15,	-1,	-1},
	{4,	5,	7,	14,	15},
	{1,	2,	3,	4,	5},
	{3,	4,	5,	9,	13} };

int SwitchCount(int*);
bool isAllTweleve(int* cur_clock);

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
		cout << SwitchCount(clock) << endl;
	}

	return 0;
}

int SwitchCount(int* clock)
{
	int* switch_push_num = new int[SWITCHNUMBER];	fill(switch_push_num, switch_push_num + SWITCHNUMBER, 0);
	queue<pair<pair<int*, int>, int*>> q;	q.push(make_pair(make_pair(clock, 0), switch_push_num));	// ((first, second), second) : ((시계 Data, count), switch_push_num)

	auto cur = q.front();
	auto cur_clock = cur.first.first;
	auto cur_count = cur.first.second;
	auto cur_switch_push = cur.second;
	/* 기저조건 2 : 스위치가 10번 이상 눌릴 경우 */
	while (cur_count <= 10 && !q.empty())
	{
		cur = q.front();	cur_clock = cur.first.first;		cur_count = cur.first.second;		cur_switch_push = cur.second;		q.pop();

		/* Push Switch */
		for (int cur_switch_num = 0; cur_switch_num < SWITCHNUMBER; cur_switch_num++)
		{
			int* pushed_switch = new int[SWITCHNUMBER];
			copy(cur_switch_push, cur_switch_push + SWITCHNUMBER, pushed_switch);
			int* moved_clock = new int[CLOCKNUMBER];
			copy(cur_clock, cur_clock + CLOCKNUMBER, moved_clock);

			/* 한 스위치를 4번 이상 못 누르게 함 */
			pushed_switch[cur_switch_num] += 1;
			if (pushed_switch[cur_switch_num] >= 4) { delete pushed_switch;	delete moved_clock;	continue; }
			
			/* Move Clock */
			for (int i = 0; (i < 5) && (switch_move[cur_switch_num][i] != -1); i++)
			{
				int clock_index = switch_move[cur_switch_num][i];
				moved_clock[clock_index] += 1;	moved_clock[clock_index] %= 4;
			}

			q.push(make_pair(make_pair(moved_clock, cur_count + 1), pushed_switch));
		}

		/* 기저조건 1 : 모든 시계가 12를 가리킬 경우 */
		if (isAllTweleve(cur_clock))	break;

		delete cur_clock;	delete cur_switch_push;
		cur_clock = nullptr;	cur_switch_push = nullptr;
	}
	
	/* Store Result */
	int ret = cur_count;

	/* Memory Free */
	if (cur_clock != nullptr)	delete cur_clock;
	if (cur_switch_push != nullptr) delete cur_switch_push;
	while (!q.empty())
	{ 
		cur = q.front();
		cur_clock = cur.first.first;
		cur_switch_push = cur.second;
		delete cur_clock;
		delete cur_switch_push;
		q.pop();
	}

	return ret > 10 ? -1 : ret;
}

bool isAllTweleve(int* cur_clock)
{
	for (int i = 0; i < CLOCKNUMBER; i++)
		if (cur_clock[i] != TWELEVE)
			return false;

	return true;
}