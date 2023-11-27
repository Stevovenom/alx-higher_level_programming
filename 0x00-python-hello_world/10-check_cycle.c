#include "lists.h"

/**
 * check_cycle - the function  checks if the singly linked list has a cycle
 * @list: its pointer to the head node of the singly linked list
 * Return: 1 for success and 0 is no cycle in the singly linked list
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (list == NULL || list->next == NULL)
		return (0);
	slow_ptr = list;
	fast_ptr = list->next;
	while (slow_ptr != fast_ptr)
	{
		if (fast_ptr == NULL || fast_ptr->next == NULL)
			return (0);
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	return (1);
}
