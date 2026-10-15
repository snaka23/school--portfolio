/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sortinfo.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 19:59:36 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/01 22:27:25 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sortinfo.h"
#include "utils.h"

void	init_sort_info(t_sortinfo *info)
{
	int	i;

	i = 0;
	info->disorder = 0;
	info->requested = NONE;
	info->selected = NONE;
	info->total_ops = 0;
	while (i < 11)
		info->opscnt[i++] = 0;
	return ;
}

int	set_requested_strategy(t_sortinfo *info, t_strategy strategy)
{
	if (info->requested == NONE)
	{
		info->requested = strategy;
		return (1);
	}
	if (info->requested != strategy)
		return (0);
	return (1);
}

int	get_requested_strategy(t_sortinfo info)
{
	return (info.requested);
}

void	set_selected_strategy(t_sortinfo *info)
{
	if (info->requested == ADAPTIVE)
	{
		if (info->disorder < 0.2)
			info->selected = SIMPLE;
		else if (info->disorder < 0.5)
			info->selected = MEDIUM;
		else
			info->selected = COMPLEX;
	}
	else
		info->selected = info->requested;
	return ;
}

int	get_selected_strategy(t_sortinfo info)
{
	return (info.selected);
}
