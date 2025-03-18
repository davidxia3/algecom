def hilbert_string_to_list(s):
    """
    Converts a Hilbert series string into a list of integer coefficients.
    
    Args:
        s (str): A string representing the Hilbert series, with terms in the form of "a_k T^k".
                 Example: "1 + 2T + 3T^2 + 4T^3"
    
    Returns:
        list: A list of integer coefficients in order of increasing powers of T.
    """
    
    coeffs = s.split("+")
    
    for i in range(len(coeffs)):
        coeffs[i] = int(coeffs[i].split("T")[0].strip())

    return coeffs


def scale_polynomial(poly, power):
    """
    Shifts the polynomial coefficients by multiplying by x^power.
    
    Args:
        poly (list): List of coefficients [a_0, a_1, ..., a_n] representing a polynomial.
        power (int): The power of x to multiply by (shifts coefficients to the right).
        
    Returns:
        list: The new list of coefficients after scaling.
    """
    if power < 0:
        raise ValueError("Power must be non-negative.")
    
    return [0] * power + poly

def get_first_coeff(poly):
    """
    Finds the first nonzero coefficient in a polynomial and its corresponding index.

    Args:
        poly (list): A list of coefficients representing a polynomial, where the index
                     corresponds to the power of x (e.g., [0, 0, 3, 4] represents 3x^2 + 4x^3).
    
    Returns:
        tuple: A tuple (coeff, index), where:
               - coeff is the first nonzero coefficient.
               - index is the position of this coefficient in the list.
               If all coefficients are zero, returns (0, 0).
    """
    
    for i in range(len(poly)):
        if poly[i] != 0:
            return (poly[i], i) 
    
    return (0, 0)

def get_weyl_of_poly(poly):
    """
    Retrieves the coefficient of the term immediately following the first nonzero term in a polynomial.

    Args:
        poly (list): A list of coefficients representing a polynomial, where the index 
                     corresponds to the power of x (e.g., [0, 0, 3, 4] represents 3x^2 + 4x^3).
    
    Returns:
        int: The coefficient of the term that comes right after the first nonzero term.
             Returns 0 if:
             - The polynomial is entirely zero.
             - The first nonzero term is the last term in the polynomial.
    """

    (first_coeff, first_power) = get_first_coeff(poly)
    if first_coeff != 0:
        if first_power + 1 >= len(poly):
            return 0
        return poly[first_power+1]
    return 0


def sub_polynomials(poly1, poly2):
    """
    Subtracts two polynomials represented by their coefficient lists.
    
    Args:
        poly1 (list): A list of coefficients representing the first polynomial.
                      The index corresponds to the power of x (e.g., [1, 2, 3] represents 1 + 2x + 3x^2).
        poly2 (list): A list of coefficients representing the second polynomial.
                      The index corresponds to the power of x (e.g., [4, 5, 6] represents 4 + 5x + 6x^2).
    
    Returns:
        list: A new list of coefficients representing the difference (poly1 - poly2).
              If one polynomial is longer than the other, the remaining coefficients are copied directly.
    """

    output = []

    for i in range(min(len(poly1), len(poly2))):
        output.append(poly1[i] - poly2[i])

    return output