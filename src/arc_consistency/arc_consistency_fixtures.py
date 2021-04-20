def unpack_fixture(fixture):
    return (
        fixture["case_name"],
        fixture["domains"],
        fixture["constraints"],
        fixture["expected_domains"],
    )


def list_all_fixtures():
    return [fixture_00(), fixture_01()]


def fixture_00():
    return {
        "case_name": "csp_problem_00",
        "domains": {
            "a": [1, 2, 3, 4],
            "b": [1, 2, 3, 4],
            "c": [1, 2, 3, 4],
            "d": [1, 2, 3, 4],
        },
        "constraints": [
            ("a", "c", "a == 2 * c"),
            ("b", "c", "b > c + 1"),
            ("a", "d", "a > d - 1"),
        ],
        "expected_domains": {
            "a": [2, 4],
            "b": [3, 4],
            "c": [1, 2],
            "d": [1, 2, 3, 4],
        },
    }


def fixture_01():
    return {
        "case_name": "csp_problem_01",
        "domains": {
            "a": [1, 2, 3, 4],
            "b": [1, 2, 3, 4],
            "c": [1, 2, 3, 4],
            "d": [1, 2, 3, 4],
        },
        "constraints": [
            ("a", "c", "a == 2 * c"),
            ("b", "c", "b > c"),
            ("a", "d", "a > 2 * d"),
        ],
        "expected_domains": {
            "a": [4],
            "b": [3, 4],
            "c": [2],
            "d": [1],
        },
    }
