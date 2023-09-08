#include "lists.h"

int is_palindrome(listint_t **head)
{
  int count = 1;
  listint_t *ptr1, *ptr2, *ptr3, *ptr4, *ptr5;
  ptr1 = *head;
  ptr2 = *head;
  ptr3 = *head;
  ptr5 = NULL;

  /* Find the middle node and split the list in two */
  while (ptr2 != NULL && fast->next != NULL)
    {
      ptr2 = ptr2->next->next;
      ptr3 = ptr1;
      ptr1 = ptr1->next;
    }
  /* If the list has an odd number of elements, skip the middle node */
  if (ptr2 != NULL)
    {
      ptr5 = ptr1;
      ptr1 = ptr->next;
    }
  /* Reversing the second half of the list */
  ptr4 = ptr1;
  ptr3->next = NULL;

  
