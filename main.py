from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations like insertion,
    recursion-based sum, search, and reverse.
    """
    # TODO: 1) Create a LinkedList instance
    ll = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    # Example IDs
    sample_ids = [101, 202, 303, 404, 505]
    for id_value in sample_ids:
        ll.insert_at_end(id_value)

    # TODO: 3) Display the list to verify insertion
    print("Original list:")
    ll.display()

    # TODO: 4) Call recursive_sum and print the result
    total = ll.recursive_sum()
    print(f"Sum of all IDs (recursive_sum): {total}")

    # TODO: 5) Call recursive_search with a target and print result
    target = 303
    found = ll.recursive_search(target)
    print(f"Searching for {target} (recursive_search): {found}")

    missing_target = 999
    missing_found = ll.recursive_search(missing_target)
    print(f"Searching for {missing_target} (recursive_search): {missing_found}")

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print("Reversing list with recursive_reverse...")
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()
