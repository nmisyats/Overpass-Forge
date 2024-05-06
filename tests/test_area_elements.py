from overpassforge.statements import  Areas
from overpassforge._variables import VariableManager
from overpassforge.filters import *
import pytest

@pytest.fixture
def paris_area():
    a = Areas(name="Paris", label="a")
    vars = VariableManager()
    vars.add_statement(a)
    return a, vars

def test_area_elements(paris_area: tuple[Areas, VariableManager]):
    a, vars = paris_area
    assert a.elements_within()._compile(vars) == "nwr(area.a);"

def test_area_nodes(paris_area: tuple[Areas, VariableManager]):
    a, vars = paris_area
    assert a.nodes_within()._compile(vars) == "node(area.a);"

def test_area_ways(paris_area: tuple[Areas, VariableManager]):
    a, vars = paris_area
    assert a.ways_within()._compile(vars) == "way(area.a);"

def test_area_realtions(paris_area: tuple[Areas, VariableManager]):
    a, vars = paris_area
    assert a.relations_within()._compile(vars) == "rel(area.a);"

def test_aera_outline(paris_area: tuple[Areas, VariableManager]):
    a, vars = paris_area
    assert a.outline()._compile(vars) == "nwr(pivot.a);"