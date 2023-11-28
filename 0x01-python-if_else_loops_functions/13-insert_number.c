#include "lists.h"
/**
 * insert_node - its pointer to insert a number into the singly linked list
 * @head: pointer to pointer to the head of the linnked list
 * @number: the value to be inserted
 * Return: address to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	
	if (new_node == NULL)
		return (NULL);
	
	new_node->n = number;
	new_node->next = NULL;
	
	if (*head == NULL || number < current->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	
	new_node->next = current->next;
	current->next = new_node;
	
	return (new_node);
}
