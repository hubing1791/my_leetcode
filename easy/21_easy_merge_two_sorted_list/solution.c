/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

//因为python没有真链表，就用c先实现一下
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    if(l1==NULL&&l2==NULL){
        return NULL;
    }
    else if(l1==NULL&&l2!=NULL){
        return l2;
    }
    else if(l1!=NULL&&l2==NULL){
        return l1;
    }//排除空链表
    struct ListNode* temp_node1 =l1;
    struct ListNode* temp_node2 =l2;
    struct ListNode* l3 =NULL;
    struct ListNode* temp_node3 =   NULL;
    if(temp_node1->val<=temp_node2->val){
        l3=temp_node1;
        temp_node1=temp_node1->next;
        temp_node3=l3;
    }
    else{
        l3=temp_node2;
        temp_node2=temp_node2->next;
        temp_node3=l3;
    }//先初始化l3和temp_node3
    while(temp_node1!=NULL&&temp_node2!=NULL){
        if(temp_node1->val<=temp_node2->val){
            temp_node3->next=temp_node1;
            temp_node1=temp_node1->next;
            temp_node3=temp_node3->next;
        }
        else{
            temp_node3->next=temp_node2;
            temp_node2=temp_node2->next;
            temp_node3=temp_node3->next;
        }
    }
    if(temp_node1==NULL&&temp_node2==NULL){
        return l3;
    }
    else if(temp_node1==NULL&&temp_node2!=NULL){
        temp_node3->next=temp_node2;
        return l3;
    }
    else if(temp_node1!=NULL&&temp_node2==NULL){
        temp_node3->next=temp_node1;
        return l3;
    }
    return l3;
}