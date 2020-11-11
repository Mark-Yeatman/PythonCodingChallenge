from fib import *


def test_compute_fib_number():
    assert fib_number(1) == 1
    assert fib_number(2) == 1
    assert fib_number(3) == 2
    assert fib_number(4) == 3
    assert fib_number(5) == 5
    assert fib_number(6) == 8

    assert fib_number(13) == 233
    assert fib_number(1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
