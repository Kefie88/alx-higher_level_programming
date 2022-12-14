#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
       	unsigned int n;

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}
/**
 * add_nodeint_end - adds a new node at the end of a list
 * @head: pointer to the first node pointer
 * @n: integer to be included in the new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}
	return (new);
}
/**
 * free_listint - frees a list
 * @head: pointer to the list to be freed
 * Return: nothing (void)
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
 /**
  * add_nodeint - adds a  new node at the begginning of a listint_t list
  * @head: first node address
  * @n: integer to insert into the new node
  * Return: address of the new element or NULL if it fails
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	
	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);
	tmp->number = number;
	tmp->next = *head;
	*head = tmp;
	return (*head);
