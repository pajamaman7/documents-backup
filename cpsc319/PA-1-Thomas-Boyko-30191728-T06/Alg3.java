// ====================================================================
// CPSC 319, W25, PA-1: Comparing Algorithms
// ALGORTHM 3: Matrix Exponentiation
//
// Student Information:
//
// ** Full Name: Thomas Boyko
//
// ** UCID: 30191728
//
// ** Tutorial Section: T06
//
// ====================================================================

import java.util.Scanner;

public class Main {

    /**
     * Multiplies two 2x2 matrices and returns the result.
     *
     * @param A the first matrix
     * @param B the second matrix
     * @return the resulting matrix after multiplication
     */
    private static int[][] multiplyMatrices(int[][] A, int[][] B) {
        int [][] result = {{0,0},{0,0}};
        // Perform multiplication on all entries of the result matrix
        result[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0];
        result[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1];
        result[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0];
        result[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1];
        return result;
    }
    /**
     * Performs matrix exponentiation to compute FM^(n-1) in place.
     *
     * @param FM the transformation matrix
     * @param n the power to which the matrix is raised
     */
    private static int[][] matrixPower(int[][] FM, int n) {
        //Initialize base matrix for later multiplication
        int[][] M = {{1, 1}, {1, 0}}; 
        // - If n <= 1, return as FM^1 is FM itself.
        if (n<=1) {
            return FM;
        }
        // Recursive call to matrixPower, change variable so as not to affect the output
        int[][] NM=matrixPower(FM, n/2);
        //Square FM
        NM=multiplyMatrices(NM,NM);
        // If n is odd, muliply FM by the base matrix
        if (n%2==1) {
            NM=multiplyMatrices(NM,M);
        }
        return NM;
    }

    /**
     * Computes the nth Fibonacci number using matrix exponentiation.
     *
     * @param n the position in the Fibonacci sequence
     * @return the nth Fibonacci number
     */
    public static int fibonacci(int n) {
        //Handle base case for n = 0 (return 0).
        if (n==0) {
            return 0;
        }

        // Initialize the transformation matrix:
        int[][] FM = {{1, 1}, {1, 0}};

        // Call matrixPower to compute FM^(n-1).
        FM=matrixPower(FM,n-1);

        // Return the top-left element of the matrix, FM[0][0], which is F(n).
        return FM[0][0]; 
    }

    /**
     * Measures execution time of the Fibonacci computation.
     *
     * @param n the position in the Fibonacci sequence
     * @param useNanoTime if true, use System.nanoTime(); otherwise, use System.currentTimeMillis()
     */
    public static void measureExecutionTime(int n, boolean useNanoTime) {
        // Initialize startTime based on useNanoTime
        long start=System.nanoTime();
        // Call the fibonacci method
        int fib = fibonacci(n);
        // Record the endTime and calculate elapsed time
        long end=System.nanoTime();

        // Print the timing results (use ns or ms based on the timing method)
        if (useNanoTime){
            System.out.println("Time elapsed: "+(end-start)+"ns");
        } else {
            System.out.println("Time elapsed: "+(end-start)/1000000 +"ms");
        }
    }

    /**
     * Main method to test the matrix exponentiation Fibonacci function.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Iterative Fibonacci Calculation with Timing");
        // Prompt the user to enter a number `n` and read the input using Scanner
        System.out.print("Enter a number (n) to calculate F(n): ");
        int n = scanner.nextInt();
        System.out.println("\nFibonacci calculation result:");
        // Call the `fibonacci` method and display the result
        System.out.println(fibonacci(n));

        System.out.println("\nTiming Measurements:");
        // Call the `measureExecutionTime` method twice: once using System.nanoTime() and once using System.currentTimeMillis()

        measureExecutionTime(n,true);
        measureExecutionTime(n,false);
        scanner.close();
    }
}
