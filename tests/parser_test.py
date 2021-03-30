import pytest
from xdrone.parser import xdrone_parser
import logging


def test_missing_brackets():
    sample_program = "main() takeoff() land() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)

    # assert excinfo.value.args[0] == ''   <--- This should tell us what the exception message exactly is
    # test will fail if you assert the exception to be a null string


def test_missing_takeoff():
    sample_program = "main() { land() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)


def test_missing_land():
    sample_program = "main(){ takeoff() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)


def test_land_before_takeoff():
    sample_program = "main() { land() takeoff() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)


def test_blank():
    sample_program = "main() { }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)


def test_missing_fly():
    sample_program = "{ takeoff() land() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)
