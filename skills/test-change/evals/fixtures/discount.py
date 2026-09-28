def discounted_subtotal(subtotal, delivery, discount):
    """Discount applies at subtotal >= 100, excluding delivery."""
    if subtotal + delivery >= 100:
        return subtotal - discount
    return subtotal
