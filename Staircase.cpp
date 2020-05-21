#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {
    n = n-1;
    for(int i = 0; i <= n; i++){ // row
        for(int j = 0; j <= n; j++){ // column
            if(i < n-j){
                cout << " ";
            }
            else if (i >= n-j){
                cout << "#";
            }
        }
    cout << endl;
    }
}


int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
