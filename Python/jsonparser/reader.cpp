#include<iostream>
#include<cctype>
#include "reader.h"

// JSON_NAMESPACE_START

bool Reader::parse()
{
    while (p < end) {
        token t = nextToken();
        cout << t << endl;
    }
    return true;
}

token Reader::nextToken()
{
    while (isblank(jsonStr[p])) p++;
    
    token t;
    bool notfound = true;
    // while (notfound && p < jsonStr.length()) {
    switch (jsonStr[p])
    {
    case '{':
        t.type = L_BRACE;  // {
        t.value = "{";
        notfound = false;
        break;
    case '}':
        t.type = R_BRACE;
        t.value = "}";
        notfound = false;
        break;
    case '[':
        t.type = L_BRACK;  // {
        t.value = "[";
        notfound = false;
        break;
    case ']':
        t.type = R_BRACK;
        t.value = "]";
        notfound = false;
        break;
    case ':':
        t.type = COLON;
        t.value = ":";
        notfound = false;
        break;
    case '\"': {
            t.type = STRING;
            int lpos = p++;
            while (jsonStr[p] != '\"') p++;
            t.value = jsonStr.substr(lpos, p - lpos + 1);
            notfound = false;
            break;
        }
    case ',': {
            t.type = COMMA;
            t.value = ',';
            notfound = false;
            break;
        }
    default:
        int num = 0;
        while (isdigit(jsonStr[p])) {
            num = num * 10 + (jsonStr[p] - '0');
            p++;
        }
        t.type = INT_NUM;
        t.value = to_string(num);
        notfound = false;
        break;
    }
    p++;
    return t;
}
// JSON_NAMESPACE_END