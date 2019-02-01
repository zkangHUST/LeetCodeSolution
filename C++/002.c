/*
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 *};
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *p,*q,*r,*m,*tmp;
    p=l1,q=l2;
    int sum=0,flag = 0;
    r = (struct ListNode*)malloc(sizeof(struct ListNode));
    m=r;
    while(p!=NULL&&q!=NULL)
    {
        tmp = (struct ListNode*)malloc(sizeof(struct ListNode));     
        sum =  p->val + q->val + flag;
        flag=sum>=10?1:0;
        tmp->val = sum%10;
        tmp->next = NULL;
        m->next = tmp;
        m= m->next;
        p=p->next;
        q=q->next;
    }
    while(p!=NULL)
    {
        tmp = (struct ListNode*)malloc(sizeof(struct ListNode));     
        sum =  p->val + flag;
        flag=sum>=10?1:0;
        tmp->val = sum%10;
        tmp->next = NULL;
        m->next = tmp;
        m= m->next;
        p=p->next;
    }    
    while(q!=NULL)
    {
        tmp = (struct ListNode*)malloc(sizeof(struct ListNode));     
        sum =  q->val + flag;
        flag=sum>=10?1:0;
        tmp->val = sum%10;
        tmp->next = NULL;
        m->next = tmp;
        m= m->next;
        q=q->next;
    }
    if(flag)
    {
        tmp = (struct ListNode*)malloc(sizeof(struct ListNode));   
        tmp->val = 1;
        tmp->next = NULL;
        m->next = tmp;
        m=m->next;
    }
    return r->next;
}
