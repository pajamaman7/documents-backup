import java.io.*;
import java.util.*;

// ============================
// (1) MAIN CLASS (PA2)
// ============================

public class PA2 {

	public static void main(String[] args) {
		try {
			// (1.1) Prompt the user to enter an input file name, read the filename from standard input,
			//          and print a confirmation message before proceeding with file operations.
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the filename of the file you would like to read: ");
            String inputFileName=scanner.nextLine();
            // Don't forget to close the scanner!
            scanner.close();

			// Debugging: Print filename before reading
			System.out.println();
			System.out.println("=============================================");
            System.out.println(" 📂  Reading input file: " + inputFileName);

			// (1.2) Read the input file and store its contents as a string.
			//          If the file is empty or cannot be read, print an error message and terminate execution.
            String[] words = readFile(inputFileName).split(" ");
            

            // Debugging: Print words before sorting
            // System.out.println("---------------------------------------------");
            // System.out.println(" ⊗  Words before sorting: " + Arrays.toString(words));
			// System.out.println("---------------------------------------------");

			// (1.4) Call MergeSort to sort words alphabetically.
            MergeSort.mergeSort(words,0,words.length-1);

			// Debugging: Print words after sorting
            // System.out.println("*********************************************");
            // System.out.println(" ✓ Words after sorting: " + Arrays.toString(words));

			// (1.5) Call AnagramGrouper.groupAnagrams() to group words into singly linked lists (anagram groups).
			Map<String, SinglyLinkedList> anagramGroups = AnagramGrouper.groupAnagrams(words);

            // Debugging: Print grouped anagrams before final output
            // System.out.println("\n =============================================");
			// System.out.println(" {} Grouped Anagrams: " + anagramGroups);

			// (1.6) Call printFinalOutput() to print and save the final formatted output (anagram groups).
            printFinalOutput(anagramGroups,inputFileName);

		} catch (Exception e) {  // Catch exceptions and handle errors.
			e.printStackTrace(); // Print stack trace for debugging.
		}
	}

	// ================================
	// FUNCTION TO READ FILE CONTENT
	// ================================
	private static String readFile(String fileName) throws IOException {

		// (1.7) Create a File object for the given file name.

        File f = new File(fileName);

		// (1.8) Check if the file exists before attempting to read.
		if (!f.exists()) { // ** YOUR CODE WHERE '?' **

			// (1.9) Print an error message if the file is not found.

            System.out.println("ERROR: File does not exist!");

			// (1.10) Return an empty string if the file doesn't exist.

            return "";

		}

		// (1.11) Use StringBuilder to store file contents.
        StringBuilder bob = new StringBuilder();

		// (1.12) Use BufferedReader to read the file line by line.
        BufferedReader reader = new BufferedReader(new FileReader(f));

		// (1.13) Declare a variable to store each line read from the file.
        String line = "";

		// (1.14) Iterate through the file and read it line by line.
		while (reader.ready()) { 

			// (1.15) Append each line to StringBuilder.
            line = reader.readLine();
            bob.append(line+ " ");
		}

		// (1.16) Close BufferedReader.
        reader.close();

		// (1.17) Return the final string containing the file content.
        return bob.toString();
	}

	// ==========================================
	// FUNCTION TO PRINT AND SAVE FINAL OUTPUT
	// ==========================================

	public static void printFinalOutput(Map<String, SinglyLinkedList> groups, String inputFileName) {

		// (1.18) Print a header for the final grouped anagrams output.

        System.out.println();
        System.out.println("=============================================");
        System.out.println("Grouped Anagrams:");

		// (1.19) Initialize a counter to number the anagram groups in the output.
        int counter=1;

		// (1.20) Create a StringBuilder to store the formatted output before saving to a file.
        StringBuilder builder = new StringBuilder();

		// Iterate over the grouped anagrams (values of the map).
		for (SinglyLinkedList group : groups.values()) {

			// (1.21) Ensure the group is not null and contains words before printing.
			if (group != null) {  

				// (1.22) Format the group as a numbered entry and remove any extra spaces.
                String line = "Group "+counter+": "+group.toString();

				// (1.23) Print the formatted group to the console.
                System.out.println(line);

				// (1.24) Append the formatted group to the output content for file saving.
                builder.append(line + "\n");

				// (1.25) Increment the counter for the next group.
                counter++;
			}
		}

		// ==========================
		// FILE OUTPUT HANDLING
		// ==========================

		// (1.26) Save the final grouped anagrams to a text file with a modified filename based on the input file.

		// Initialize BufferedWriter for writing to the output file.
        BufferedWriter bw = null;
             try {
                 File file = new File("output-"+inputFileName);
                 String mycontent = "Grouped anagrams for " + inputFileName + ": \n";
                 /* This logic will make sure that the file 
                 * gets created if it is not present at the
                 * specified location*/
                 if (!file.exists()) {
                    file.createNewFile();
                 }

                 FileWriter fw = new FileWriter(file);
                 bw = new BufferedWriter(fw);
                 bw.write(mycontent);
                     System.out.println("File written Successfully");

                 } catch (IOException ioe) {
                  ioe.printStackTrace();
            }
		// (1.27) Use try-with-resources to ensure BufferedWriter is closed automatically after writing.
		try { 
			// (1.28) Write the final grouped anagrams output to the specified file.
            bw.write(builder.toString());

			// (1.29) Print a confirmation message indicating successful file saving.
            System.out.println("File saved successfully!");
            bw.close();

            // (1.30) Handle any IOException that may occur during file writing.
		} catch (IOException e) { 
			// (1.31) Print an error message to standard error (stderr) if file writing fails.
			e.printStackTrace(); 
		}
	}
}

// ============================
// (2) MERGE SORT CLASS
// ============================
class MergeSort {
	public static void mergeSort(String[] array, int left, int right) {

		// left represents the starting index of the current subarray 'array'.
		// right represents the ending index of the current subarray 'array'.

		// (2.1) If the subarray has at least two elements, then it can still be split further.
		if (left<right)  { // ** YOUR CODE WHERE '?' **

			// (2.2) Calculate the middle index to divide the array into two halves.
            int middle = left+(right-left)/2;

			// Debugging: Print subarray being sorted

			// (2.3) Recursively sort the left half of the array.
            mergeSort(array,left,middle);

			// (2.4) Recursively sort the right half of the array.
            mergeSort(array,middle+1,right);

            // (2.5) Merge the left and right half of the array.
            merge(array,left,middle,right);
		}
	}

	// ==================================================
	// MERGE FUNCTION to combine two sorted subarrays.
	// ==================================================
	private static void merge(String[] array, int left, int mid, int right) {

		// (2.6) Compute the sizes of the two subarrays to be merged.

        int leftSize = mid-left+1;
        int rightSize = right-mid;

		// (2.7) Create temporary arrays to store elements from the left and right subarrays.

        String[] leftArray = new String[leftSize];
        String[] rightArray = new String[rightSize];

		// (2.8) Copy data from the original array into the left and right subarrays.
        for (int i = 0; i<leftSize; i++ ){
            leftArray[i]=array[left+i];
        }
        for (int i = 0; i<rightSize; i++ ){
            rightArray[i]=array[mid+i+1];
        }

		// Debugging: Print subarrays before merging
		//System.out.println("( ................... )");
		//System.out.println(" ∪ Merging: " + Arrays.toString(leftArray) + " and " + Arrays.toString(rightArray));

		// (2.9) Merge the two subarrays by comparing their elements.
        // Iterate over the right array;
        // i := pos in array
        // j:= pos in leftArray
        // k:= pos in rightArray
        int j=0, k = 0, i = left;
        while (k<rightSize&&j<leftSize) {
            if (leftArray[j].compareTo(rightArray[k])<=0) {// Will be negative if the leftArray element is before the right in the alphabet.
                array[i++]=leftArray[j++];
            } else {
                array[i++]=rightArray[k++];
            }
        }

		// (2.10) Copy any remaining elements from `leftArray` to `array`.

		// ** YOUR CODE HERE **
        while (j<leftSize) {
            array[i++]=leftArray[j++];
        }
		// (2.11) Copy any remaining elements from `rightArray` to `array`.
        while (k<rightSize) {
            array[i++]=rightArray[k++];
        }

		// Debugging: Print merged array
		// System.out.println(" ≡ After Merge: " + Arrays.toString(Arrays.copyOfRange(array, left, right + 1)));
	}
}

// ====================================
// (5) SINGLY LINKED LIST CLASS
// ====================================

class SinglyLinkedList {

	// (5.1) Declare a head node representing the start of the linked list
    Node head=new Node(null);

	// (5.2) Define the node structure for a singly linked list.
	private static class Node {
		// (5.2) Store the Data (word) in this node
        private String data;
        Node next;

		// (5.3) Constructor for Node in SinglyLinkedList. Creates a new linked list node containing a word.
        Node(String word){
            this.data=word;
        }
	}

	// =====================================================
	// ADD SORTED METHOD to insert a word in sorted order
	// =====================================================
	public void addSorted(String word) {

		// (5.4) Allocate new Node
        Node node = new Node(word);

		// (5.5) Handle insertion at the beginning of the list:
		//            If the list is empty (i.e., head == NULL) OR
		//            If word comes before head.data alphabetically, THEN we insert at the beginning.
		//            Return immediately after inserting at the head to avoid unnecessary traversal.
        if (head.data==null||word.compareTo(head.data)>0) {
            node.next=head;
            head=node;
            return;
        }

		// (5.6) Position 'current' at the beginning of the singly linked list
		
        Node current = this.head;

		// (5.7) Traverse to find correct insertion point
		//            -------------------------------------------
		//            Moves forward in the linked list until:
		//            (1) The end of the list is reached (current.next == null).
		//            (2) The first node with data lexicographically greater than or equal to word is found.
        while (current.next !=null && current.data.compareTo(word)<0){
            current=current.next;
        }

		// (5.8) Insert the new node at the correct position
        node.next=current.next;
		current.next=node;
	}

	// (5.9) Implement method to check if the list is empty
	public boolean isEmpty() {
        return (this.head==null);
	}

	// ===============================================================
	// METHOD TO RETURN A STRING REPRESENTATION OF THE LINKED LIST.
	//
	// This method produces a human-readable representation of the linked list, where elements are separated by spaces.
	// Example:
	//          --------------------------------------------------
	//          SinglyLinkedList list = new SinglyLinkedList();
	//          list.addSorted("banana");
	//          list.addSorted("apple");
	//          list.addSorted("cherry");
	//          --------------------------------------------------
	//          Final Output: "apple banana cherry"
	// ===============================================================

	@Override // Java annotation that indicates a method overrides a method from its superclass.

	// Convert the linked list to a formatted string representation
	public String toString() {

		// (5.10) Initialize a StringBuilder to store the result
		
        StringBuilder bob = new StringBuilder();

		// (5.11) Start from the head of the linked list
		
        Node current = this.head;

		// (5.12) Traverse the entire linked list
		while (current.next!=null) { 

			// (5.13) Append the current node's data to the string
			bob.append(current.data);


			// (5.15) Move to the next node in the list
            current=current.next;

			// (5.14) Add a space if there is another node after this
            if (current.next!=null){
                bob.append (" ");
            }
		}

		// (5.16) Return the final formatted string
		
        return bob.toString();
	}
}

// =======================================================
// (6) ANAGRAM GROUPER CLASS (with Insertion Sort)
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
			// System.out.println("*********************************************");
			// System.out.println(" ∴ Canonical form of '" + word + "' is '" + canonicalForm + "'");

			// Create a new linked list if this key does not exist
			map.putIfAbsent(canonicalForm, new SinglyLinkedList());

			// Add the word into the appropriate linked list (maintaining order)
			map.get(canonicalForm).addSorted(word);

			// Debugging: Print updated anagram group
			// System.out.println(" + Adding '" + word + "' to group: " + map.get(canonicalForm));
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
		
        char[] charArr = word.toCharArray();

		// (6.6) Sort characters in-place calling insertion sort
        insertionSort(charArr);

		// (6.7) Return the converted sorted character array back to a string
        return String.copyValueOf(charArr);
	}

	// =================================
	// METHOD insertionSort()
	// Implement insertion sort for sorting characters in a word
	// =================================
	private static void insertionSort(char[] arr) {
		// Debugging: Initial array state
		// System.out.println();
		// System.out.println("=============================================");
		// System.out.println(" ► Starting Insertion Sort on: " + Arrays.toString(arr)); 

		// (6.8) Iterate over the array starting from index 1.
		for (int i = 1; i< arr.length; i++) { 

			// (6.9) Store the current element (`key`) to be inserted into the sorted section.
            char key = arr[i];

			// (6.10) Initialize `j` to track the last element in the sorted portion of the array.
            int j = i-1;

			// Debugging: Show current key being inserted
			//System.out.println("-----------------------------");
			//System.out.println(" ↳  Inserting '" + key + "' into sorted portion: " + Arrays.toString(Arrays.copyOfRange(arr, 0, i)));

			// (6.11) Iterate backwards through the sorted portion of the array:
			//             - Compare `key` with each element in the sorted section,
			//             - Shift elements that are greater than `key` to the right.
			while ( j>=0 && arr[j]>key ) { 

				// (6.12) Shift `arr[j]` one position to the right to create space for `key`.
                arr[j+1]=arr[j];

				// (6.13) Move `j` one step left to continue shifting process.
                j--;

				// Debugging: Show shifting process
				// System.out.println(" ⟲  Shifting " + Arrays.toString(arr));
			}

			// (6.14) Place `key` at its correct position after all shifts.
            arr[j+1]=key;

			// Debugging: Show array state after inserting key
			// System.out.println(" ✔  After inserting '" + key + "': " + Arrays.toString(arr));
		}
	}
}
