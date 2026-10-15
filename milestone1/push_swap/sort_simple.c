/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_simple.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 18:44:49 by snakagaw          #+#    #+#             */
/*   Updated: 2026/06/01 23:11:26 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "operations.h"
#include "sort_utils.h"

void	simple_sort(t_pushswap *ps)
{
	while (ps->a)
	{
		a_move_min_top(ps);
		pb(ps);
	}
	while (ps->b)
		pa(ps);
}
