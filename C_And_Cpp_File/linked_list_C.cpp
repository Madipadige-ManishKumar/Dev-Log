#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node* head = NULL;

void insert_at_start(struct node** h, int value) {
    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = value;
    new_node->next = *h;
    *h = new_node;
}

void insert_at_end(struct node **h,int value)
{
	struct node* temp =*h;
	while(temp->next!=NULL)
	{
		temp=temp->next;
	}
	struct node *n = (struct node*)malloc(sizeof(struct node));
	n->data=value;
	n->next=temp->next;
	temp->next=n;
}
void insert_at_mid(struct node **h,int value,int p)
{
	int c=0;
	struct node *temp = *h;
	struct node *n = (struct node*)malloc(sizeof(struct node));
	n->data=value;
	if(p==0)
	{
		printf("hello\n");
	}
	else{
	
		while(temp!=NULL)
		{
			if(c==p)
			break;
			else
			{
				temp=temp->next;
			}
			c++;
		}
	}
	printf("temp-> data is %d\n",temp->data);
	n->next=temp->next;
	temp->next=n;
}
void dis(struct node* h) {
    struct node* temp = h;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}


int main() {
    head = NULL; // Initialize head to NULL

    // Insert nodes at the start
    insert_at_start(&head, 10);
    insert_at_start(&head, 20);
    insert_at_start(&head, 30);
	insert_at_end(&head,40);
	insert_at_mid(&head,50,1);
    // Display the list
    dis(head);

    // Free allocated memory (good practice)
    struct node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}

