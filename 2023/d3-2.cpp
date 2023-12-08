#include <iostream>
#include <set>
#include <map>
#define ll long long
#define mp(a,b) make_pair(a,b)
using namespace std;

int main(){
    set<pair<ll,ll>> sym;
    map<ll,ll> nums;
    map<pair<ll,ll>,ll> ids;
    string l;
    int ln = 0;
    ll id = 0;
    while (getline(cin,l)){
        for (int i=0;i<l.length();i++){
            if (l[i] == '.') continue;
            if (l[i] <= '9' && l[i] >= '0'){
                ll n = 0;
                ll len = 1;
                while (l[i] <= '9' && l[i] >= '0' && i<l.length()){
                    n = n*10+(ll)(l[i]-'0');
                    ids[mp(i,ln)] = id;
                    i++;
                    len++;
                }
                nums[id] = n;
                i--;
                id++;
            }
            else if (l[i] == '*') sym.insert(mp(i,ln));
        }
        ln++;
    }
    ll res = 0;
    
    for (auto p: sym){
        set<ll> ress;
        for (int dx=-1;dx<2;dx++){
            for (int dy=-1;dy<2;dy++){
                if (ids.count(mp(p.first+dx,p.second+dy))){
                    ress.insert(ids[mp(p.first+dx,p.second+dy)]);
                }
            }
        }
        if (ress.size() == 2){
            res += nums[*ress.begin()] * nums[*ress.rbegin()];
        }
    }
    cout << res<<'\n';
}