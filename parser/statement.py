﻿def statement(input):
    a = input.strip()
    op = a[0:a.find(" ")].strip();
    if (op == "RETURN"):
        return ReturnNode()
    if (op == "CLEAR"):
        return ClearNode()
    if (op == "LIST"):
        return ListNode()
    if (op == "RUN"):
        return RunNode()
    if (op == "END"):
        return EndNode()
    if (op == "LET"):

    
if (__name__ == "__main__"):
    pass