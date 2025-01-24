// ====================================================================
// CPSC 319, W25, PA-1: Comparing Algorithms
// ALGORTHM 2: Iterative
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
     * Computes the nth Fibonacci number using an iterative approach.
     *
     * @param n the position in the Fibonacci sequence (non-negative integer)
     * @return the nth Fibonacci number
     */
    public static int fibonacci(int n) {
        // Base Cases
        if (n==0) { return 0; }
        if (n==1) { return 1; }
        // Initialize variables `a` (F(0)) and `b` (F(1))
        int a =0;
        int b= 1;
        // Create a temporary variable for switching a,b later
        int tmp;

        // Use a loop to compute Fibonacci numbers sequentially from F(2) to F(n)
        for (int i=2; i<=n; i++) {
            // - Calculate the next Fibonacci number as the sum of `a` and `b`
            tmp=b;
            b=a+b;
            // - Update `a` and `b` for the next iteration
            a=tmp;
        }
        // Return the nth Fibonacci number (stored in `b` after the loop)
        return b; // Placeholder return value
    }

    /**
     * Measures execution time of the Fibonacci computation.
     *
     * @param n the position in the Fibonacci sequence
     * @param useNanoTime if true, use System.nanoTime(); otherwise, use System.currentTimeMillis()
     */
    public static void measureExecutionTime(int n, boolean useNanoTime) {
        // Initialize startTime based on useNanoTime
        long startTime=System.nanoTime();
        // Call the fibonacci method
        int fib = fibonacci(n);
        // Record the endTime and calculate elapsed time
        long endTime=System.nanoTime();

        // Print the timing results (use ns or ms based on the timing method)
        if (useNanoTime){
            System.out.println("Time elapsed: "+(endTime-startTime)+"ns");
        } else {
            System.out.println("Time elapsed: "+(endTime-startTime)/1000000 +"ms");
        }
    }

    /**
     * Main method to test the iterative Fibonacci function.
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
