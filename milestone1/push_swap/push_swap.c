/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 18:14:51 by snakagaw          #+#    #+#             */
/*   Updated: 2026/06/04 14:49:07 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "parse.h"
#include "sort.h"
#include <unistd.h>

static void	init_pushswap(t_pushswap *ps)
{
	ps->a = NULL;
	ps->b = NULL;
	init_sort_info(&ps->info);
	ps->bench = 0;
}

int	main(int argc, char **argv)
{
	int			parseflg;
	t_pushswap	ps;

	if (argc == 1)
		return (0);
	init_pushswap(&ps);
	parseflg = ft_parse(&ps, argv, argc);
	if (!parseflg)
	{
		stack_free(ps.a);
		write(2, "ERROR\n", 6);
		return (1);
	}
	ft_sort(&ps);
	if (ps.bench)
		put_sortinfo(ps.info);
	stack_free(ps.a);
	return (0);
}
