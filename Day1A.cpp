#include <bits/stdc++.h>
using namespace std;

int main() {
  int n =1000;
  long long ans =0, x, y;
  vector<long long>a(n), b(n);
  
  for(int i=0;i<n;i++) {
     cin>>a[i]>>b[i];
     ans+= abs(x-y);
  }
   sort(a.begin(),a.end());
   sort(b.begin(),b.end());
  for(int i=0;i<n;i++) {
     ans+= abs(a[i]-b[i]);
  }
  cout<<ans;
    return 0;
}
