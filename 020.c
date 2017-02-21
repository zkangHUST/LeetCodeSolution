bool isValid(char* s) {
    char stack[10000];
    char* p= s;
    int i= 0;
    while(*p!='\0')
    {
        if(*p=='('||*p=='['||*p=='{')
        {
            i++;
            stack[i]=*p;
            p++;
        }
        else if(*p==')')
        {
            if(stack[i]=='(')
            {
                i--;
                p++;
            }
            else 
                return 0;

        }
        else if(*p==']')
        {
            if(stack[i]=='[')
            {
                i--;
                p++;
            }
            else 
                return 0;

        }
        else if(*p=='}')
        {
            if(stack[i]=='{')
            {
                i--;
                p++;
            }
            else 
                return 0;

        }
        else 
            return 0;
    }
    if(i>0)
        return 0;
    else
        return 1;
}
