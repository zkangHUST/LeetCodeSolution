bool canWinNim(int n) {
    if(n==1||n==2||n==3)
        return true;
    else if(n%4==0){   //重点在于找规律
        return false;
    }
    else
        return true;
}
