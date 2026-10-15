/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 18:51:28 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/20 10:56:40 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*read_and_join(int fd, char *save)
{
	char	*tmp;
	int		read_bytes;
	char	*buf;

	buf = (char *)malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!buf)
		return (free(save), NULL);
	read_bytes = 1;
	while (!ft_strchr(save, '\n') && read_bytes > 0)
	{
		read_bytes = read(fd, buf, BUFFER_SIZE);
		if (read_bytes == -1)
			return (free(buf), free(save), NULL);
		if (read_bytes > 0)
		{
			buf[read_bytes] = '\0';
			tmp = ft_strjoin(save, buf);
			free(save);
			save = tmp;
			if (!save)
				return (free(buf), NULL);
		}
	}
	free(buf);
	return (save);
}

static char	*extract_line(char **save, int len)
{
	char	*res;
	char	*tmp;

	if (!save || !*save)
		return (NULL);
	if ((*save)[len] == '\n')
	{
		res = ft_substr(*save, 0, len + 1);
		if (!res)
			return (NULL);
		tmp = *save;
		*save = ft_substr(tmp, len + 1, ft_strlen(tmp) - len - 1);
		free(tmp);
		if (!*save)
			return (free(res), NULL);
		return (res);
	}
	res = ft_strdup(*save);
	free(*save);
	*save = NULL;
	if (!res)
		return (NULL);
	return (res);
}

char	*get_next_line(int fd)
{
	static char	*save;
	int			len;

	if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
		return (free(save), save = NULL, NULL);
	if (!save)
	{
		save = ft_strdup("");
		if (!save)
			return (NULL);
	}
	save = read_and_join(fd, save);
	if (!save || save[0] == '\0')
	{
		free(save);
		save = NULL;
		return (NULL);
	}
	len = 0;
	while (save[len] && save[len] != '\n')
		len++;
	return (extract_line(&save, len));
}
/*#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>

int	main(void)
{
	char	*a;
	int		fd;

	fd = open("./file1", O_RDONLY);
	a = get_next_line(fd);
	while (a)
	{
		printf("%s", a);
		free(a);
		a = get_next_line(fd);
	}
	close(fd);
	free(a);
	return (0);
}*/
