#include<iostream>
#include "base.h"
#include "reader.h"

// JSON_NAMESPACE_START
int main()
{
    string str = "{\"name\":\"vincent\", \"age\":18}";
    Reader reader(str);
    reader.parse();
}

// JSON_NAMESPACE_END
