public class SinglyLinkedList<T extends Comparable<T>> implements ListInterface<T> {
    private Node<T> head; // Refers to the head of the linked list
    private Node<T> current; // Used for the getNext method (Iterator)
    // private int size = 0;

    private static class Node<T> {
        /*
         * T data : Stores data for each node
         * Node<T> next : Stores a reference to the next node
         */
        T data;
        Node<T> next;

        // Constructor -> Next Node = NULL when created
        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    // Constructor
    public SinglyLinkedList() {
        head = null;
        current = null;
    }

    @Override
    public boolean isEmpty() {
        return head == null;
    }

    @Override
    public boolean isFull() {
        // This is unnecessary for a linked list but required by the interface.
        return false;
    }

    @Override
    public int size() {
        int count = 0;
        Node<T> temp = head;
        while (temp != null) {
            count++;
            temp = temp.next;
        }
        return count;

        // return size
    }

    @Override
    public void clear() {
        head = null;
        current = null;
        // size = 0;

        // head.next = null;
        // current.next = null;
    }

    @Override
    public void reset() {
        current = head;
    }

    @Override
    public T getNext() {
        if (current == null) return null;
        T data = current.data;
        current = current.next;
        return data;
    }

    @Override
    public void add(T element) {
        Node<T> newNode = new Node<>(element);
        if (isEmpty()) {
            head = newNode;
        } else {
            Node<T> temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
        // size++;
    }

    @Override
    public int contains(T element) {
        Node<T> temp = head;
        int index = 0;
        while (temp != null) {
            if (temp.data.equals(element)) {
                return index;
            }
            temp = temp.next;
            index++;
        }
        return -1;
    }

    @Override
    public void remove(T element) {
        if (isEmpty()) return;
        if (head.data.equals(element)) {
            head = head.next;
            // size--;
            return;
        }
        Node<T> temp = head;
        while (temp.next != null) {
            if (temp.next.data.equals(element)) {
                temp.next = temp.next.next;
                // size--;
                return;
            }
            temp = temp.next;
        }
    }

    @Override
    public void sort() {
        // Implement sorting logic here
    }

    // @Override
    // public void sort() {
    //     boolean swapped;
    //     Node<T> ptr1;
    //     Node<T> lptr = null;

    //     if (head == null)
    //         return;

    //     do {
    //         swapped = false;
    //         ptr1 = head;

    //         while (ptr1.next != lptr) {
    //             if (ptr1.data.compareTo(ptr1.next.data) > 0) {
    //                 T temp = ptr1.data;
    //                 ptr1.data = ptr1.next.data;
    //                 ptr1.next.data = temp;
    //                 swapped = true;
    //             }
    //             ptr1 = ptr1.next;
    //         }
    //         lptr = ptr1;
    //     } while (swapped);
    // }

    public void printList() {
        Node<T> current = head; // Start from the head of the list
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next; // Move to the next node
        }
        System.out.println("null"); // Indicate the end of the list
    }

    // Helper method to print the list
    private static void printList(SinglyLinkedList<Integer> list) {
        list.reset();
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.getNext() + " -> ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        SinglyLinkedList<Integer> list = new SinglyLinkedList<>();

        // Check if the list is empty
        System.out.println("Is the list empty? " + list.isEmpty());

        // Adding elements to the list
        list.add(10);
        list.add(20);
        list.add(30);
        list.add(40);

        // Checking the size of the list
        System.out.println("Size of the list: " + list.size());

        // Check if the list contains a specific element
        int containsElement = 20;
        int index = list.contains(containsElement);
        if (index != -1) {
            System.out.println("List contains " + containsElement + " at index: " + index);
        } else {
            System.out.println("List does not contain " + containsElement);
        }

        // Removing an element
        list.remove(20);
        System.out.println("Removed 20 from the list. New size: " + list.size());

        // Resetting and getting next element
        list.reset();
        System.out.println("Getting elements using getNext:");
        Integer element;
        while ((element = list.getNext()) != null) {
            System.out.println(element);
        }

        System.out.println("The linked list contains:");
        list.printList();
        printList(list);

        // Clearing the list
        list.clear();
        System.out.println("Cleared the list. Is it empty now? " + list.isEmpty());
    }
}