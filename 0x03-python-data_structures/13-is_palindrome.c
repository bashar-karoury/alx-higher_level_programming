#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

listint_t *get_node_at_index(listint_t *head, int index);
int list_length(listint_t *head);
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head node
 *
 * Return: 0 if it is not a palindrome, 1 it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int result = 1;
	int list_len = 0;
	int i = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	list_len = list_length(*head);

	for (i = 0; i < list_len / 2; i++)
	{
		listint_t *first = get_node_at_index(*head, i);
		listint_t *second = get_node_at_index(*head, list_len - i - 1);

		if (first->n != second->n)
		{	result = 0;
			break;
		}
	}

	return (result);
}

/**
 * get_node_at_index - returns node pointer at specific index
 * @head: pointer to head node of list
 * @index: index at which node should be returned
 *
 * Return: node at index, NULL if failed
 */
listint_t *get_node_at_index(listint_t *head, int index)
{
	int idx = 0;

	if (index < 0)
		return (NULL);

	while (head != NULL && idx < index)
	{
		head = head->next;
		idx++;
	}

	if (idx == index)
		return (head);
	else
		return (NULL);
}

/**
 * list_length - calculate length of list
 * @head: head node pointer
 *
 * Return: length of list as int
 */
int list_length(listint_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		head = head->next;
		len++;
	}
	return (len);
}
