#include "lists.h" 
/** 
* check_cycle - checks cycles 
* @list: list 
* Return: 1 0r 0 
*/ 
int check_cycle(listint_t *list) 
{
listint_t *slow, *fast;
if (list == NULL)
return (0);

if( list->next == NULL)
return (0);

slow = list;
fast = list;
while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if(slow == fast)
return (1);
}
return (0);
}
