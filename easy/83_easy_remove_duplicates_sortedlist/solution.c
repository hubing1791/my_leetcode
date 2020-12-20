struct ListNode {
    int val;
    struct ListNode *next;
 };

 struct ListNode* deleteDuplicates(struct ListNode* head){
	 if (head ==NULL || head->next == NULL){
		 return head;
	 }
	 int temp=head->val;
	 struct ListNode* temp_node = head;
	 while(temp_node->next){
		 if (temp_node->next->val == temp){
			 temp_node->next=temp_node->next->next;
		 }
		 else{
			 temp=temp_node->next->val;
			 temp_node = temp_node->next;
		 }
	 }
	return head;
}