/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/02 11:37:43 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/04 18:19:00 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static int	countwords(char	*s, char c)
{
	int	count;

	count = 0;
	while (*s)
	{
		while (*s && *s == c)
			s++;
		if (*s)
		{
			count++;
			while (*s && *s != c)
				s++;
		}
	}
	return (count);
}

static char	*wordstrdup(char *s, char c)
{
	char	*res;
	int		count;
	int		i;

	count = 0;
	while (s[count] && s[count] != c)
		count++;
	res = (char *)malloc(sizeof(char) * (count + 1));
	if (res == NULL)
		return (NULL);
	i = 0;
	while (count > i)
	{
		res[i] = s[i];
		i++;
	}
	res[i] = '\0';
	return (res);
}

static char	**free_all(char	**res, int i)
{
	while (i > 0)
	{
		i--;
		free(res[i]);
	}
	free(res);
	return (NULL);
}

char	**ft_split(char const *s, char c)
{
	char	**res;
	int		i;

	res = (char **)malloc(sizeof(char *) * (countwords((char *)s, c) + 1));
	if (res == NULL)
		return (NULL);
	i = 0;
	while (*s)
	{
		while (*s && *s == c)
			s++;
		if (*s)
		{
			res[i] = wordstrdup((char *)s, c);
			if (res[i] == NULL)
				return (free_all(res, i));
			i++;
			while (*s && *s != c)
				s++;
		}
	}
	res[i] = NULL;
	return (res);
}
