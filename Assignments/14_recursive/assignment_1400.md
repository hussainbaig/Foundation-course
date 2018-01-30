## Recursion

Do the following programs using recursion: <br/>

**Ungraded** <br/>
14.1: Factorial of a number<br/>
14.2: Sum of the first n numbers<br/>
14.3: Multiples of 3<br/>
14.4: Fibonacci Series<br/>
14.5: Pascal's Triangle<br/>

**Graded**<br/>
14.6: Implement a recursive function in Python for the sieve of Eratosthenes.<br/>
The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer. It was created by the ancient Greek mathematician Eratosthenes. <br/>
The algorithm to find all the prime numbers less than or equal to a given integer n:<br/>
1. Create a list of integers from two to n: 2, 3, 4, ..., n<br/>
2. Start with a counter i set to 2, i.e. the first prime number<br/>
3. Starting from i+i, count up by i and remove those numbers from the list, i.e. 2*i, 3*i, 4*i, aso..<br/>
4. Find the first number of the list following i. This is the next prime number.<br/>
5. Set i to the number found in the previous step<br/>
6. Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to the square root of n)<br/>
All the numbers, which are still in the list, are prime numbers.<br/>
You can easily see that we would be inefficient, if we strictly used this algorithm, e.g. we will try to remove the multiples of 4, although they have been already removed by the multiples of 2. So it's enough to produce the multiples of all the prime numbers up to the square root of n. We can recursively create these sets.
