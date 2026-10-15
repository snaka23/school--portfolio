/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 20:04:13 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/01 14:42:40 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

size_t	ft_strlen(const char *s)
{
	size_t	len;

	len = 0;
	while (s[len])
		len++;
	return (len);
}

static int	skip_space_symbol(const char **nptr)
{
	int	sign;

	sign = 1;
	while ((9 <= **nptr && **nptr <= 13) || **nptr == 32)
		(*nptr)++;
	if (**nptr == '+' || **nptr == '-')
	{
		if (**nptr == '-')
			sign = -sign;
		(*nptr)++;
	}
	return (sign);
}

int	ft_safe_atoi(const char *nptr, int *flag)
{
	int		sign;
	long	value;
	int		has_digit;

	sign = skip_space_symbol(&nptr);
	value = 0;
	has_digit = 0;
	*flag = 0;
	while ('0' <= *nptr && *nptr <= '9')
	{
		has_digit = 1;
		value = value * 10 + (*nptr - '0');
		nptr++;
	}
	value = value * sign;
	if (!has_digit || *nptr != '\0')
		*flag = -1;
	if (!(-2147483648 <= value && value <= 2147483647))
		*flag = -1;
	return ((int)value);
}

int	ft_strcmp(const char *s1, const char *s2)
{
	size_t	i;

	i = 0;
	while (s1[i] || s2[i])
	{
		if ((unsigned char)s1[i] != (unsigned char)s2[i])
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
		i++;
	}
	return (0);
}
