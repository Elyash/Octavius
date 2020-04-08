import pytest


@pytest.mark.lego("giraffe", exclusive=False)
def test_sync(components):
    print(f"Components a: {components}")


@pytest.mark.lego("elephant")
async def test_async(components):
    print(f"Components b: {components}")


class TestsSpecA:
    @classmethod
    @pytest.mark.lego('giraffe')
    def setup_class(cls, components):
        cls._components = components
        print(f"setup class with {cls._components}")

    @classmethod
    def teardown_class(cls):
        print(f"teardown class with {cls._components}")

    def setup_method(self):
        print(f"setup method {self._components}")

    def teardown_method(self):
        print(f"teardown method {self._components}")

    @pytest.mark.lego('zebra')
    def test_a(self, components):
        print(f"Using: {components} and {self._components}")

    @pytest.mark.lego('elephant')
    def test_b(self, components):
        print(f"Using: {components} and {self._components}")


class TestsSpecB:
    @classmethod
    @pytest.mark.lego('giraffe')
    def setup_class(cls, components):
        cls._components = components
        print(f"setup class with {cls._components}")

    @classmethod
    def teardown_class(cls):
        print(f"teardown with {cls._components}")

    @pytest.mark.lego('zebra')
    def test_a(self, components):
        print(f"Using: {components} and {self._components}")


class TestsSpecWithoutSetupClass:
    @pytest.mark.lego('zebra')
    def test_a(self, components):
        print(f"Using: {components}")


class TestsSpecSetupClassWithoutTeardown:
    @classmethod
    @pytest.mark.lego('giraffe')
    def setup_class(cls, components):
        cls._components = components
        print(f"setup class with {cls._components}")

    @pytest.mark.lego('zebra')
    def test_a(self, components):
        print(f"Using: {components}")