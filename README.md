# Algorithm Study

- [2019](./2019)
  - Group Study in SketchAlgorithm
- [2020](./2020)
  - Self Study

## Tips for Python

``` python
def python_input_tips():

    # 1
    a = list( map( int, input().split() ))
    # 2
    a, b, c = map( int, input().split() )

    print('a', a)
    print('b', b)
    print('c', c)

    # 3
    import sys
    a = sys.stdin.readline().rstrip()

def python_output_tips():

    answer = 7
    print(f'The answer is {answer}')

def python_lambda_function():

    # 1
    ## basic add() method
    def add(a, b):
        return a + b
    print( add(3, 7) )

    ## lambda function
    print( (lambda a,b: a+b)(3, 7) )

    # 2
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9,10]

    result = map( (lambda a,b: a+b), list1, list2)

def GCD_and_LCM():
    import math
    # GCD
    print(math.gcd(21, 14))
    # LCM
    print( (lambda a,b: a*b//math.gcd(a,b))(21,14) )
```
