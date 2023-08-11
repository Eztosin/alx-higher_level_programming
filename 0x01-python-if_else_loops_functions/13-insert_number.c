#include "lists.h"

/**
* insert_node- inserts a number in sorted singly linked list.
* @head: double pointer that points to the firt node of list.
* @number:number to insert.
* Return: pointer to new node or NULL if it fails.
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *newptr, *ch;
newptr = malloc(sizeof(listint_t));

if (newptr == NULL)
{
return (NULL);
}
newptr->n = number;

if (*head == NULL || number < ((*head)->n))
{
newptr->next = *head;
*head = newptr;
}
else
{
ch = *head;
while (ch->next != NULL && ch->next->n <= number)
{
ch = ch->next;
}
newptr->next = ch->next;
ch->next = newptr;
}
return (newptr);
}
