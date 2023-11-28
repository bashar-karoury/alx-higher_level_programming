#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to head node
 * @number: number to be inserted
 *
 * Return: pointer to newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *trav, *prev = NULL, *next;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		*head = new;
		return (new);
	}

	trav = *head;
	while ((trav != NULL) && (trav->n < number))
	{
		prev = trav;
		trav = trav->next;
	}

	next = trav;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = next;
	}
	return (new);
}
