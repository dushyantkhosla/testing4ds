from quadratic import quadratic
from hypothesis import given, assume, strategies as st
import math

@given(
    st.floats(min_value=-1000, max_value=1000),
    st.floats(min_value=-1000, max_value=1000),
    st.floats(min_value=-1000, max_value=1000)
)
def test_hypothesis_01(a, b, c):
    assume(abs(a) > 0.001)
    assume(abs(b) > 0.001)
    assume(abs(c) > 0.001)
    x1, x2 = quadratic(a, b, c)
    assert math.isclose(a*x1**2 + b*x1 + c, 0.0, abs_tol=0.001)
    assert math.isclose(a*x2**2 + b*x2 + c, 0.0, abs_tol=0.001)
