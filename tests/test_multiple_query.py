from overpassforge.builder import build, Settings
from overpassforge.statements import *
from overpassforge.filters import *
import pytest

def test_2_independant_queries():
    a = Nodes(amenity="cafe").within(Areas(name="Paris"))
    a.out()
    b = Ways(amenity="train_station")
    b.out()
    assert build(a, b) == \
        """area["name"="Paris"]->.set_0;\n""" \
        """node["amenity"="cafe"](area.set_0);\n""" \
        """out;\n""" \
        """way["amenity"="train_station"];\n""" \
        """out;"""

def test_2_dependant_queries():
    a = Nodes(amenity="cafe").within(Areas(name="Paris"))
    a.out()
    b = Ways(amenity="train_station") + a
    b.out()
    assert build(a, b) == \
        """area["name"="Paris"]->.set_0;\n""" \
        """node["amenity"="cafe"](area.set_0)->.set_1;\n""" \
        """.set_1 out;\n""" \
        """(way["amenity"="train_station"]; .set_1;);\n""" \
        """out;"""
