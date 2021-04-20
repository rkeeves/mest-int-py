def unpack_graph_fixture(fixture):
    return (fixture[0], fixture[1])


def list_all_fixtures():
    return [graph_fixture_00()]


def graph_fixture_00():
    return (
        "a",
        {"a": ["b", "c", "e"], "b": ["c", "d"], "c": ["e"], "d": ["a", "e"], "e": []},
    )


def graph_fixture_01():
    return (
        "a",
        {
            "a": ["b", "c"],
            "b": ["c", "d"],
            "c": ["e"],
            "d": ["f", "g"],
            "e": ["g"],
            "f": [],
            "g": [],
        },
    )
