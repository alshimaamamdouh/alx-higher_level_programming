#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node 
 * @head: input pointer
 * @number: number to insert
 * Return: node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = *head, *new_node = malloc(sizeof(listint_t));
if(!new_node)
return (NULL);

new_node->n = number;
if (*head == NULL || (*head)->n >= new_node->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

while (temp->next != NULL && temp->next->n < new_node->n)
temp = temp->next;

new_node->next = temp->next;
temp->next = new_node;
return (new_node);
}
