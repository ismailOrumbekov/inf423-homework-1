import math
def time_to_cyclic(hour):
    if not (0 <= hour < 24):
        raise ValueError("Hour must be in the range [0, 24).")

    radians = (hour / 24) * 2 * math.pi
    return math.sin(radians), math.cos(radians)


def cyclic_difference(hour1, hour2):
    sin1, cos1 = time_to_cyclic(hour1)
    sin2, cos2 = time_to_cyclic(hour2)

    dot_product = sin1 * sin2 + cos1 * cos2
    angle_difference = math.acos(dot_product)

    hour_difference = (angle_difference / (2 * math.pi)) * 24
    return min(hour_difference, 24 - hour_difference)
