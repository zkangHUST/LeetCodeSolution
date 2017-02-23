#include<stdio.h>
#include<string.h>
int table[1000][1000]={0};
int main()
{
	char s[1001];
//	int table[1000][1000]={0};
	scanf("%s",s);
	int i =0,len = strlen(s),max = 0,begin = 0;
	for(i=0;i<len;i++)
		table[i][i] = 1;
	for(i=0;i<len-1;i++)
	{
		if(s[i]==s[i+1])
		{
			table[i][i+1] = 1;
			max = 2;
			begin = i;
		}
	}
	int l,j;
	for(l=3;l<=len;l++)
	{
		for(i=0;i<len-l+1;i++)
		{
			j = i+l-1;
			if(s[i]==s[j]&&table[i+1][j-1])
			{
				table[i][j] = 1;
				max = l;
				begin = i;
			}
		}
	}
	for(i=begin;i<max;i++)
		putchar(s[i]);
	return 0;
}
