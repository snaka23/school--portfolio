/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/02 10:19:43 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/04 18:17:27 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	i;
	size_t	s1_len;
	char	*res;

	i = 0;
	while (s1[i] && ft_strchr(set, s1[i]))
		i++;
	s1_len = ft_strlen(s1);
	while (s1_len > i && ft_strchr(set, s1[s1_len - 1]))
		s1_len--;
	res = ft_substr(s1, (unsigned int)i, (s1_len - i));
	return (res);
}
