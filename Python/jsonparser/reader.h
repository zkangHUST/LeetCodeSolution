#include<string>
#include "base.h"
using namespace std;

// JSON_NAMESPACE_START
struct token;

class Reader {
public:
    Reader(){}
    Reader(const std::string& str):jsonStr(str), p(0), end(str.length()) {}
    bool parse();

private:
    token nextToken();
private:
    string::size_type p;
    string::size_type end;
    string jsonStr;
};

enum tokenType {
    NONE = 0,
    L_BRACE, // {
    R_BRACE, // }
    L_BRACK, // [
    R_BRACK, // ]
    STRING, 
    INT_NUM,
    FLOAT,
    BOOL,
    COLON,
    COMMA
};

struct token {
    token():type(NONE){}
    tokenType type;
    string      value;
    friend ostream & operator<<(ostream &out, token &obj) {
        out << "{" << obj.type << ":" << obj.value << "}" << endl;
        return out;
    }
    
};
// JSON_NAMESPACE_END