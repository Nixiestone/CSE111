class FormulaError(Exception):
    """FormulaError is the type of error that the parse_formula
    function will raise if a formula is invalid.
    """

def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound list
    that stores the quantity of atoms of each element in the molecule.
    For example, this function will convert "H2O" to [["H", 2], ["O", 1]]
    and "C6H6" to [["C", 6], ["H", 6]].

    Parameters
        formula: a string that contains a chemical formula
        periodic_table_dict: the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["symbol", quantity], ["symbol", quantity], ...]
    """
    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdigit():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdigit():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_ele(formula, index):
        ele = formula[index]
        index += 1
        if index < len(formula) and formula[index].islower():
            ele += formula[index]
            index += 1
        return ele, index

    compound_list = []
    index = 0
    while index < len(formula):
        # Get the next element and quantity
        ele, index = get_ele(formula, index)
        quant, index = parse_quant(formula, index)
        
        # Verify the element exists in periodic table
        if ele not in periodic_table_dict:
            raise FormulaError(f"Invalid element symbol: {ele}")
        
        # Add element and quantity to compound list
        compound_list.append([ele, quant])

    return compound_list