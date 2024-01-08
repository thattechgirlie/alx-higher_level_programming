#include "lists.h"
/**
 * reverse_listint - this is the main code
 * @head: this is the beginning of the list
 * Return: returns value
 */
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current)
{
	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
}
*head = prev;
}
