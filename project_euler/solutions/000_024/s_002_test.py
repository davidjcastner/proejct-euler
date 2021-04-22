from s_002 import solve


def test_simplified_version() -> None:
    answer = solve(limit=100)
    assert type(answer) == str
    assert answer == str(2 + 8 + 34)


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '4613732'
