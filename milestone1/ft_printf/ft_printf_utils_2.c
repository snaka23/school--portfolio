/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils_2.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 17:23:17 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/13 17:23:28 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	put_nbr_hex(unsigned long long size, char *hex)
{
	int	count;
	int	res;

	count = 0;
	if (size > 15)
	{
		res = put_nbr_hex(size / 16, hex);
		if (res == -1)
			return (-1);
		count = res;
	}
	if (write(1, &hex[size % 16], 1) == -1)
		return (-1);
	return (count + 1);
}

int	ft_printf_ptr(void *ptr)
{
	unsigned long long	size;
	char				*hex;
	int					res;

	hex = "0123456789abcdef";
	if (ptr == NULL)
	{
		if (write(1, "(nil)", 5) == -1)
			return (-1);
		return (5);
	}
	if (write(1, "0x", 2) == -1)
		return (-1);
	size = (unsigned long long)ptr;
	res = put_nbr_hex(size, hex);
	if (res == -1)
		return (-1);
	return (res + 2);
}

int	ft_printf_hex_low(unsigned int nb)
{
	int		count;
	char	*hex;

	hex = "0123456789abcdef";
	count = put_nbr_hex((unsigned long long)nb, hex);
	return (count);
}

int	ft_printf_hex_upp(unsigned int nb)
{
	int		count;
	char	*hex;

	hex = "0123456789ABCDEF";
	count = put_nbr_hex((unsigned long long)nb, hex);
	return (count);
}
