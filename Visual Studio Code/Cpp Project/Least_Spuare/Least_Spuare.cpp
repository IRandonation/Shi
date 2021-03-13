#include  <stdlib.h> 
#include  <iostream> 
#include  <valarray> 
using namespace std; 
int main(int argc, char *argv[]) 
{  
    double DATA_X[] = {0.9,2.5,3.3,4.5,5.7,6.7}; 
    double DATA_Y[] = {1.1,1.6,2.6,3.2,4.0,5.0}; 
    valarray<double> data_x(DATA_X,sizeof(DATA_X)/sizeof(DATA_X[0]));
    valarray<double> data_y(DATA_Y,sizeof(DATA_Y)/sizeof(DATA_Y[0]));
    
    double A =0.0; 
    double B =0.0; 
    double C =0.0; 
    double D =0.0;

    A = (data_x*data_x).sum(); 
    B = data_x.sum(); 
    C = (data_x*data_y).sum(); 
    D = data_y.sum(); 
    double k,b,tmp =0; 
    if(tmp = (A*data_x.size()-B*B)) 
    { 
        k = (C*data_x.size()-B*D)/tmp; 
        b = (A*D-C*B)/tmp; 
    } 
    else 
    { 
        k=1; 
        b=0; 
    } 

    double Cal = k* data_x.max() +b;
    double YL = (data_y.max() - Cal)/(data_y.max() - data_y.min());

    cout <<"灵敏度k="<<k<<endl; 
    cout <<"线性度YL="<<YL<<endl; 
    cout <<"The Least Suqare is y="<<k<<"x+"<<b<<endl;
    return 0; 
}