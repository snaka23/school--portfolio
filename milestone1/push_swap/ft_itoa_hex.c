/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_hex.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/10 22:50:20 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/28 17:08:01 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_utils.h"
#include <stdio.h>

static size_t	ft_countdigit(unsigned long n)
{
	size_t			count;

	count = 1;
	while (n / 16)
	{
		count++;
		n /= 16;
	}
	return (count);
}

static void	ft_minuscase(int *sign, long *n)
{
	*sign = -1;
	*n = *n * -1;
}

char	*ft_itoa_hexa(long n, const char *hex)
{
	int		sign;
	size_t	digit;
	char	*str;

	sign = 1;
	digit = ft_countdigit(n);
	if (n < 0)
		ft_minuscase(&sign, &n);
	str = (char *)malloc(sizeof(char) * (digit + 1));
	if (!str)
		return (NULL);
	if (sign < 0)
		str[0] = '-';
	if (n == 0)
		str[0] = '0';
	str[digit] = '\0';
	while (n > 0)
	{
		str[--digit] = hex[n % 16];
		n /= 16;
	}
	return (str);
}

char	*ft_itoa_ptr(unsigned long n, const char *hex)
{
	size_t	digit;
	char	*str;

	digit = ft_countdigit(n);
	digit += 2;
	str = (char *)malloc(sizeof(char) * (digit + 1));
	if (!str)
		return (NULL);
	str[0] = '0';
	str[1] = 'x';
	str[digit] = '\0';
	while (n > 0)
	{
		str[--digit] = hex[n % 16];
		n /= 16;
	}
	return (str);
}
