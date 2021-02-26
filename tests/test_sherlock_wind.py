from sherlock_wind import __version__
from sherlock_wind.wind import wind_speed


def test_version():
    assert __version__ == '0.1.0'


# def test_wind_speed():
#     id = "S1A_IW_GRDH_1SDV_20190811T212221_20190811T212246_028527_0339B5_B0AF"
#     bbox = [
#         -54.543690602444514,
#         46.366703072211514,
#         -50.82358734784875,
#         48.25819573445358
#     ]

#     result = wind_speed(id, bbox)

#     assert result == f"{id}.nc"


def test_wind_speed():
    id = "S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD"
    bbox = [
        -139.232834,
        68.606705,
        -131.700699,
        70.689018
    ]

    result = wind_speed(id, bbox)

    assert result == f"{id}.nc"
