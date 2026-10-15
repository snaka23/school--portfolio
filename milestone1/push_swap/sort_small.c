/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 18:43:12 by snakagaw          #+#    #+#             */
/*   Updated: 2026/06/01 23:08:03 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "operations.h"
#include "sort_utils.h"

void	sort_three(t_pushswap *ps)
{
	int	max;

	max = max_value(ps->a);
	if ((ps->a)->value == max)
		ra(ps);
	else if ((ps->a)->next->value == max)
		rra(ps);
	if ((ps->a)->value > (ps->a)->next->value)
		sa(ps);
}

void	sort_five(t_pushswap *ps)
{
	while (stack_size(ps->a) > 3)
	{
		a_move_min_top(ps);
		pb(ps);
	}
	sort_three(ps);
	while (ps->b)
		pa(ps);
}
