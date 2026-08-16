# kite string tension, toy model
def tension(wind_ms, area_m2=0.25, cd=1.2, rho=1.2):
    return 0.5 * rho * cd * area_m2 * wind_ms ** 2

if __name__ == "__main__":
    for w in (3, 6, 9):
        print(w, round(tension(w), 2), "N")
# TODO: gust model
