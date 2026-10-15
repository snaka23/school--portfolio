/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sortinfo3.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 17:33:51 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/02 15:11:38 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_stderr.h"
#include "sortinfo.h"
#include "utils.h"
#include <unistd.h>

void	set_current_op(t_sortinfo *info, t_ops op)
{
	info->current_op = op;
}

t_ops	get_current_op(t_sortinfo info)
{
	return (info.current_op);
}

void	increment_opscnt(t_sortinfo *info, t_ops ops)
{
	info->total_ops++;
	info->opscnt[ops]++;
}

void	put_sortinfo(t_sortinfo info)
{
	ft_printf_stderr("[bench] disorder:  %f%\n", info.disorder * 100);
	ft_printf_stderr("[bench] strategy:  %s / %s\n", get_requested_str(info),
		get_order_str(info.selected));
	ft_printf_stderr("[bench] total_ops: %d\n", info.total_ops);
	ft_printf_stderr("[bench] sa: %d  sb: %d  ss: %d  pa: %d  pb: %d\n",
		info.opscnt[SA], info.opscnt[SB], info.opscnt[SS], info.opscnt[PA],
		info.opscnt[PB]);
	ft_printf_stderr("[bench] ra: %d  rb: %d  rr: %d ",
		info.opscnt[RA], info.opscnt[RB], info.opscnt[RR]);
	ft_printf_stderr("rra: %d rrb: %d  rrr:%d\n",
		info.opscnt[RRA], info.opscnt[RRB], info.opscnt[RRR]);
	return ;
}
