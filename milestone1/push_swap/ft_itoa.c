/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/10 22:50:20 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/13 21:14:38 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_itoa.h"
#include "ft_printf_utils.h"

static size_t	ft_countdigit(long n)
{
	size_t			count;

	count = 1;
	if (n < 0)
	{
		n = -n;
		count++;
	}
	while (n / 10)
	{
		count++;
		n /= 10;
	}
	return (count);
}

static void	ft_minuscase(int *sign, long *n)
{
	*sign = -1;
	*n = *n * -1;
}

char	*ft_itoa(long n)
{
	int		sign;
	long	longn;
	size_t	digit;
	char	*str;

	longn = n;
	sign = 1;
	digit = ft_countdigit(longn);
	if (n < 0)
		ft_minuscase(&sign, &longn);
	str = (char *)malloc(sizeof(char) * (digit + 1));
	if (!str)
		return (NULL);
	if (sign < 0)
		str[0] = '-';
	if (longn == 0)
		str[0] = '0';
	str[digit] = '\0';
	while (longn > 0)
	{
		str[--digit] = longn % 10 + '0';
		longn /= 10;
	}
	return (str);
}
