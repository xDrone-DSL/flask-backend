import pytest
from xdrone.parser import xdrone_parser
import logging 

def test_missing_brackets(): 
    sample_program = "fly() TAKEOFF() LAND() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)
    
def test_missing_takeoff(): 
    sample_program = "fly() { LAND() }"
    with pytest.raises(LarkError) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)   
    
    #assert excinfo.value.args[0] == ''   <--- This should tell us what the exception message exactly is 


def test_missing_land(): 
    sample_program = "fly(){ TAKEOFF() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)

def test_land_before_takeoff(): 
    sample_program = "fly() { LAND() TAKEOFF() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)
    
def test_blank():
    sample_program = "fly() { }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)
    
def test_missing_fly(): 
    sample_program = "{ TAKEOFF() LAND() }"
    with pytest.raises(Exception) as excinfo:
        parse_tree = xdrone_parser.parse(sample_program)
    



