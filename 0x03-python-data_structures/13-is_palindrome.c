#include "lists.h"
#include <stddef.h>

listint_t *reverse_list(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *mid, *second_half;
	int palindrome = 1;
	
	if (*head == NULL || (*head)->next == NULL)
		return 1;
	
	slow = *head;
	fast = *head;
	prev_slow = *head;
	mid = NULL;
	
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	
	second_half = reverse_list(&slow);
	palindrome = compare_lists(*head, second_half);
	second_half = reverse_list(&second_half);
	
	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}
	
	return palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;
	
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	
	*head = prev;
	return *head;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first list
 * @list2: pointer to the second list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;
		
		list1 = list1->next;
		list2 = list2->next;
	}
	return (list1 == NULL && list2 == NULL);
}
