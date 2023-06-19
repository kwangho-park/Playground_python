
import platform

class TestClass:

    member =""

    # constructor (생성자)
    def __init__(self):
        # 함수를 정의하는 경우, 주석을 제외한 소스코드가 1줄 이상 있어야 에러가 발생하지않음
        self.member = "test"

    def basicTest(self):
        # python ver
        print(platform.python_version())

        query = "select ID " \
                "FK_USER_ID " \
                "FK_AH_ID " \
                "from POLICY "

        print(query)


    # java map = python dict
    def typeTest(self):
        varDict = {"key1":"value1", "key2":"value2"}

        value = varDict.get("key1")

        print(value)




