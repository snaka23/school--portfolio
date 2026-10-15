/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 11:15:25 by snakagaw          #+#    #+#             */
/*   Updated: 2026/06/04 14:59:59 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "sort.h"
#include "utils.h"
#include <stdlib.h>
#include <unistd.h>

static int	ft_duplicate(t_stack *stk, int data)
{
	while (stk)
	{
		if (stk->value == data)
			return (0);
		stk = stk->next;
	}
	return (1);
}

static int	parse_flag(t_pushswap *ps, char *arg)
{
	if (ft_strcmp(arg, "--bench") == 0)
		ps->bench = 1;
	else if (ft_strcmp(arg, "--simple") == 0)
		return (set_requested_strategy(&ps->info, SIMPLE));
	else if (ft_strcmp(arg, "--medium") == 0)
		return (set_requested_strategy(&ps->info, MEDIUM));
	else if (ft_strcmp(arg, "--complex") == 0)
		return (set_requested_strategy(&ps->info, COMPLEX));
	else if (ft_strcmp(arg, "--adaptive") == 0)
		return (set_requested_strategy(&ps->info, ADAPTIVE));
	else
		return (-1);
	return (1);
}

static int	parse_flag_loop(t_pushswap *ps, char **argv, int size)
{
	int	arg_i;
	int	ret;

	arg_i = 1;
	while (arg_i < size)
	{
		ret = parse_flag(ps, argv[arg_i]);
		if (ret == 0)
			return (-1);
		if (ret == -1)
			break ;
		arg_i++;
	}
	if (get_requested_strategy(ps->info) == NONE)
		set_requested_strategy(&ps->info, ADAPTIVE);
	return (arg_i);
}

int	ft_parse(t_pushswap *ps, char **argv, int size)
{
	int		ret;
	int		arg_i;
	int		data;
	t_stack	*new;

	arg_i = parse_flag_loop(ps, argv, size);
	if (arg_i == -1)
		return (0);
	while (arg_i < size)
	{
		data = ft_safe_atoi(argv[arg_i++], &ret);
		if (ret == -1)
			return (0);
		if (!ft_duplicate(ps->a, data))
			return (0);
		new = stack_new(data);
		if (!new)
			return (0);
		stackadd_back(&ps->a, new);
	}
	assign_index(ps->a);
	return (1);
}
