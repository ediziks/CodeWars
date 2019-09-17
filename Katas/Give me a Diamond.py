'''
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James.
Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print
a diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is: " *\n ***\n*****\n ***\n *\n"
'''

def diamond(n):
    diamondString = ""

    #returns None if n is not odd or a positive integer
    if n % 2 == 0 or n <= 0:
        return None

    #draws the diamond shape into the string
    else:
        for i in range(1, n + 1, 2):
            diamondString += int((n - i) / 2) * " " + i * "*" + "\n"

        for i in range(n - 2, 0, -2):
            diamondString += int((n - i) / 2) * " " + i * "*" + "\n"

    return diamondString
