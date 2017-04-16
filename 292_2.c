bool canWinNim(int n)
{
	bool a,b,c;
	if(n==1||n==2||n==3)
		return true;
	else
	{
		if(canWinNim(n-1)==false)
			return true;
		else if(canWinNim(n-2)==false)
			return true;
		else if(canWinNim(n-3)==false)
			return true;
		else
			return false;
	}
}
