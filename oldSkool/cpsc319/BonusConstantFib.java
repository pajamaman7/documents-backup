// ====================================================================
// CPSC 319, W25, PA-1: Comparing Algorithms
// ALGORTHM 1: Recursive
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
     * Computes the nth Fibonacci number using recursion.
     *
     * @param n the position in the Fibonacci sequence (non-negative integer)
     * @return the nth Fibonacci number
     */
    public static long fibonacci(int n) {
        
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
        long fib = fibonacci(n);
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
     * Main method to test the Fibonacci computation and timing.
     *
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Recursive Fibonacci Calculation with Timing");
        System.out.print("Enter a number (n) to calculate F(n): ");
        int n = scanner.nextInt();

        System.out.println("\nFibonacci calculation result:");
        System.out.println(fibonacci(n));

        System.out.println("\nTiming Measurements:");
        measureExecutionTime(n,true);
        measureExecutionTime(n,false);
        scanner.close();
    }
}

