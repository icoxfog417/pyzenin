from modules.dummy import x


class TestDummy:
    def test_dummy(self) -> None:
        assert x(3) == 3
