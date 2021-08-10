from test_requests.api.wework import WeWork


class TestWework:
    def test_get(self):
        print(WeWork().test_get())

    def test_create(self):
        print(WeWork().test_create("aoteman996", "17603068888"))
