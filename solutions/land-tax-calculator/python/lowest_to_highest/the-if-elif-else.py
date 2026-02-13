

def lbtt_calc(house_price: float) -> float:
    if house_price <= 145_000:
        return 0
    elif 145_000 < house_price <= 250_000:
        return (house_price - 145_000) * 0.02
    elif 250_000 < house_price <= 325_000:
        return ((house_price - 250_000) * 0.05) + 2_100
    elif 325_000 < house_price <= 750_000:
        return ((house_price - 325_000) * 0.10) + 3_750 + 2_100
    else:  # house_price > 750_000
        return ((house_price - 750_000) * 0.12) + 42_500 + 3_750 + 2_100


if __name__ == "__main__":
    assert lbtt_calc(house_price=1_000_000) == 78_350
    assert lbtt_calc(house_price=250_000) == 2_100
    assert lbtt_calc(house_price=145_000) == 0
