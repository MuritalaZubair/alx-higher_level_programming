#include "lists.h"
#include <stddef.h>

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;
	int result = 1;

	if (!head || !*head || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast)
		slow = slow->next;

	while (prev && slow)
	{
		if (prev->n != slow->n)
		{
			result = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}

	return (result);
}
