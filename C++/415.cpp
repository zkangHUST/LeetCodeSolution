class Solution {
public:
    string addStrings(string num1, string num2) {
        reverse(num1.begin(),num1.end());
        reverse(num2.begin(),num2.end());
        string res="";
        int flag = 0;
        string::iterator i,j;
        i=num1.begin();
        j=num2.begin();
        char c;
        for(;i!=num1.end()&&j!=num2.end();i++,j++)
        {
           c = (flag + *i-'0'+*j-'0')%10+'0';
           flag = (flag + *i-'0'+*j-'0')/10;
           res+=c;
        }
        while(i!=num1.end())
        {
            c = (flag + *i-'0')%10+'0';
            flag = (flag + *i-'0')/10;
            res+=c;
            i++;
        }
        while(j!=num2.end())
        {
            c = (flag + *j-'0')%10+'0';
            flag = (flag + *j-'0')/10;
            res+=c;
            j++;
        }
        if(flag)
            res+='1';
        reverse(res.begin(),res.end());
        return res;
    }
};
