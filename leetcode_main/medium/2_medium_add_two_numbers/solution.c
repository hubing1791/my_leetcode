//Definition for singly-linked list.
struct ListNode {
        int val;
        struct ListNode *next;
};

//用两个链表原有的结点进行拼接即可
//别人的解答更好，节点不存在可以直接补0运算，这样就不用讨论多种情况
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int temp_carry = 0 ;//保存暂时的进位
    int temp_result = 0 ;//保存暂时位上的结果
    struct ListNode* temp_list1=l1;
    struct ListNode* temp_list2=l2;
    while(temp_list1->next && temp_list2->next){//虽然这样会留一个节点不处理，但是留下了指针方便继续接点
        temp_result = (temp_list1->val + temp_list2->val + temp_carry)%10;
        temp_carry = (temp_list1->val + temp_list2->val + temp_carry)/10;
        temp_list1->val = temp_result;
        temp_list1 = temp_list1->next;
        temp_list2 = temp_list2->next;
        }
    temp_result = (temp_list1->val + temp_list2->val + temp_carry)%10;
    temp_carry = (temp_list1->val + temp_list2->val + temp_carry)/10;
    temp_list1->val = temp_result;
    //处理还没处理的一个借点
    if(temp_carry==0){
         if(temp_list2->next == NULL){
            return l1;
        }
        else{
            temp_list1->next = temp_list2->next;
            return l1;
        }
    }//因为必定至少有一个链表已经到头，那么如果没有进位只需要接一下即可
    else{
        if(temp_list2->next == NULL && temp_list1->next == NULL){
            l2->val = 1;
            l2->next = NULL;
            temp_list1->next = l2;//直接取用之前没有使用的l2的头作补充
            return l1;
        }
        else{
            if(temp_list1->next){
                temp_list1 = temp_list1->next;
            }
            else{
                temp_list1->next = temp_list2->next;
                temp_list1 = temp_list1->next;
            }

            while(temp_list1->next){
                temp_result = (temp_list1->val+temp_carry)%10;
                temp_carry = (temp_list1->val+temp_carry)/10;
                temp_list1->val=temp_result;
                temp_list1 = temp_list1->next;
            }
            temp_result = (temp_list1->val+temp_carry)%10;
            temp_carry = (temp_list1->val+temp_carry)/10;
            temp_list1->val=temp_result;
            if(temp_carry){
                l2->val = 1;
                l2->next = NULL;
                temp_list1->next = l2;
                return l1;
            }
            return l1;
        }
    }
}