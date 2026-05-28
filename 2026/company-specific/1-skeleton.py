"""
Practice skeleton for a 45-minute Python-centric coding interview.

Use this file as the version you fill in during practice. It includes the
problem prompts, function signatures, expected behavior, and assert-based tests,
but leaves the implementations blank.

Provenance: prompts and tests prepared/generated via my OpenClaw + GPT 5.5 system.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SafetySummary:
    total_runs: int
    total_events: int
    collision_runs: int
    collision_rate: float
    ttc_violation_count: int
    ttc_violation_rate: float
    min_ttc_by_run: dict[str, float]
    avg_speed: float | None
    worst_run_id: str | None


def moving_average_fixed(values: list[float], k: int) -> list[float]:
    """
    Problem:
    You are given a list of numeric sensor readings and an integer window size k.
    Return a list where each output value is the average of the current reading
    and up to the previous k - 1 readings. For the first few readings, average
    over the values available so far.

    Example:
    values = [10, 20, 30, 40], k = 3
    output = [10.0, 15.0, 20.0, 30.0]

    Requirements:
    - Preserve input order.
    - Return one average per input value.
    - If values is empty, return [].
    - If k <= 0, raise ValueError.

    Target complexity:
    - Time: O(n)
    - Space: O(k)
    """
    raise NotImplementedError


def moving_average_time_window(
    points: list[tuple[float, float]], window_seconds: float
) -> list[tuple[float, float]]:
    """
    Problem:
    You are given sorted (timestamp, value) points and a time window in seconds.
    For each point, return the average value among points whose timestamps are in
    [current_timestamp - window_seconds, current_timestamp].

    Example:
    points = [(0, 10), (1, 20), (4, 30), (5, 40)], window_seconds = 3
    output = [(0, 10.0), (1, 15.0), (4, 25.0), (5, 35.0)]

    Requirements:
    - Assume points are sorted by timestamp.
    - The left boundary is inclusive.
    - If points is empty, return [].
    - If window_seconds < 0, raise ValueError.

    Target complexity:
    - Time: O(n)
    - Space: O(w), where w is the max number of points inside the window
    """
    raise NotImplementedError


def compute_safety_metrics(
    events: list[dict[str, Any]], ttc_threshold: float = 1.5
) -> SafetySummary:
    """
    Problem:
    You are given event records from autonomous-driving simulation runs. Each
    event may include run_id, collision, ttc, and speed. Compute summary safety
    metrics.

    Expected event fields:
    - run_id: str
    - collision: bool, optional, defaults to False
    - ttc: float | None, optional
    - speed: float | None, optional

    Return:
    - total_runs: number of unique run IDs
    - total_events: number of event records
    - collision_runs: number of unique runs with at least one collision
    - collision_rate: collision_runs / total_runs
    - ttc_violation_count: number of non-missing TTC values below threshold
    - ttc_violation_rate: ttc_violation_count / number of non-missing TTC values
    - min_ttc_by_run: minimum TTC for each run with TTC data
    - avg_speed: average over non-missing speed values, or None
    - worst_run_id: selected by choose_worst_run

    Requirements:
    - Empty input returns zero counts/rates and None unavailable fields.
    - TTC violation means ttc < threshold, not <= threshold.
    - Missing ttc and speed are skipped for those metrics.

    Target complexity:
    - Time: O(n)
    - Space: O(r), where r is number of unique runs
    """
    raise NotImplementedError


def choose_worst_run(
    collision_run_ids: set[str], min_ttc_by_run: dict[str, float]
) -> str | None:
    """
    Problem:
    Given a set of run IDs that had collisions and a dictionary mapping run_id to
    minimum TTC, choose the worst run.

    Ranking rule:
    1. Any collision run is worse than a non-collision run.
    2. Within the same collision group, smaller minimum TTC is worse.

    Requirements:
    - Return None if there are no candidates.
    - A collision run with no TTC is still worse than any non-collision run.

    Target complexity:
    - Time: O(r)
    - Space: O(r)
    """
    raise NotImplementedError


def parse_log_line(line: str) -> dict[str, Any]:
    """
    Problem:
    You are given a structured log line where the first token is a timestamp and
    the remaining tokens are key=value fields. Parse one line into a dictionary,
    convert simple scalar values, and normalize run to run_id.

    Example:
    line = "2026-05-24T10:01:03Z run=r7 speed=12.3 collision=false"
    output includes:
    {"timestamp": "2026-05-24T10:01:03Z", "run_id": "r7", "speed": 12.3}

    Requirements:
    - Values do not contain spaces.
    - Empty line raises ValueError.
    - Tokens without "=" may be ignored.
    - "run" should also be available as "run_id".
    """
    raise NotImplementedError


def parse_scalar(value: str) -> Any:
    """
    Problem:
    Convert a scalar string from a log line to bool, int, float, or leave it as a
    string if no simple conversion applies.

    Requirements:
    - "true" and "false" are case-insensitive booleans.
    - Numeric integers become int.
    - Numeric decimal values become float.
    - Unknown values remain strings.
    """
    raise NotImplementedError


def aggregate_logs_by_run(lines: list[str]) -> dict[str, dict[str, Any]]:
    """
    Problem:
    You are given many structured log lines. Parse them and produce per-run
    aggregates.

    Return one dictionary per run_id containing:
    - event_count
    - collision_count
    - avg_speed
    - min_ttc

    Requirements:
    - Empty input returns {}.
    - Malformed empty lines should fail through parse_log_line.
    - Records with no run_id are grouped as "unknown".
    - Missing speed or ttc fields are skipped for those metrics.
    - If a run has no speed or ttc values, return None for that metric.
    """
    raise NotImplementedError


def flatten_runs_json(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Problem:
    You are given nested JSON containing simulation runs, and each run contains
    metadata plus a list of events. Flatten it into one row per event while
    carrying run-level fields such as run_id and scenario onto each row.

    Expected shape:
    {
      "runs": [
        {
          "run_id": "r1",
          "scenario": "left_turn",
          "events": [
            {"timestamp": 1.0, "speed": 5.2, "ttc": 2.1}
          ]
        }
      ]
    }

    Requirements:
    - Missing "runs" means no rows.
    - Missing "events" for a run means that run contributes no event rows.
    - If run-level and event-level fields conflict, event-level fields win.
    """
    raise NotImplementedError


def aggregate_flattened_rows(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """
    Problem:
    You are given flattened event rows. Group them by scenario and compute:
    - num_runs
    - num_events
    - collision_events
    - min_ttc

    Requirements:
    - Empty input returns {}.
    - Missing scenario is grouped as "unknown".
    - Missing ttc is skipped for min_ttc.
    - If a scenario has no ttc values, return min_ttc=None.
    """
    raise NotImplementedError


def run_tests() -> None:
    """
    These tests define the expected behavior. They will fail until you implement
    the functions above.
    """
    assert moving_average_fixed([10, 20, 30, 40], 3) == [10.0, 15.0, 20.0, 30.0]
    assert moving_average_fixed([2, 4], 5) == [2.0, 3.0]
    assert moving_average_fixed([], 3) == []
    try:
        moving_average_fixed([1], 0)
        raise AssertionError("expected ValueError for k=0")
    except ValueError:
        pass

    points = [(0.0, 10.0), (1.0, 20.0), (4.0, 30.0), (5.0, 40.0)]
    assert moving_average_time_window(points, 3.0) == [
        (0.0, 10.0),
        (1.0, 15.0),
        (4.0, 25.0),
        (5.0, 35.0),
    ]
    assert moving_average_time_window([(1.0, 10.0), (1.0, 20.0), (2.0, 30.0)], 0) == [
        (1.0, 10.0),
        (1.0, 15.0),
        (2.0, 30.0),
    ]
    assert moving_average_time_window([], 1.0) == []
    try:
        moving_average_time_window([(0.0, 1.0)], -1.0)
        raise AssertionError("expected ValueError for negative window")
    except ValueError:
        pass

    events = [
        {"run_id": "r1", "collision": False, "ttc": 2.4, "speed": 8.0},
        {"run_id": "r1", "collision": False, "ttc": 1.5, "speed": 9.0},
        {"run_id": "r2", "collision": True, "ttc": 0.6, "speed": 7.5},
        {"run_id": "r3", "collision": False},
    ]
    summary = compute_safety_metrics(events, ttc_threshold=1.5)
    assert summary.total_runs == 3
    assert summary.collision_runs == 1
    assert summary.collision_rate == 1 / 3
    assert summary.ttc_violation_count == 1
    assert summary.ttc_violation_rate == 1 / 3
    assert summary.min_ttc_by_run == {"r1": 1.5, "r2": 0.6}
    assert summary.avg_speed == (8.0 + 9.0 + 7.5) / 3
    assert summary.worst_run_id == "r2"

    empty_summary = compute_safety_metrics([])
    assert empty_summary.total_runs == 0
    assert empty_summary.avg_speed is None
    assert empty_summary.worst_run_id is None

    parsed = parse_log_line(
        "2026-05-24T10:01:03Z run=r7 event=brake speed=12.3 ttc=0.8 collision=false"
    )
    assert parsed["timestamp"] == "2026-05-24T10:01:03Z"
    assert parsed["run_id"] == "r7"
    assert parsed["speed"] == 12.3
    assert parsed["collision"] is False
    try:
        parse_log_line("")
        raise AssertionError("expected ValueError for empty log line")
    except ValueError:
        pass

    logs = [
        "t1 run=r7 speed=12.0 ttc=0.8 collision=false",
        "t2 run=r7 speed=8.0 collision=false",
        "t3 run=r8 ttc=0.2 collision=true",
    ]
    log_summary = aggregate_logs_by_run(logs)
    assert log_summary["r7"]["event_count"] == 2
    assert log_summary["r7"]["avg_speed"] == 10.0
    assert log_summary["r7"]["min_ttc"] == 0.8
    assert log_summary["r8"]["avg_speed"] is None
    assert aggregate_logs_by_run([]) == {}

    payload = {
        "runs": [
            {
                "run_id": "r1",
                "scenario": "left_turn",
                "events": [
                    {"timestamp": 0.0, "ttc": 2.0, "collision": False},
                    {"timestamp": 1.0, "ttc": 1.0, "collision": False},
                ],
            },
            {
                "run_id": "r2",
                "scenario": "left_turn",
                "events": [{"timestamp": 0.0, "collision": True}],
            },
            {"run_id": "r3", "scenario": "merge", "events": []},
        ]
    }
    rows = flatten_runs_json(payload)
    assert len(rows) == 3
    assert flatten_runs_json({}) == []

    scenario_summary = aggregate_flattened_rows(rows)
    assert scenario_summary["left_turn"]["num_runs"] == 2
    assert scenario_summary["left_turn"]["num_events"] == 3
    assert scenario_summary["left_turn"]["collision_events"] == 1
    assert scenario_summary["left_turn"]["min_ttc"] == 1.0
    assert aggregate_flattened_rows([]) == {}

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
