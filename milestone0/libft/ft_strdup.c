/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/01 16:36:48 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/07 16:38:35 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*res;
	size_t	s_len;
	size_t	i;

	s_len = ft_strlen(s);
	res = (char *)malloc(sizeof(char) * (s_len + 1));
	if (res == NULL)
		return (NULL);
	i = 0;
	while (i < s_len)
	{
		res[i] = s[i];
		i++;
	}
	res[i] = '\0';
	return (res);
}
