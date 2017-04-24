class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> res;
        string a("QWERTYUIOPqwertyuiop");
        string b("ASDFGHJKLasdfghjkl");
        string c("ZXCVBNMzxcvbnm");
        int status = 0;
        for(vector<string>::iterator it=words.begin();it!=words.end();it++)
        {
            for(string::iterator i=it->begin();i!=it->end();i++)
            {
                if(a.find(*i)!=string::npos){
                    if(status==0)
                        status=1;
                    else if(status==2||status==3){
                        status = 0;
                        break;
                    }
                }
                else if(b.find(*i)!=string::npos) {
                    if(status==0)
                        status=2;
                    else if(status==1||status==3){
                        status = 0;
                        break;
                    }
                }
                else if(c.find(*i)!=string::npos){
                    if(status==0)
                        status=3;
                    else if(status==1||status==2){
                        status = 0;
                        break;
                    }
                }
            }
            if(status ==1||status==2||status==3){
                    res.push_back(*it);
                    status = 0;
            }
        }
        return res;
    }
};
