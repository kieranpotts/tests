import sys


def lbtt_calc(house_price: float) -> float:
    bands_and_rates = [
    #     band    rate
        (145_000, 0.00),
        (250_000, 0.02),
        (325_000, 0.05),
        (750_000, 0.10),
        (sys.maxsize, 0.12)
    ]
    total_tax = 0.00
    prev_band = 0

    for band, rate in bands_and_rates:
        if house_price < prev_band:
            continue
        if house_price >= band:
            taxable_amount = band - prev_band
        else:
            taxable_amount = house_price - prev_band
        total_tax += taxable_amount * rate
        prev_band = band

    return total_tax


if __name__ == "__main__":
    assert lbtt_calc(house_price=1_000_000) == 78_350
    assert lbtt_calc(house_price=250_000) == 2_100
    assert lbtt_calc(house_price=145_000) == 0
