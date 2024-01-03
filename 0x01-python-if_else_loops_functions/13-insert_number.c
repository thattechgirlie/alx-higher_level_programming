#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - check the main code
 * @head: points to head of list
 * @number: gives us number 
 * Return: returns 0 or 1
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *new;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return(NULL);
	new->n = number;

	if (nd == NULL || nd->n >= number)
	{
		new->next = nd;
		*head = new;
		return (new);
	}
	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;
	new->next = nd->next;
	nd->next = new;

	return (new);
}
