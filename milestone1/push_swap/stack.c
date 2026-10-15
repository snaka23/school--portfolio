/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 16:58:31 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/27 13:05:24 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

t_stack	*stack_new(int data)
{
	t_stack	*res;

	res = (t_stack *)malloc(sizeof(t_stack));
	if (!res)
		return (NULL);
	res->value = data;
	res->next = NULL;
	return (res);
}

void	stackadd_back(t_stack **stc, t_stack *new)
{
	t_stack	*ptr;

	if (!stc || !new)
		return ;
	if (!*stc)
	{
		*stc = new;
		new->next = NULL;
		return ;
	}
	ptr = *stc;
	while (ptr->next)
		ptr = ptr->next;
	ptr->next = new;
}

void	assign_index(t_stack *a)
{
	int		count;
	int		target_value;
	t_stack	*ptr;
	t_stack	*start;

	start = a;
	while (a)
	{
		count = 0;
		target_value = a->value;
		ptr = start;
		while (ptr)
		{
			if (target_value > ptr->value)
				count++;
			ptr = ptr->next;
		}
		a->index = count;
		a = a->next;
	}
}

void	stack_free(t_stack *a)
{
	t_stack	*ptr;

	while (a)
	{
		ptr = a->next;
		free(a);
		a = ptr;
	}
}
