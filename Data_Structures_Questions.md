Answer the following questions for each of the data structures you implemented as part of this project.

## Queue - FIFO data structure

1. What is the runtime complexity of `enqueue`?
O(n), we will add the item to the front of the array making all the indices have to shift one. If the array runs out of space we will also need to copy all the data to a new array twice as big which is O(n)

2. What is the runtime complexity of `dequeue`?
O(1), dequeue on the end is 'popped' off the end of the array making it a single operation

3. What is the runtime complexity of `len`?
len is an O(1) operation, in python len under the hood will keep track of all the items being added or removed from the list making the call a single operation when needed. In a queue data structure we can rely on len of the queue array or we can just add/decrement each item as its enqueued or dequeued.

## Binary Search Tree

1. What is the runtime complexity of `insert`?
O(log n) 

2. What is the runtime complexity of `contains`?
O(log n)

3. What is the runtime complexity of `get_max`? 
O(n), the max value will almost be the furthest item to right on the tree. When Looking for the max you will be basically going down a linked-list until we find the last value

## Heap

1. What is the runtime complexity of `_bubble_up`?
O(log n)

2. What is the runtime complexity of `_sift_down`?
O(log n)

3. What is the runtime complexity of `insert`?
best time: O(1) if the item is inserted is less than its parent
worst time: O(log n) if we have to insert then bubble up

4. What is the runtime complexity of `delete`?
O(log n), we will have to move the last item in the array to the first then sift_down

5. What is the runtime complexity of `get_max`?
O(1), it will be the first item in the array

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?


2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?