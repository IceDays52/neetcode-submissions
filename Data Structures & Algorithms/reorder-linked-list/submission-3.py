
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # KROK 1: Znajdź środek listy
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # KROK 2: Podziel listę na dwie połowy
        second = slow.next
        slow.next = None

        # KROK 3: Odwróć drugą połowę
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # KROK 4: Połącz obie połowy naprzemiennie
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
