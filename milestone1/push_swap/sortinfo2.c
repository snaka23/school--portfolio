/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sortinfo2.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 17:28:49 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/28 19:36:09 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sortinfo.h"

double	compute_disorder(t_stack *a)
{
	size_t	i;
	size_t	j;
	double	mistakes;
	double	total_pairs;

	i = 0;
	j = 0;
	mistakes = 0;
	total_pairs = 0;
	while (i < stack_size(a))
	{
		j = i + 1;
		while (j < stack_size(a))
		{
			total_pairs++;
			if (stack_at(a, i)->value > stack_at(a, j)->value)
				mistakes++;
			j++;
		}
		i++;
	}
	return (mistakes / total_pairs);
}

void	set_disorder(t_sortinfo *info, double disorder)
{
	info->disorder = disorder;
}

double	get_disorder(t_sortinfo info)
{
	return (info.disorder);
}

char	*get_order_str(t_strategy strategy)
{
	char	*order;

	order = NULL;
	if (strategy == SIMPLE)
		order = "O(n²)";
	else if (strategy == MEDIUM)
		order = "O(n√n)";
	else if (strategy == COMPLEX)
		order = "O(n log n)";
	return (order);
}

char	*get_requested_str(t_sortinfo info)
{
	char	*reqstr;

	reqstr = NULL;
	if (info.requested == SIMPLE)
		reqstr = "Simple";
	else if (info.requested == MEDIUM)
		reqstr = "Medium";
	else if (info.requested == COMPLEX)
		reqstr = "Complex";
	else if (info.requested == ADAPTIVE)
		reqstr = "Adaptive";
	return (reqstr);
}
