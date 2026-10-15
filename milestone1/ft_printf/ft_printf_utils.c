/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 17:22:41 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/13 17:22:57 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf_char(int c)
{
	unsigned char	ch;

	ch = (unsigned char)c;
	if (write(1, &ch, 1) == -1)
		return (-1);
	return (1);
}

int	ft_printf_str(const char *str)
{
	int	count;

	if (!str)
	{
		if (write(1, "(null)", 6) == -1)
			return (-1);
		return (6);
	}
	count = 0;
	while (str[count])
	{
		if (write(1, &str[count], 1) == -1)
			return (-1);
		count++;
	}
	return (count);
}

int	ft_printf_nbr(int nb)
{
	char	c;
	int		count;
	int		res;

	if (nb == -2147483648)
		return (write(1, "-2147483648", 11));
	count = 0;
	if (nb < 0)
	{
		if (write(1, "-", 1) == -1)
			return (-1);
		nb = -nb;
		count = 1;
	}
	if (nb > 9)
	{
		res = ft_printf_nbr(nb / 10);
		if (res == -1)
			return (-1);
		count = count + res;
	}
	c = nb % 10 + '0';
	if (write(1, &c, 1) == -1)
		return (-1);
	return (count + 1);
}

int	ft_printf_unbr(unsigned int nb)
{
	char	c;
	int		count;
	int		res;

	count = 0;
	if (nb > 9)
	{
		res = ft_printf_unbr(nb / 10);
		if (res == -1)
			return (-1);
		count = res;
	}
	c = nb % 10 + '0';
	if (write(1, &c, 1) == -1)
		return (-1);
	return (count + 1);
}
