#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - nserts a number into a sorted singly linked list
 * @head: the head of list
 * @number: the number to insert
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
if (node == NULL || new->n <= node->n)
{
new->next = node;
new = *head;
return (new);
}
while (node)
{
if (node->next == NULL || new->n < node->next->n)
{
new->next = node->next;
node->next = new;
return (node);
}
node = node->next;
}
return (NULL);
}
