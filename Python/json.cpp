#include "json.h"

void Json::addKeyValue(const string& key, const string& value, bool end)
{
    addKey(key);
    jsonStr.append("\"");
    jsonStr.append(value);
    jsonStr.append("\"");
    close(end);
}

void Json::addKeyValue(const string& key, bool value, bool end)
{
    addKey(key);
    if (value) {
        jsonStr += "true";
    } else {
        jsonStr += "false";
    }
    close(end);
}

void Json::addKeyValue(const string& key, int value, bool end)
{
    addKey(key);
    jsonStr += to_string(value);
    close(end);
}


void Json::addKeyValue(const string& key, const Json& value, bool end)
{
    jsonStr.append("\"");
    jsonStr.append(key);
    jsonStr.append("\":");
    jsonStr += value.get();
    close(end);
}

void Json::addKey(const string& key)
{
    jsonStr.append("\"");
    jsonStr += key;
    jsonStr += "\":";
}

string Json::get() const
{
    return jsonStr;
} 

void Json::close(bool end)
{
    if (end == false) {
        jsonStr.append(",");
    } else {
        jsonStr.append("}");
    }
}

void Json::createArray(const vector<Json>& array)
{
    jsonStr.clear();
    jsonStr += "[";
    int cnt = 0;
    for (auto it : array) {
        jsonStr += it.get();
        cnt++;
        if (cnt < array.size()) {
            jsonStr += ",";
        }
    }
    jsonStr += "]";
}
