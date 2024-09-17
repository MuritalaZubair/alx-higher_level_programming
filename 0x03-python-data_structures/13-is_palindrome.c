#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *first_half;
	listint_t *temp;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse_list(slow);
	first_half = *head;

	temp = second_half;

	while (temp != NULL)
	{
		if (first_half->n != temp->n)
		{
			result = 0;
			break;
		}
		first_half = first_half->next;
		temp = temp->next;
	}

	reverse_list(second_half); /* Optional: Restore the list */

	return (result);
}
