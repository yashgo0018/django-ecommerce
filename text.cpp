#include<iostream>

using namespace std;

int main() {
	int a[100] = {1, -1, 2, -5, 5, 10, -8, 8, 15, 9};
	int n; cin >> n;
	for (int i=0; i<n; ++i){
		cin >> a[i];
	}
cout << max(a[0], a[1]);
	return 0;
}
