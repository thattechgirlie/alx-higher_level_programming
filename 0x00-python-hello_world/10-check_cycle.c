#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - looks for cycle
 * @list: gives us a linked list
 * Return: returns 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	
	if (!list)
	{
		return (0);
	}
	while (slow && fast && fast ->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
