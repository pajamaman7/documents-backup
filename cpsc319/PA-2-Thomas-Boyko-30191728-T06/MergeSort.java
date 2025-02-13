// ============================
// TODO (2) MERGE SORT CLASS
// ============================
class MergeSort {
	public static void mergeSort(String[] array, int left, int right) {

		// left represents the starting index of the current subarray 'array'.
		// right represents the ending index of the current subarray 'array'.

		// (2.1) If the subarray has at least two elements, then it can still be split further.
		if ( array.length>=2 )  { // ** YOUR CODE WHERE '?' **

			// (2.2) Calculate the middle index to divide the array into two halves.
            int middle = (right-left)/2;

			// Debugging: Print subarray being sorted

			// (2.3) Recursively sort the left half of the array.
            mergeSort(array,left,middle);

			// (2.4) Recursively sort the right half of the array.
            mergeSort(array,middle,left);

            // (2.5) Merge the left and right half of the array.
            merge(array,left,middle,right);
		}
	}

	// ==================================================
	// MERGE FUNCTION to combine two sorted subarrays.
	// ==================================================
	private static void merge(String[] array, int left, int mid, int right) {

		// (2.6) Compute the sizes of the two subarrays to be merged.

        int leftSize = mid-left;
        int rightSize = right-mid;

		// (2.7) Create temporary arrays to store elements from the left and right subarrays.

        String[] leftArray = new String[leftSize];
        String[] rightArray = new String[rightSize];

		// (2.8) Copy data from the original array into the left and right subarrays.
        for (int i = 0; i<leftSize; i++ ){
            leftArray[i]=array[left+i];
        }
        for (int i = 0; i<rightSize; i++ ){
            rightArray[i]=array[mid+i];
        }

		// Debugging: Print subarrays before merging
		System.out.println("( ................... )");
		System.out.println(" ∪ Merging: " + Arrays.toString(leftArray) + " and " + Arrays.toString(rightArray));

		// (2.9) Merge the two subarrays by comparing their elements.
        // Iterate over the right array;
        // i := pos in array
        // j:= pos in leftArray
        // k:= pos in rightArray
		for (int i = 0; i<rightSize+leftSize; i++) {
            int j,k=0;
            if (leftArray[j].compareTo(rightArray[k])<=0) {// Will be negative if the leftArray element is before the right in the alphabet.
                array[i]=leftArray[j];
                j++;
            } else {
                array[i]=leftArray[k];
                i++;
            }
		}

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
