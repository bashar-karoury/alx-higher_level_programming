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
	listint_t *trav = list;
	int result = 0;

	while (temp != NULL)
	{
		trav = list;
		while (trav != temp)
		{
			if (temp->next == trav)
			{
				result = 1;
				return (result);
			}
			trav = trav->next;
		}
		temp = temp->next;
	}
	return (result);
}
