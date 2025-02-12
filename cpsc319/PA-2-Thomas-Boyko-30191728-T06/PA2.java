import java.io.*;
import java.util.*;

// ============================
// TODO (1) MAIN CLASS (PA2)
// ============================

public class PA2 {

	public static void main(String[] args) {
		try {
			// (1.1) Prompt the user to enter an input file name, read the filename from standard input,
			//          and print a confirmation message before proceeding with file operations.
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the filename of the file you would like to read: ");
            String inputFileName=scanner.nextLine();

			// Debugging: Print filename before reading
			System.out.println();
			System.out.println("=============================================");
            System.out.println(" 📂  Reading input file: " + inputFileName);

			// (1.2) Read the input file and store its contents as a string.
			//          If the file is empty or cannot be read, print an error message and terminate execution.
            File f = new File(inputFileName);
            if( !f.exists || f.toString()==""){
                System.out.println("File read error! Exiting...");
                System.exit(1);
            }


			// (1.3) Process input text to extract words into a 1-D array.
			// Trim input, split words by whitespace, and store words in an array.
            BufferedReader reader = new BufferedReader(f);
            int numLines=reader.lines();
            String[] words=new String[lines];
            for (int i=0; i<lines; i++) {
                words[i]=reader.readLine();
            }

			// Debugging: Print words before sorting
            System.out.println("---------------------------------------------");
            System.out.println(" ⊗  Words before sorting: " + Arrays.toString(words));
			System.out.println("---------------------------------------------");

			// (1.4) Call MergeSort to sort words alphabetically.
            MergeSort.mergeSort(array,0,lines);

			// Debugging: Print words after sorting
			System.out.println("*********************************************");
            System.out.println(" ✓ Words after sorting: " + Arrays.toString(words));

			// TODO (1.5) Call AnagramGrouper.groupAnagrams() to group words into singly linked lists (anagram groups).
			// Map<?, ?> anagramGroups = ? // ** YOUR CODE WHERE '?' **

            // Debugging: Print grouped anagrams before final output
            //System.out.println("\n =============================================");
			//System.out.println(" {} Grouped Anagrams: " + anagramGroups);

			// TODO (1.6) Call printFinalOutput() to print and save the final formatted output (anagram groups).

            // ** YOUR CODE HERE **

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
		if (!f.exists) { // ** YOUR CODE WHERE '?' **

			// (1.9) Print an error message if the file is not found.

            System.out.println("ERROR: File does not exist!");

			// (1.10) Return an empty string if the file doesn't exist.

            return "";

		}

		// (1.11) Use StringBuilder to store file contents.

        StringBuilder bob = new StringBuilder();

		// (1.12) Use BufferedReader to read the file line by line.

        BufferedReader reader = new BufferedReader(f);

		// (1.13) Declare a variable to store each line read from the file.

        String line = "";

		// (1.14) Iterate through the file and read it line by line.
		while (reader.ready) { // ** YOUR CODE WHERE '?' **

			// (1.15) Append each line to StringBuilder.
            line = reader.readLine();
            bob.append(line);
		}

		// (1.16) Close BufferedReader.

        reader.close();

		// TODO (1.17) Return the final string containing the file content.

		// ** YOUR CODE HERE **
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

        int counter=0;

		// (1.20) Create a StringBuilder to store the formatted output before saving to a file.

        StringBuilder builder = new StringBuilder();

		// Iterate over the grouped anagrams (values of the map).
		for (SinglyLinkedList group : groups.values()) {

			// TODO (1.21) Ensure the group is not null and contains words before printing.
			if (group != null) {  // ** YOUR CODE WHERE '?' **

				// TODO (1.22) Format the group as a numbered entry and remove any extra spaces.

				// ** YOUR CODE HERE **

				// TODO (1.23) Print the formatted group to the console.

				// ** YOUR CODE HERE **

				// TODO (1.24) Append the formatted group to the output content for file saving.

				// ** YOUR CODE HERE **

				// TODO (1.25) Increment the counter for the next group.

				// ** YOUR CODE HERE **
			}
		}

		// ==========================
		// FILE OUTPUT HANDLING
		// ==========================

		// TODO (1.26) Save the final grouped anagrams to a text file with a modified filename based on the input file.

        File f = new File("out-"+inputFileName);

		// Initialize BufferedWriter for writing to the output file.
        BufferedWriter writer = new BufferedWriter(f);
		// TODO (1.27) Use try-with-resources to ensure BufferedWriter is closed automatically after writing.
		try { 

			// TODO (1.28) Write the final grouped anagrams output to the specified file.

			// ** YOUR CODE HERE **

			// TODO (1.29) Print a confirmation message indicating successful file saving.

			// ** YOUR CODE HERE **

			// (1.30) Handle any IOException that may occur during file writing.
		} catch (IOException e) { // ** YOUR CODE WHERE '?' **
			// (1.31) Print an error message to standard error (stderr) if file writing fails.
			e.printStackTrace(); // Print stack trace for debugging.
		}
	}
}

