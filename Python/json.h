#include<string>
#include<vector>
#include<map>
using namespace std;

class Json {
public:
    Json():jsonStr("{"){}
    void addKeyValue(const string& key, const Json& value, bool end = false);
    void addKeyValue(const string& key, int value, bool end = false);
    void addKeyValue(const string& key, const string& value, bool end = false);
    void addKeyValue(const string& key, bool value, bool end = true);

    void createArray(const vector<Json>& array);
    // void addKeyArray(const string& key, );
    
    string get() const;
    
private:
    void addKey(const string& key);
    void close(bool end);

private:
    string jsonStr;
};