

def lbtt_calc(house_price: float) -> float:
    tax = 0
    if house_price > 750_000:
        taxable_amount = house_price - 750_000
        tax += taxable_amount * 0.12
        house_price = 750_000
    if house_price > 325_000:
        taxable_amount = house_price - 325_000
        tax += taxable_amount * 0.10
        house_price = 325_000
    if house_price > 250_000:
        taxable_amount = house_price - 250_000
        tax += taxable_amount * 0.05
        house_price = 250_000
    if house_price > 145_000:
        taxable_amount = house_price - 145_000
        tax += taxable_amount * 0.02
    return tax


if __name__ == "__main__":
    assert lbtt_calc(house_price=1_000_000) == 78_350
    assert lbtt_calc(house_price=250_000) == 2_100
    assert lbtt_calc(house_price=145_000) == 0
