/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/29 13:08:46 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/01 23:16:30 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"
#include "operations.h"

static int	is_sorted(t_stack *stc)
{
	if (stc == NULL)
		return (1);
	if (!(stc->next))
		return (1);
	while (stc->next)
	{
		if (stc->value > stc->next->value)
			return (0);
		stc = stc->next;
	}
	return (1);
}

static void	ft_strategic_sort(t_pushswap *ps)
{
	t_strategy	stra;

	stra = get_selected_strategy(ps->info);
	if (stra == SIMPLE)
		simple_sort(ps);
	else if (stra == MEDIUM)
		chunk_sort(ps);
	else if (stra == COMPLEX)
		radix_sort(ps);
	return ;
}

void	ft_sort(t_pushswap *ps)
{
	int		size;

	if (is_sorted(ps->a))
		return ;
	set_disorder(&ps->info, compute_disorder(ps->a));
	set_selected_strategy(&ps->info);
	size = stack_size(ps->a);
	if (size <= 5)
	{
		if (size == 2)
			sa(ps);
		else if (size == 3)
			sort_three(ps);
		else
			sort_five(ps);
		return ;
	}
	else
		ft_strategic_sort(ps);
	return ;
}
