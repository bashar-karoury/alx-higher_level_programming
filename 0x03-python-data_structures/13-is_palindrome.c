#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head node
 *
 * Return: 0 if it is not a palindrome, 1 it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *trav_node = *head;
	listint_t *reverse = NULL;
	int result = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);


	/* traverse to last node and copy in reverse order*/
	while (trav_node != NULL)
	{
		add_nodeint_begin(&reverse, trav_node->n);
		trav_node = trav_node->next;
	}

	trav_node = *head;
	/* now compare *head with reverse */
	while (trav_node != NULL)
	{
		if (trav_node->n != reverse->n)
		{
			result = 0;
			break;
		}

		trav_node = trav_node->next;
		reverse = reverse->next;
	}

	free_listint(reverse);
	return (result);
}
/**
 * add_nodeint_begin - adds a new node at the beginning of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_begin(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

