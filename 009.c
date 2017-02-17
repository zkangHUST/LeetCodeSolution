bool isPalindrome(int x) {
    if(x<0)
        return false;
    else if(x<10)
        return true;
    else
    {
        int bit = (int)log10(x)+1;
        while(bit>0)
        {
            if(x%10!=x/((int)pow(10,bit-1)))
            {
                return false;
            }
            else 
            {
                x = x%((int)pow(10,bit-1));
                x/=10;
                bit -= 2;
            }
                
        }
        
    }
    return true;
}
