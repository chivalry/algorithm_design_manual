"""
Children are taught to add multi-digit numbers from right-to-left one digit at a time.
Many find the “carry” operation - in which a 1 is carried from one digit position to be
added to the next - to be a significant challenge. Your job is to count the number of
carry operations for each of a set of addition problems so that educators may assess
their difficulty.

Input
Each line of input contains two unsigned integers less than 10 digits. The last line of
input contains ‘0 0’.

Output
For each line of input except the last you should compute and print the number of carry
operations that would result from adding the two numbers, in the format shown below.

Sample Input
123 456
555 555
123 594
00

Sample Output
No carry operation.
3 carry operations.
1 carry operation.
"""


def carry_count(addend_1: str, addend_2: str) -> int:
    addend_1, addend_2 = addend_1[::-1], addend_2[::-1]
    addend_1 = addend_1.zfill(10)
    addend_2 = addend_2.zfill(10)
    count = carry = 0
    for a, b in zip(addend_1, addend_2):
        if int(a) + int(b) + carry >= 10:
            count += 1
            carry = 1
    return count


def read_input():
    while True:
        line = input('> ')
        if line == '00':
            break
        arr = [num for num in line.split()]
        count = carry_count(arr[0], arr[1])
        count = 'No' if not count else count
        plural = 's' if count != 1 else ''
        print('{} carry operation{}.'.format(count, plural))


if __name__ == '__main__':
    read_input()
