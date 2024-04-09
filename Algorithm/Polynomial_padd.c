#include <stdio.h>
#define MAX_TERMS 100
#include <stdlib.h>
void attach(float,int);

typedef struct {
    float coef;
    int exp;
}Polynomial;

Polynomial terms[MAX_TERMS];
int avail = 0;

int COMPARE(int a, int b){
    if (a > b) return 1;
    else if (a == b) return 0;
    else return -1;
}

void padd(int starta, int finisha, int startb, int finishb, int *startd, int *finishd)
{  
    float coefficient;
    *startd = avail;
    while (starta <= finisha && startb <= finishb)
           switch (COMPARE(terms[starta].exp, terms[startb].exp)) {  
                 case -1:   
                                attach(terms[startb].coef, terms[startb].exp);
                                startb++; 
                                break;
                 case 0:    
                                coefficient = terms[starta].coef + terms[startb].coef;
                                if(coefficient) 
                                    attach(coefficient, terms[starta].exp);
                                starta++; 
                                startb++; 
                                break;
                 case 1:    
                                attach(terms[starta].coef,terms[starta].exp);
                                starta++;
           }
            for(;starta <= finisha;starta++)
                attach(terms[starta].coef,terms[starta].exp);
            for (;startb <= finishb;startb++)
                attach(terms[startb].coef,terms[startb].exp);
            *finishd = avail - 1;
}
void attach(float coefficient, int exponent)
{            
            if (avail >= MAX_TERMS) {
                    fprintf(stderr, "다항식에 항이 너무 많습니다!.");
                    exit(1);          }
            terms[avail].coef = coefficient;
            terms[avail++].exp = exponent;
}

int main() {
    int startd, finishd;

    //A
    attach(3.0,2);
    attach(4.0,1);


    int starta = 0;
    int finisha = avail -1;

    //B
    attach(4.0, 3); 
    attach(2.0,2);
    attach(6.0,0);

    int startb = finisha + 1;
    int finishb = avail - 1;

    padd(starta, finisha, startb, finishb, &startd, &finishd);

   for(int i = startd; i< finishd;i++){
        printf("%3.1lfx^%d + ",terms[i].coef, terms[i].exp);
   }
   printf("%3.1lfx^%d",terms[finishd].coef, terms[finishd].exp);

   return 0;
}
