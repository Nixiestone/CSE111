import pytest
from chemistry import make_periodic_table, compute_molar_mass
from formula import parse_formula

def test_make_periodic_table():
    periodic_table = make_periodic_table()
    
    # Test that the table has the correct number of elements
    assert len(periodic_table) == 94
    
    # Test some specific elements
    assert periodic_table["H"] == ["Hydrogen", 1.00794]
    assert periodic_table["O"] == ["Oxygen", 15.9994]
    assert periodic_table["Fe"] == ["Iron", 55.845]
    assert periodic_table["Au"] == ["Gold", 196.966569]

def test_compute_molar_mass():
    periodic_table = make_periodic_table()
    
    # Test water (H2O)
    water = parse_formula("H2O", periodic_table)
    assert compute_molar_mass(water, periodic_table) == pytest.approx(1.00794*2 + 15.9994)
    
    # Test glucose (C6H12O6)
    glucose = parse_formula("C6H12O6", periodic_table)
    expected = 12.0107*6 + 1.00794*12 + 15.9994*6
    assert compute_molar_mass(glucose, periodic_table) == pytest.approx(expected)
    
    # Test carbon dioxide (CO2)
    co2 = parse_formula("CO2", periodic_table)
    assert compute_molar_mass(co2, periodic_table) == pytest.approx(12.0107 + 15.9994*2)

def test_known_molecules():
    from chemistry import known_molecules_dict, get_formula_name
    
    # Test known molecules
    assert get_formula_name("H2O", known_molecules_dict) == "water"
    assert get_formula_name("C6H6", known_molecules_dict) == "benzene"
    assert get_formula_name("C13H18O2", known_molecules_dict) == "ibuprofen"
    
    # Test unknown molecule
    assert get_formula_name("XYZ123", known_molecules_dict) == "unknown compound"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])