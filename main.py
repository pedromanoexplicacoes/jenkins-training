from sys import exit
import sys
from junit_xml import TestSuite, TestCase


def runTests_failures():
    test_cases = [
        TestCase('Test1', 'funcional', 123.345, 'Output do teste', 'Falhou falhou!!!!!', False),
        TestCase('Test2', 'funcional', 33.24, 'Output 2', None, True),
        TestCase('Test1', 'Integracao', 5, 'Ok Integracao', None, True),
        ]
    ts = TestSuite("Test Suite", test_cases)
    with open('output.xml', 'w') as f:
        TestSuite.to_file(f, [ts], prettyprint=False)

def runTests():
    test_cases = [
        TestCase('Test1', 'funcional', 123.345, 'Output do teste', None, True),
        TestCase('Test2', 'funcional', 33.24, 'Output 2', None, True),
        TestCase('Test1', 'Integracao', 5, 'Ok Integracao', None, True),
        ]
    ts = TestSuite("Test Suite", test_cases)
    with open('output.xml', 'w') as f:
        TestSuite.to_file(f, [ts], prettyprint=False)

def main():
    if len(sys.argv) == 1:
        print("Hi, from Python !!")
        exit(0)

    if sys.argv[1] == "runtests":
        runTests()
        exit(0)
    
    if sys.argv[1] == "runtests_f":
        runTests_failures()
        exit(0)
    
    exit(1)

if __name__ == "__main__":
    main()