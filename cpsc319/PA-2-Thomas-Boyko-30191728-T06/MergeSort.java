// ============================
// TODO (2) MERGE SORT CLASS
// ============================
class MergeSort {
	public static void mergeSort(String[] array, int left, int right) {

		// left represents the starting index of the current subarray 'array'.
		// right represents the ending index of the current subarray 'array'.

		// TODO (2.1) If the subarray has at least two elements, then it can still be split further.
		if ( array.length>=2 )  { // ** YOUR CODE WHERE '?' **

			// TODO (2.2) Calculate the middle index to divide the array into two halves.

            int middle = (right-left)/2;

			// Debugging: Print subarray being sorted

			// (2.3) Recursively sort the left half of the array.
            mergeSort(array,left,middle);

			// (2.4) Recursively sort the right half of the array.
            mergeSort(array,middle,left);

			// ** YOUR CODE HERE **

            merge(array,left,middle,right);

			// ** YOUR CODE HERE **
		}
	}

    /**
     * Returns a bool, whether x is earlier in the alphabet than y
     **/
    private boolean  compareAlph(String x, String y) {
        xArr=x.toCharArray();
        yArr=y.toCharArray();
        return true;
    }
	// ==================================================
	// MERGE FUNCTION to combine two sorted subarrays.
	// ==================================================

	private static void merge(String[] array, int left, int mid, int right) {

		// TODO (2.6) Compute the sizes of the two subarrays to be merged.

        int leftSize = mid-left;
        int rightSize = right-mid;

		// TODO (2.7) Create temporary arrays to store elements from the left and right subarrays.

        String[] leftArr = new String[leftSize];
        String[] rightArr = new String[leftSize];

		// TODO (2.8) Copy data from the original array into the left and right subarrays.
        for (int i = 0; i<=leftSize; i++ ){
            leftArr[i]=array[left+i];
        }
        for (int i = 0; i<=rightSize; i++ ){
            rightArr[i]=array[mid+i];
        }

		// Debugging: Print subarrays before merging
		System.out.println("( ................... )");
		System.out.println(" ∪ Merging: " + Arrays.toString(leftArray) + " and " + Arrays.toString(rightArray));

		// TODO (2.9) Merge the two subarrays by comparing their elements.

		// ** YOUR CODE HERE **

		// TODO (2.10) Copy any remaining elements from `leftArray` to `array`.

		// ** YOUR CODE HERE **

		// TODO (2.11) Copy any remaining elements from `rightArray` to `array`.

		// ** YOUR CODE HERE **

		// Debugging: Print merged array
		System.out.println(" ≡ After Merge: " + Arrays.toString(Arrays.copyOfRange(array, left, right + 1)));
	}


	// =============================
	// MANUAL ARRAY COPY FUNCTION
	// =============================

	private static void manualCopy(String[] source, int sourceStart, String[] destination, int destStart, int length) {

		// (2.12) Iterate over the given range and copy elements
		for (int i = 0; i<= source.length-sourceStart; i++) { // ** YOUR CODE WHERE '?' **

			// (2.13) Copy each element from source to destination at the correct index
            destination[i+destStart]=source[i+sourceStart];
		}
	}
}
