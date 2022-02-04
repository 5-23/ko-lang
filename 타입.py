def 정수(x):
    """
    x를 정수로 변형합니다.
    """
    return int(x)

def 실수(x):
    """
    x를 실수로 변형합니다.
    """
    return float(x)

def 글자(x):
    """
    x를 글로 변형합니다.
    """
    return str(x)

def 연산자(x):
    """
    x를 식으로 변형합니다.
    """
    return str(x)

def 식(x):
    """
    x를 식으로 변형합니다.
    """
    return str(x)

def 타입(x):
    """
    x의 타입을 변환합니다.
    """
    x = str(type(x))

    if "int" in x:x = "<정수>"

    if "float" in x:x = "<실수>"

    if "str" in x:x = "<글자>"

    if "bool" in x:x = "<연산자>"

    if "eval" in x:x = "<식>"

    return x