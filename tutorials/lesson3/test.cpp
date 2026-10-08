#include<iostream>
#include<string>
using namespace std;

class Student{
    string name;
    string modules[10];
    int nofm;
    int student_number;

public:
    void set_modules(){
        cout<<"Enter number of modules tou have: ";
        cin>>nofm;
        for(int i=0;i<nofm;i++){
            cout<<"Enter the name of the module number "<<i+1<<" : ";
            getline(cin, modules[i]);
        }
    }
        void print(){
             for(int i=0;i<nofm;i++){
            cout<<"The module number "<<i+1<<" : "<<modules[i]<<endl;;
        }
        }

    


};
int main(){

    cout<<"hello world!"<<endl;
    Student abdou;
    abdou.set_modules();
    abdou.print();
    
    return 0;


}