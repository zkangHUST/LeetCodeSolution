bool judgeCircle(char* moves) {
    int i= 0;
    int down =0, left = 0;
   while(moves[i]!='\0')
    {
        switch (moves[i])
        {
            case 'U':   down++;break;
            case 'D':   down--;break;
            case 'L':   left++;break;
            case 'R':   left--;break;
        }    
       i++;        
    }
    if (down==0&&left==0 )
        return true;
    else 
        return false;
}
