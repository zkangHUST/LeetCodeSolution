#include<stdio.h>
#include<stdbool.h>
typedef unsigned int uint32_t;
typedef unsigned char u_char;
int main()
{

    return 0;
}
//192.168.1.1-254
bool ngx_is_black_ip_style_two(char* base, char* src)
{
	int num = 0, len, len_of_base;
	char* ip;
	uint32_t res[3] = {0,0,0};
	u_char	*pos;
	pos = base;	
	pos = (u_char*)ngx_strchr(base, '-');
	ip = base;
	len = pos - base;
    len_of_base = strlen(base);
	//IP 下限
	res[0] = ngx_convert_ip_to_uint(ip);
	num = ngx_atoi(pos+1, len_of_base - len -1);
	printf("num = %d\n", num);	
	//IP上限	
	res[1] = res[0] + num;
	//待匹配IP
	res[2] = ngx_convert_ip_to_uint(src);
	printf("res=%u\t%u\t%u",res[0],res[1],res[2]);
	//printf("res = %u\n", res);
	if (res[2] > res[0] && res[2] < res[1])
		return true;
	return false;
	//return res[0];
}

//判断安全组黑名单Ip 192.168.0.1/24
bool ngx_is_black_ip_style_one(char* base, char* src)
{
	int num = 0, len, len_of_base;
	char* ip;
	uint32_t res[3] = {0,0,0};
	u_char	*pos;
	pos = base;	
	pos = (u_char*)ngx_strchr(base, '/');
	ip = base;
	len = pos - base;
       len_of_base = strlen(base);
	//IP 下限
	res[0] = ngx_convert_ip_to_uint(ip);
	num = ngx_atoi(pos+1, len_of_base - len -1);
	printf("num = %d\n", num);	
	//IP上限	
	res[1] = res[0] + (1<<(32 - num));
	//待匹配IP
	res[2] = ngx_convert_ip_to_uint(src);
	printf("res=%u\t%u\t%u",res[0],res[1],res[2]);
	//printf("res = %u\n", res);
	if (res[2] > res[0] && res[2] < res[1])
		return true;
	return false;
	//return res[0];
}

//IP 转换成数字
uint32_t ngx_convert_ip_to_uint(char* base) 
{
	int i = 0, len = 0;
	u_char	*pos, *index;
	index = pos = base;
	uint32_t res=0;	
	while (i < strlen(base)) {
		if(*pos == '.') {
			len = pos - index;
			res = (res << 8) + ngx_atoi(index, len);
			printf("res = %u\n",res);
			index = pos+1;
		}
		pos++;
		i++;
	}
	len = pos - index;
	if(len)
		res = (res << 8) + ngx_atoi(index, len);	
	return res;
}
