from overpassforge.base import Set
from overpassforge.statements import Relations, Nodes
from overpassforge._variables import VariableManager
from overpassforge.filters import *
import pytest

@pytest.fixture
def paris_area():
    a = Relations(name="Paris") + Nodes(amnity="cafe")
    a.label = "a"
    vars = VariableManager()
    vars.add_statement(a)
    return a, vars

def test_sub_elements(paris_area: tuple[Set, VariableManager]):
    a, vars = paris_area
    assert a.elements()._compile(vars) == "nwr.a;"

def test_sub_nodes(paris_area: tuple[Set, VariableManager]):
    a, vars = paris_area
    assert a.nodes()._compile(vars) == "node.a;"

def test_sub_ways(paris_area: tuple[Set, VariableManager]):
    a, vars = paris_area
    assert a.ways()._compile(vars) == "way.a;"

def test_sub_realtions(paris_area: tuple[Set, VariableManager]):
    a, vars = paris_area
    assert a.relations()._compile(vars) == "rel.a;"

def test_sub_areas(paris_area: tuple[Set, VariableManager]):
    a, vars = paris_area
    assert a.areas()._compile(vars) == "area.a;"