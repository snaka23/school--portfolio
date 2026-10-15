/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 17:17:54 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/01 23:14:16 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "operations.h"

int	min_value(t_stack *stc)
{
	int	val;

	val = stc->value;
	stc = stc->next;
	while (stc)
	{
		if (val > stc->value)
			val = stc->value;
		stc = stc->next;
	}
	return (val);
}

size_t	min_position(t_stack *a)
{
	int		min;
	size_t	pos;

	min = min_value(a);
	pos = 0;
	while (a)
	{
		if (min == a->value)
			break ;
		pos++;
		a = a->next;
	}
	return (pos);
}

void	a_move_min_top(t_pushswap *ps)
{
	size_t	pos;

	pos = min_position(ps->a);
	while (pos != 0)
	{
		if (pos <= stack_size(ps->a) / 2)
			ra(ps);
		else
			rra(ps);
		pos = min_position(ps->a);
	}
}

int	max_value(t_stack *stc)
{
	int	val;

	val = stc->value;
	stc = stc->next;
	while (stc)
	{
		if (val < stc->value)
			val = stc->value;
		stc = stc->next;
	}
	return (val);
}

size_t	max_position(t_stack *stc)
{
	size_t	pos;
	int		max;

	max = max_value(stc);
	pos = 0;
	while (stc)
	{
		if (max == stc->value)
			break ;
		pos++;
		stc = stc->next;
	}
	return (pos);
}
