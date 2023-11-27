#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head node of list
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{

	listint_t *temp = list;

	while (temp != NULL)
	{
		if(temp->f == 1)
		{	
			return(1);
		}
		temp->f = 1;
		temp = temp->next;
	}
	return (0);
}
