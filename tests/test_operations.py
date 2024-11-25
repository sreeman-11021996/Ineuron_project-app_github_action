from src.math_operations import add, sub

def test_add():
    # add function
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(-1,-2)==-3
    
def test_sub():
    # sub function
    assert sub(5,3)==2
    assert sub(-2,1)==-3
    assert sub(-2,-1)==-1