/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sortinfo.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 19:58:10 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/02 15:11:45 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SORTINFO_H
# define SORTINFO_H

# include "stack.h"

typedef enum e_strategy
{
	NONE,
	SIMPLE,
	MEDIUM,
	COMPLEX,
	ADAPTIVE
}					t_strategy;

typedef enum e_ops
{
	SA,
	SB,
	SS,
	PA,
	PB,
	RA,
	RB,
	RR,
	RRA,
	RRB,
	RRR
}					t_ops;

typedef struct s_sortinfo
{
	double			disorder;
	t_strategy		requested;
	t_strategy		selected;
	t_ops			current_op;
	int				total_ops;
	int				opscnt[11];
}					t_sortinfo;

void				init_sort_info(t_sortinfo *info);
int					set_requested_strategy(t_sortinfo *info,
						t_strategy strategy);
int					get_requested_strategy(t_sortinfo info);
void				set_selected_strategy(t_sortinfo *info);
int					get_selected_strategy(t_sortinfo info);
double				compute_disorder(t_stack *a);
void				set_disorder(t_sortinfo *info, double disorder);
double				get_disorder(t_sortinfo info);
char				*get_order_str(t_strategy strategy);
char				*get_requested_str(t_sortinfo info);
void				set_current_op(t_sortinfo *info, t_ops op);
t_ops				get_current_op(t_sortinfo info);
void				increment_opscnt(t_sortinfo *info, t_ops ops);
void				put_sortinfo(t_sortinfo info);

#endif