def triangle_area(base, height):
    """
    Calcula el área de un triángulo dado su base y su altura.

    Args:
        base (float): La base del triángulo.
        height (float): La altura del triángulo.

    Returns:
        float: El área del triángulo.
    """
    if base < 0 or height < 0:
        raise ValueError("La base y la altura deben ser valores no negativos.")
    return (base * height) / 2
