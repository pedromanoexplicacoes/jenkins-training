from sys import exit
from junit_xml import TestSuite, TestCase


def runTests():
    test_cases = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
    ts = TestSuite("my test suite", test_cases)
    with open('output.xml', 'w') as f:
        TestSuite.to_file(f, [ts], prettyprint=False)

def main():
    if len(sys.argv) == 1:
        print("Hi, from Python !!")
        exit(0)

    if sys.argv[1] == "runtests":
        runTests()
        exit(0)
    
    exit(1)

if __name__ == "__main__":
    main()