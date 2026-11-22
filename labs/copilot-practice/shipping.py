"""Artificial, non-sensitive shipping policy for Copilot study exercises."""


def shipping_fee_cents(subtotal_cents: int) -> int:
    """Charge 599 cents below 10000 cents; otherwise shipping is free."""
    if not isinstance(subtotal_cents, int) or isinstance(subtotal_cents, bool):
        raise TypeError("subtotal_cents must be an integer, excluding booleans")
    if subtotal_cents < 0:
        raise ValueError("subtotal_cents must not be negative")
    return 0 if subtotal_cents >= 10000 else 599
