class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> um;

    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        um[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        int l=0, r=um[key].size()-1, mid;
        string res = "";
        
        while(l<=r){
            mid = (l+r)/2;
            if(timestamp>=um[key][mid].first)
            {
                res = um[key][mid].second;
                l = mid+1;
            }else
                r = mid-1;
        }
        return res;
    }
};
