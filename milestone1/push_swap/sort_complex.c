/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_complex.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 15:50:39 by snakagaw          #+#    #+#             */
/*   Updated: 2026/06/02 23:21:27 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "operations.h"
#include "sort_utils.h"

static int	max_bits(t_stack *a)
{
	int	count;
	int	max_value;

	max_value = a->index;
	count = 0;
	while (a)
	{
		if (max_value < a->index)
			max_value = a->index;
		a = a->next;
	}
	while (max_value > 0)
	{
		max_value = max_value / 2;
		count++;
	}
	return (count);
}

void	radix_sort(t_pushswap *ps)
{
	int	i;
	int	size;
	int	bits;

	bits = max_bits(ps->a);
	i = 0;
	while (i < bits)
	{
		size = stack_size(ps->a);
		while (size)
		{
			if (((ps->a)->index >> i) & 1)
				ra(ps);
			else
				pb(ps);
			size--;
		}
		while (ps->b)
		{
			pa(ps);
		}
		i++;
	}
}
