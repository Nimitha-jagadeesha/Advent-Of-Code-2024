#include <bits/stdc++.h>
using namespace std;

int main() {
  int n =1000;
  long long ans =0, x, y;
  vector<long long>a(n), b(n);
  map<long long, int> m;
  
  for(int i=0;i<n;i++) {
     cin>>a[i]>>b[i];
     if(m.find(b[i])!=m.end())
     m[b[i]]++;
     else
     m[b[i]] = 1;
  }
  
  for(int i=0;i<n;i++) {
   if(m.find(a[i])!=m.end()) {
   ans+=a[i] * m[a[i]];
   }
     
     
  }
  cout<<ans;
    return 0;
}
