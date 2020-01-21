import re
#global variables
opstack = []  #assuming top of the stack is the end of the list
dictstack = []  #assuming top of the stack is the end of the list




#------- Part 1 TEST CASES--------------
def printTestInput(funcName, input):
    print("\n-------------------------")
    print(funcName,":")
    print("input:", input)

# 2 pts
def testDefine():
    printTestInput("define-1",'"/n1" 4')
    define("/n1", 4)
    if lookup("n1") != 4:
        print("FAIL - deduct:",-2)
        return False
    print("PASS")
    return True

# 3 pts
def testDefine2():
    printTestInput("define-2", '"/n1" 4  "/n1" 5.0')
    define("/n1", 4)
    define("/n1", 5.0)
    if lookup("n1") != 5.0:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

# 2 pts
def testLookup():
    printTestInput("lookup-1", '"/v" 3.4')
    opPush("/v")
    opPush(3.4)
    psDef()
    if lookup("v") != 3.4:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#3 pts
def testLookup2():
    printTestInput("lookup-2", '"/a" [1,2,3,4]')
    opPush("/a")
    opPush([1,2,3,4])
    psDef()
    if lookup("a") != [1,2,3,4]:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

#Arithmatic operator tests
#2 pts
def testAdd():
    printTestInput("add", '9.1 0.9 add')
    opPush(9.1)
    opPush(0.9)
    add()
    if opPop() != 10.0:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#2 pts
def testSub():
    printTestInput("sub", '10 1.5 sub')
    opPush(10)
    opPush(1.5)
    sub()
    if opPop() != 8.5:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#2 pts
def testMul():
    printTestInput("mul", '2 4.5 mul')
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

#2 pts
def testDiv():
    printTestInput("div", '10 4 div')
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True
    
#Comparison operators tests
# 3 pts
def testEq():
    printTestInput("eq", '6.0 6.0 eq')
    opPush(6.0)
    opPush(6.0)
    eq()
    if opPop() != True:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True
# 3 pts
def testLt():
    printTestInput("lt", '3.1 3.2 lt')
    opPush(3.1)
    opPush(3.2)
    lt()
    if opPop() != True:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True
# 3 pts
def testGt():
    printTestInput("gt", '4 5 gt')
    opPush(4)
    opPush(5)
    gt()
    if opPop() != False:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

#boolean operator tests
# 3 pts
def testPsAnd():
    printTestInput("psAnd", 'true false and')
    opPush(True)
    opPush(False)
    psAnd()
    if opPop() != False:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True
# 3 pts
def testPsOr():
    printTestInput("psOr", 'true false or')
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True
# 3 pts
def testPsNot():
    printTestInput("psNot", 'true not')
    opPush(True)
    psNot()
    if opPop() != False:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

# 5 pts
#Array operator tests
def testLength():
    printTestInput("length", '[1,1,2,3,4,5,6] length')
    opPush([1,1,2,3,4,5,6])
    length()
    if opPop() != 7:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

# 5 pts
def testGet():
    printTestInput("get", '[1,2,3,4,5] 0 get')
    opPush([1,2,3,4,5])
    opPush(0)
    get()
    if opPop() != 1:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

#stack manipulation functions
# 3 pts
def testDup():
    printTestInput("dup", '[1,2,3,4] dup')
    opPush([1,2,3,4])
    dup()
    if opPop()!=opPop():
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True
# 5 pts
def testExch():
    printTestInput("exch", '"/x" 5 exch')
    opPush("/x")
    opPush(5)
    exch()
    if opPop()!="/x" and opPop()!=5:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True
# 2 pts
def testPop():
    printTestInput("pop", '10 pop')
    l1 = len(opstack)
    opPush(10)
    pop()
    l2 = len(opstack)
    if l1!=l2:
        print("FAIL - deduct:", -2)
        return False
    print("PASS")
    return True

# 5 pts
def testCopy():
    printTestInput("copy", 'true 1 [1,2] 3 4 3 copy')
    opPush(True)
    opPush(1)
    opPush([1,2])
    opPush(3)
    opPush(4)
    opPush(3)
    copy()
    if opPop()!=4 and opPop()!=3 and opPop()!=[1,2] and opPop()!=4 and opPop()!=3 and opPop()!=[1,2] and opPop()!=1:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

# 3 pts
def testClear():
    printTestInput("clear", '10 clear')
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

#dictionary stack operators
# 3 pts
def testDict():
    printTestInput("dict", '1 dict')
    opPush(1)
    psDict()
    if opPop()!={}:
        print("FAIL - deduct:", -3)
        return False
    print("PASS")
    return True

# 5 pts
def testBeginEnd():
    printTestInput("begin-end-1", '/x 3 def 1 dict begin /x 4 end x')
    opPush("/x")
    opPush(3)
    psDef()
    opPush(1)
    psDict()
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

# 6 pts
def testBeginEnd2():
    printTestInput("begin-end-2", '/x 3 def 1 dict begin /x 30 def 1 dict begin /x 300 def end x')
    # define x in the bottom dictionary
    opPush("/x")
    opPush(3)
    psDef()
    opPush(1)
    psDict()
    begin()
    # define x in the second dictionary
    opPush("/x")
    opPush(30)
    psDef()
    opPush(1)
    psDict()
    begin()
    # define x in the third dictionary
    opPush("/x")
    opPush(300)
    psDef()
    end()
    if lookup("x")!=30:
        end()
        print("FAIL - deduct:", -6)
        return False
    end()
    print("PASS")
    return True

# 5 pts
def testpsDef():
    printTestInput("psDef", '/x 10 def /x 20 def x')
    opPush("/x")
    opPush(10)
    psDef()
    opPush("/x")
    opPush(20)
    psDef()
    if lookup("x")!=20:
        print("FAIL - deduct:", -5)
        return False
    print("PASS")
    return True

# 5 pts
def testpsDef2():
    printTestInput("psDef-2", '/x 10.0 def 2 dict begin /y 20.0 def x')
    opPush("/x")
    opPush(10.0)
    psDef()
    opPush(2)
    psDict()
    begin()
    opPush("/y")
    opPush(20.0)
    psDef()
    if lookup("x")!=10.0:
        end()
        print("FAIL - deduct:", -5)
        return False
    end()
    print("PASS")
    return True

#Tests to check "error checking"

# (2 pts) Make sure that the following test prints/raises an error message about the type of the second argument
# (2 pts) Also make sure that the opstack content is : ['/x', 10]
def testdivInputs():
    global opstack
    opstack = []
    opPush(10)
    opPush("/x")
    div()
    print(opstack)

# Make sure that the following test prints/raises an error message about the type of the first argument (the variable name needs be a string)
# 4 pts
def testpsDefInputs():
    opPush(1)
    opPush(10)
    psDef()

# Make sure that the following test prints/raises an error message about the type of the second argument (needs to be boolean) (  points)
# 4 pts
def testpsAndInputs():
    opPush(True)
    opPush(10)
    psAnd()

def main_part1():
    testCases = [('define',testDefine),('define2',testDefine2),('lookup',testLookup),('lookup2',testLookup2),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv), \
                 ('eq',testEq),('lt',testLt),('gt', testGt), ('psAnd', testPsAnd),('psOr', testPsOr),('psNot', testPsNot), \
                 ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('copy', testCopy), \
                 ('clear', testClear), ('dict', testDict), ('begin1', testBeginEnd), ('begin2', testBeginEnd2), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed\n', failedTests)
    else:
        return ('All part-1 tests OK\n')

import sys
def errorchecking_part1():
    print('\n------------------\nTesting "TYPE CHECKING":\n')
    try:
        testdivInputs()
        testpsDefInputs()
        testpsAndInputs()
    except:  # catch *all* exceptions
        print(sys.exc_info())

if __name__ == '__main__':
    print(main_part1())
    errorchecking_part1()