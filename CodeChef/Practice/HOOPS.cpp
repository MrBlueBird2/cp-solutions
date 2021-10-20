#include <iostream>
using namespace std;

int main()
{
    /*
    int t;
    cin >> t;
    for(int i = 0; i<t; i++) {
        int ans = 0;
        int D, d, P, Q;
        cin >> D >> d >> P >> Q;
        for(int j = 0; j<D; j++) {
            ans += (P+(j/d)*Q);
        }
        cout << ans << endl;
    }
    */
    int t;
    cin >> t;
    for(int i = 0; i < t; i ++ ) {
        int n;
        cin >> n;
        cout << (n+1)/2 << endl;
    }
}