#include lists.h

/**
* check_cycle - Will look for cilces in linked lists
* @list: Pointer to a list
* Return: 0 if no clycle is found, otherwise return 1
**/

int check_cycle(listint_t *list)
{
	listint_t *fast_gel;
	listint_t *slow_motion;

	fast_gel = list;
	slow_motion = list;

	while (fast_gel && slow_motion && slow_motion->next)
	{
		fast_gel = fast_gel->next;
		slow_motion = slow_motion->next->next;
		if (fast_gel == slow_motion)
			return (1);
	}
	return (0);
}