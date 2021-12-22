#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;
int main(){
    vector<vector<vector<vector<vector<pair<int,int>>>>>>dp;
    for (int i=0;i<10;i++){
        for (int j=0;j<10;j++){
            for (int q=0;q<21;q++){
                for (int w=0;w<21;w++){
                    dp[i][j][q][w].emplace(0,0);
                }
            }
        }
        dp.append
    }
    
}