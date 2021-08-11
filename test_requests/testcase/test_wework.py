from test_requests.api.wework import WeWork


class TestWework:
    def test_create(self):
        print(WeWork().test_create("aoteman996", "17603068888"))

    def test_get(self):
        print(WeWork().test_get("aoteman996"))

    def test_update(self):
        print(WeWork().test_update("aoteman996"))

    def test_delete(self):
        print(WeWork().test_delete("aoteman996"))
