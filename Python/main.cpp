#include<iostream>
#include "json.h"

using namespace std;

int main()
{
    Json child1;
    child1.addKeyValue("subject", string("subscribe"));
    child1.addKeyValue("to", string("vincent.zheng@zoom.us"));
    child1.addKeyValue("age", 18);
    child1.addKeyValue("male", true, true);

    cout << child1.get() << endl;
    Json child2;
    child2.addKeyValue("subject", string("subscribe"));
    child2.addKeyValue("to", string("vincent.zheng@zoom.us"));
    child2.addKeyValue("age", 18);
    child2.addKeyValue("male", true, true);

    cout << child2.get() << endl;
    // string value = child.get();

    Json father;
    father.addKeyValue("name", child1);
    father.addKeyValue("aaa", child2);
    father.addKeyValue("aa", false, true);

    vector<Json> array(3, father);
    Json grandFather;
    grandFather.createArray(array);

    cout << endl << endl;
    cout << grandFather.get() << endl;
    
    // cout << grandFather.get() << endl;
    return 0;
}