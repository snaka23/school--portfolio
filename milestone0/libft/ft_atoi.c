/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/01 16:04:51 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/07 16:00:42 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *nptr)
{
	int		sign;
	long	value;

	while ((9 <= *nptr && *nptr <= 13) || *nptr == 32)
		nptr++;
	sign = 1;
	if (*nptr == '+' || *nptr == '-')
	{
		if (*nptr == '-')
			sign = -sign;
		nptr++;
	}
	value = 0;
	while ('0' <= *nptr && *nptr <= '9')
	{
		value = value * 10 + (*nptr - '0');
		nptr++;
	}
	return ((int)(sign * value));
}
