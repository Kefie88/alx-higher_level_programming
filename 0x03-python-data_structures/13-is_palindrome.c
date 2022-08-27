#include "lists.h"
/**
 * is_palindrome - checks if a single linked list is a palindrome
 * @head: doublevpointer to list
 * Return: 1 if palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	return (checkPalindrome(head, *head));
}
/**
 * checkpalindrome - recursive function to check if list is a palindrome
 * @headptr: double pointer to list
 * @tptr: pointer to list
 * Return: 1 or 0
 */
int checkPalindrome(listint_t **headptr, listint_t *tptr)
{
	int ret;

	if (tptr == NULL)
		return (1);
	ret = checkPalindrome(headptr, tptr->next) && ((*headptr)->n == tptr->n);
	return (ret);
}
