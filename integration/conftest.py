MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High priority
medium: Medium priority
low: Low priority
"""


def pytest_configure(config):
    map(
        lambda line: config.addinivalue_line("markers", line),
        MARKER.split("\n"),
    )
