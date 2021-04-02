from hikStruct import *
from excepetion import HiKException


class HcnetSDK:
    def __init__(self, libPath):
        self.libPath = libPath
        self.sdk = cdll.LoadLibrary(libPath + "libhcnetsdk.so")

    def execute_func(self, func_name, *args):
        ret = eval("self.sdk.%s" % func_name)(*args)
        if ret < 0:
            raise HiKException(self.sdk.NET_DVR_GetLastError())
        else:
            return ret

    def NET_DVR_Init(self):
        self.sdk.NET_DVR_Init()

    def NET_DVR_SetConnectTime(self, waitTime: int = 2000, tryTimes: int = 1):
        self.sdk.NET_DVR_SetConnectTime(waitTime, tryTimes)

    def NET_DVR_SetReconnect(self, interval: int = 10000, enableRecon: bool = True):
        self.sdk.NET_DVR_SetReconnect(interval, enableRecon)

    def NET_DVR_Login_V40(self, address: str, user: str, password: str, port=8000):
        b_address = bytes(address, "ascii")
        b_user = bytes(user, "ascii")
        b_password = bytes(password, "ascii")

        # 构建登录信息结构体
        struLoginInfo = NET_DVR_USER_LOGIN_INFO()
        struLoginInfo.bUseAsynLogin = 0  # 同步登陆


if __name__ == '__main__':
    hs = HcnetSDK("./libs/")
    hs.NET_DVR_Init()
