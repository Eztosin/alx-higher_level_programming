#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list: list to check
* Return: 0 if there is no cycly, 1 if there is.
*/

int check_cycle(listint_t *list)
{
listint_t *ptr1, *ptr2;
if (!list || !list->next)
{
return (0);
}
ptr1 = list;
ptr2 = list->next;

while (ptr2 && ptr2->next)
{
if (ptr1 == ptr2)
{
return (1);
}
ptr1 = ptr1->next;
ptr2 = ptr2->next->next;
}
return (0);
}
