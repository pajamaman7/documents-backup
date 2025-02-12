// =======================================================
// TODO (6) ANAGRAM GROUPER CLASS (with Insertion Sort)
//
// Groups words into anagram groups using a LinkedHashMap
// This method groups words that are anagrams of each other by mapping each word to a canonical form (a sorted version of its characters).
// Words that share the same canonical form belong to the same group and are stored in a singly linked list.
// Key Idea: Two words are anagrams if they have the same characters in the same frequency.
//
// Approach:
// ---------------
// (1) Sort the characters of each word to get a canonical form.
// (2) Use a LinkedHashMap<String, SinglyLinkedList>:
//     (2.1) The key is the canonical form (e.g., "acr" for "arc" and "car").
//     (2.2) The value is a singly linked list containing all words that share this form.
// (3) Words are inserted into their respective groups in sorted order.
//
// =======================================================
class AnagramGrouper {

	public static Map<String, SinglyLinkedList> groupAnagrams(String[] words) {

		// (6.1) Store anagram groups while preserving insertion order
		Map<String, SinglyLinkedList> map = new LinkedHashMap<>(); 

		// (6.2) Iterate through each word in the words array and processing them to group anagrams together.
		for (String word:words) { 

			// (6.4) Call computeCanonicalForm() to get sorted-character form of the word (anagram key)
			
            String canonicalForm =computeCanonicalForm(word);

			// Debugging: Print computed canonical form
			System.out.println("*********************************************");
			System.out.println(" ∴ Canonical form of '" + word + "' is '" + canonicalForm + "'");

			// Create a new linked list if this key does not exist
			map.putIfAbsent(canonicalForm, new SinglyLinkedList());

			// Add the word into the appropriate linked list (maintaining order)
			map.get(canonicalForm).addSorted(word);

			// Debugging: Print updated anagram group
			System.out.println(" + Adding '" + word + "' to group: " + map.get(canonicalForm));
		}

		// Return the map of anagram groups
		return map;
	}

	// ===================================================================================================
	// METHOD computeCanonicalForm()
	//
	// This method computes the canonical form of a word by sorting its characters using insertion sort.
	// It helps group anagrams by ensuring words with the same letters get the same representation.
	// Example:
	//      (1) Processing ----------------------------> "stop"
	//      (2) Convert "stop" into a character array -> ['s', 't', 'o', 'p']
	//      (3) Sort using insertion sort -------------> ['o', 'p', 's', 't']
	//      (4) Convert back to string ----------------> "opst"
	// ===================================================================================================

	private static String computeCanonicalForm(String word) {

		// (6.5) Convert word into a character array
		
        String[] charArr = word.toCharArray();

		// (6.6) Sort characters in-place calling insertion sort
        insertionSort(charArr);

		// (6.7) Return the converted sorted character array back to a string
        return charArr.toString();
	}

	// =================================
	// METHOD insertionSort()
	// Implement insertion sort for sorting characters in a word
	// =================================
	private static void insertionSort(char[] arr) {
		// Debugging: Initial array state
		System.out.println();
		System.out.println("=============================================");
		System.out.println(" ► Starting Insertion Sort on: " + Arrays.toString(arr)); 

		// (6.8) Iterate over the array starting from index 1.
		for (int i = 1; i< arr.length; i++) { // ** YOUR CODE WHERE '?' **

			// (6.9) Store the current element (`key`) to be inserted into the sorted section.
            char key = arr[i];

			// (6.10) Initialize `j` to track the last element in the sorted portion of the array.
            int j = i-1;

			// Debugging: Show current key being inserted
			System.out.println("-----------------------------");
			System.out.println(" ↳  Inserting '" + key + "' into sorted portion: " + Arrays.toString(Arrays.copyOfRange(arr, 0, i)));

			// (6.11) Iterate backwards through the sorted portion of the array:
			//             - Compare `key` with each element in the sorted section,
			//             - Shift elements that are greater than `key` to the right.
			while (key>arr[j]) { // ** YOUR CODE WHERE '?' **

				// (6.12) Shift `arr[j]` one position to the right to create space for `key`.
                arr[j+1]=arr[j];

				// (6.13) Move `j` one step left to continue shifting process.
                j--;

				// Debugging: Show shifting process
				System.out.println(" ⟲  Shifting " + Arrays.toString(arr));
			}

			// (6.14) Place `key` at its correct position after all shifts.
            arr[j]=key;

			// Debugging: Show array state after inserting key
			System.out.println(" ✔  After inserting '" + key + "': " + Arrays.toString(arr));
		}
	}

}
