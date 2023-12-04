#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
return (1);
return (ch_palindrome(head, *head));
}
/**
 * ch_palindrome - to check list if palindrome
 * @head: head of list to check
 * @end: end of list to check
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int ch_palindrome(listint_t **head, listint_t *end)
{
if (end == NULL)
return (1);
if (ch_palindrome(head, end->next) && (*head)->n == end -> n)
{
*head = (*head)->next;
return (1);
}
return (0);
}
