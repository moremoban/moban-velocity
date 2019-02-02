import os

from nose.tools import eq_
from moban.plugins import ENGINES, BaseEngine
from moban_velocity.engine import EngineVelocity


def test_velocity_engine_type():
    engine = ENGINES.get_engine("velocity", [], "")
    assert engine.engine_cls == EngineVelocity
    pass


def test_velocity_file_test():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "velocity_tests")
    engine = BaseEngine(path, path, EngineVelocity)
    engine.render_to_file("file_tests.velocity", "file_tests.json", output)
    with open(output, "r") as output_file:
        expected_path = os.path.join("tests", "fixtures", "velocity_tests",
                                     "expected_output.txt")
        with open(expected_path) as expected_file:
            expected = expected_file.read()
            content = output_file.read()
            eq_(content, expected)
    os.unlink(output)


def test_velocity_string_template():
    string_template = "Hello $hello"
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "velocity_tests")
    engine = BaseEngine(path, path, EngineVelocity)
    engine.render_string_to_file(string_template, "file_tests.json", output)
    with open(output, "r") as output_file:
        expected = "Hello World!"
        content = output_file.read()
        eq_(content, expected)
    os.unlink(output)
