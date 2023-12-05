#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
int palindrome_check(listint_t **compare_head,
				listint_t *trav_head, int *check_flag);
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
	int check_flag = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	result  = palindrome_check(head, *head, &check_flag);

	return (result);
}


int	palindrome_check(listint_t **compare_head, listint_t *trav_head,
												 int *check_flag)
{
	if (trav_head == NULL)
		return (0);

	palindrome_check(compare_head, trav_head->next, check_flag);
	if (*check_flag == 0)
	{
		return (0);
	}
	/* Stop when two pointer equates*/

	if (*compare_head == trav_head)
	{
		*check_flag = 1;
		(*compare_head) = (*compare_head)->next;
		return (1);
	}
	if ((*compare_head)->n == trav_head->n)
	{
		(*compare_head) = (*compare_head)->next;
	}
	else
	{
		*check_flag = 0;
	}
	return (1);
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
