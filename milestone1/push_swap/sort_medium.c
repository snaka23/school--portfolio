/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_medium.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 17:29:02 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/02 23:23:24 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "operations.h"
#include "push_swap.h"
#include "sort_utils.h"

static void	b_move_max_top(t_pushswap *ps)
{
	size_t	pos;

	pos = max_position(ps->b);
	while (pos != 0)
	{
		if (pos <= stack_size(ps->b) / 2)
			rb(ps);
		else
			rrb(ps);
		pos = max_position(ps->b);
	}
}

static int	get_chunk_size(t_stack *a)
{
	int	size;
	int	i;

	size = stack_size(a);
	i = 1;
	while (i * i <= size)
		i++;
	i--;
	if (i == 0)
		i = 1;
	return (i);
}

static void	push_chunks(t_pushswap *ps,
	int *chunk_limit, int *count, int chunk_size)
{
	if ((ps->a)->index < *chunk_limit)
	{
		pb(ps);
		(*count)++;
	}
	else
		ra(ps);
	if (*count >= chunk_size)
	{
		*chunk_limit += chunk_size;
		*count = 0;
	}
}

static void	restore_stack(t_pushswap *ps)
{
	while (ps->b)
	{
		b_move_max_top(ps);
		pa(ps);
	}
}

void	chunk_sort(t_pushswap *ps)
{
	int	chunk_size;
	int	chunk_limit;
	int	count;

	chunk_size = get_chunk_size(ps->a);
	chunk_limit = chunk_size;
	count = 0;
	while (ps->a)
		push_chunks(ps, &chunk_limit, &count, chunk_size);
	restore_stack(ps);
}
