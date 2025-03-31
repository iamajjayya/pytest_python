def add(a,b):
    return a + b

def test_add():
    assert add(2,2) == 4
    assert add(3,4) == 7
    assert add(6,1) == 7

#checking for  equality 

    assert add(2,3) !=7
    assert add(2,2) != 4 + 1

#Checking Boolean Conditions
    
is_logged_in = True
assert is_logged_in

fruits  = ["apple", "bannana", "cherry"]
assert "bannana" in fruits 
# assert "grape" in fruits

assert isinstance(10,int)
assert isinstance("hello",str)
# assert isinstance(10.5, str)


data = {"name" :  "Ajjayya", "age" : 25}

assert data["name"] == "Ajjayya"