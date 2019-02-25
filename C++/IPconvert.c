#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
typedef unsigned int uint32_t;
typedef unsigned char u_char;
uint32_t ngx_convert_ip_to_uint(char* base) ;
bool ngx_is_black_ip_style_two(char* base, char* src);
bool ngx_is_black_ip_style_one(char* base, char* src);
int main()
{
    char s[30], r[30], *pos;
    bool ans;
    scanf("%s\n%s", &s, &r);
    pos = strchr(s, '/');
    if (pos) {
         ans = ngx_is_black_ip_style_one(s, r);
    } else {
         ans = ngx_is_black_ip_style_two(s, r);
    }
    printf("\nans = %d\n", ans);
    return 0;
}
//192.168.1.1-254
bool ngx_is_black_ip_style_two(char* base, char* src)
{
	int 		 num = 0, len, len_of_base;
	char	    *pos;
	uint32_t 	 res[3] = {0,0,0};
	
	pos = strchr(base, '-');
    *pos = '\0';
	//IP 下限
	res[0] = ngx_convert_ip_to_uint(base);
	num = atoi(pos+1);
	printf("num = %d\n", num);	
	//IP上限	
	res[1] = res[0] + num;
	//待匹配IP
	res[2] = ngx_convert_ip_to_uint(src);
	printf("res = %u\t%u\t%u\n", res[0], res[1], res[2]);
	if (res[2] > res[0] && res[2] < res[1])
		return true;
	return false;

}

//判断安全组黑名单Ip 192.168.0.1/24
bool ngx_is_black_ip_style_one(char* base, char* src)
{
	int 		 num = 0, len;
	char		*pos;
	uint32_t 	 res[3] = {0,0,0};

	pos = (u_char*)strchr(base, '/');
	*pos = '\0';
	//IP 下限
	res[0] = ngx_convert_ip_to_uint(base);
	num = atoi(pos+1);
	printf("num = %d\n", num);	
	//IP上限	
	res[1] = res[0] + (1 << (32 - num));
	//待匹配IP
	res[2] = ngx_convert_ip_to_uint(src);
	printf("res = %u\t%u\t%u\n", res[0], res[1], res[2]);
	if (res[2] > res[0] && res[2] < res[1])
		return true;
	return false;

}

//IP 转换成数字
uint32_t ngx_convert_ip_to_uint(char* base) 
{
	int         i = 0;
	char	   *pos, *index;
	uint32_t    res = 0;	

	index = pos = base;
	while (*pos) {
		if (*pos == '.') {
            *pos = '\0';
			res = (res << 8) + atoi(index);
			printf("res = %u\n",res);
			index = pos+1;
		}
		pos++;
	}
	res = (res << 8) + atoi(index);	
	return res;
}

