// Online C++ compiler to run C++ program online
#include <iostream>

void printComb(int& br,int a, int b, int c=0, bool d=0, bool e=0){
    std::cout<<"settlments: "<<a<<" cities: "<<b <<" vp: "<<c<<" ";
    if(d)
        std::cout<<"biggest Army ";
    if(e)
        std::cout<<"longest Road";
    std::cout<<std::endl;
    br++;
}
int main() {
    int sM = 5, cM = 4, vpM = 5, br = 0;
    bool bA = 0, lR = 0;
    for(int i=0; i<=sM;i++){
        for(int j = 0; j<=cM; j++){
            for(int k = 0; k<=5; k++){
                if(i + 2*j + k >=6){
                    if(i + 2*j + k>=10&&i +2*j +k<=11){
                        printComb(br,i,j,k);
                    }
                    else if(i +2*j + k == 8|| i + 2*j +k ==9){
                        printComb(br,i,j,k,1,0);
                        printComb(br,i,j,k,0,1);
                    }
                    else if(i + 2*j + k ==6 || i + 2*j + k==7){
                        printComb(br,i,j,k,1,1);
                    }
                }
            }
        }
    }    
    std::cout<<std::endl<<br;

    return 0;
}
