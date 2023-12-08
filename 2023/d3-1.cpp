#include <iostream>
#include <set>
#include <map>
#define ll long long
#define mp(a,b) make_pair(a,b)
using namespace std;

int main(){
    set<pair<ll,ll>> sym;
    map<pair<ll,ll>,ll> nums;
    map<pair<ll,ll>,ll> lens;
    string l;
    int ln = 0;
    while (getline(cin,l)){
        for (int i=0;i<l.length();i++){
            if (l[i] == '.') continue;
            if (l[i] <= '9' && l[i] >= '0'){
                ll n = 0;
                ll len = 1;
                while (l[i] <= '9' && l[i] >= '0' && i<l.length()){
                    n = n*10+(ll)(l[i]-'0');
                    i++;
                    len++;
                }
                nums[mp(i,ln)] = n;
                lens[mp(i,ln)] = len;
                i--;
            }
            else sym.insert(mp(i,ln));
        }
        ln++;
    }
    ll res = 0;
    for (auto p: nums){
        pair<ll,ll> loc = p.first;
        ll len = lens[loc];
        bool good = 0;
        if (sym.count(loc)) good = 1;
        loc = mp(loc.first+1,loc.second);
        for (int i=0;i<len+1 && !good;i++){
            loc = mp(loc.first-1,loc.second);
            if (sym.count(mp(loc.first,loc.second-1)) || sym.count(mp(loc.first,loc.second+1))){
                good = 1;
            }
        }
        if (sym.count(loc)) good = 1;
        if (good) res += p.second;
    }
    cout << res<<'\n';
}