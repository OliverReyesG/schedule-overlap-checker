import pytest
from reports.report_renderer import ConsoleRenderer


def test_report_renderer_length(capsys):
    report = [("Test1-Test2", 2), ("Test1-Test3", 3), ("Test2-Test3", 1)]
    report_renderer = ConsoleRenderer()
    report_renderer.render(report=report)
    out, err = capsys.readouterr()
    assert len(out) == 45


def test_report_render_output(capsys):
    report = [("Test1-Test2", 2), ("Test1-Test3", 3), ("Test2-Test3", 1)]
    report_renderer = ConsoleRenderer()
    report_renderer.render(report=report)
    out, err = capsys.readouterr()
    assert out == "Test1-Test2: 2\nTest1-Test3: 3\nTest2-Test3: 1\n"