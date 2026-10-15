/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/01 18:30:29 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/04 17:45:51 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	unsigned int	s_len;
	unsigned int	m_len;
	unsigned int	i;
	char			*res;

	s_len = (unsigned int)ft_strlen((char *)s);
	if (s_len < start)
		return (ft_strdup(""));
	if (len > (s_len - start))
		m_len = s_len - start;
	else
		m_len = len;
	res = (char *)malloc(sizeof(char) * (m_len + 1));
	if (res == NULL)
		return (NULL);
	i = 0;
	while (i < m_len)
	{
		res[i] = s[start + i];
		i++;
	}
	res[i] = '\0';
	return (res);
}
