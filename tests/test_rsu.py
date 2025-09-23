from rsu import rsu_score

def test_rsu_bounds():
    s = rsu_score(0, 0, 18, pupil_mm=3.5, microsaccades_per_min=25)
    assert 0.0 <= s <= 1.0

def test_rsu_higher_with_more_stress():
    s1 = rsu_score(120, 2.0, 12.0, pupil_mm=3.3, microsaccades_per_min=25)
    s2 = rsu_score(300, 5.0, 2.0, pupil_mm=2.6, microsaccades_per_min=40)
    assert s2 > s1
