#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 101

typedef int element;
typedef struct {
    element stack[MAX_STACK_SIZE];
    int top;
} StackType;

StackType *st;

void init(StackType *s){
    s->top = -1;
}

int is_empty(StackType *s){
    return (s->top == -1);
}

int is_full(StackType *s){
    return (s->top == (MAX_STACK_SIZE-1));
}

void push(StackType *s, element item){
    if(is_full(s)){
        fprintf(stderr,"Stack is full!\n");
        exit(1);
    }
    else s->stack[++(s->top)] = item;
}

element pop(StackType *s){
    if(is_empty(s)){
        fprintf(stderr,"Stack is empty!\n");
        exit(1);
    }
    else return s->stack[(s->top)--];
}

element peek(StackType *s){
    if(is_empty(s)){
        fprintf(stderr,"Stack is empty!\n");
        exit(1);
    }
    else return s->stack[s->top];
}

void showStack(StackType *s){
    for(int i =0 ; i<= s->top; i++){
        printf("%d\n",s->stack[i]);
    }
}

int main() {

    st = (StackType *)malloc(sizeof(StackType));

    init(st);

    push(st,5);
    push(st,3);
    showStack(st);
    element a = pop(st);
    int b = is_empty(st);
    printf("POP : %d\n",a);
    printf("Is empty? : %d\n",b);

    free(st);
    return 0;

}