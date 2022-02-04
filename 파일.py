def 파일읽기(파일이름):
    with open(파일이름 , "r") as f:
        return f.read()

def 파일쓰기(파일이름 , 글자):
    with open(파일이름 , "w" , encoding = "UTF-8") as f:
        f.write(글자)