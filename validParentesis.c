#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct Node_ {
  void *data;
  struct Node_ *next;
} Node;

typedef struct List_ {
  int size;
  Node * head;
  Node * tail;
  void(*destroy)(void *data);
} List;

#define list_size(list) ((list)->size)

void list_init(List* list, void(*destroy)(void *data)) {
  list->size = 0;
  list->head = NULL;
  list->tail = NULL;
  list->destroy = destroy;
  return;
}

void list_destroy(List* list) {
  void * data;
  while (list_size(list) > 0) {
    if (list_rem_next(list, NULL, (void **) &data) == 0 && list->destroy != NULL) {
      list->destroy(data);
    }
  }
  memset(list, 0, sizeof(List));
  return ;
}
int list_ins_next(List *list, Node *element, const void *data) {
  Node* new_element;
  if ((new_element = (Node *)malloc(sizeof(Node))) == NULL ) {
    return -1;
  }

  new_element->data = (void *)data;
  if (element == NULL ) {
    if (list_size(list) == 0) {
      list->tail = new_element;
    }
    new_element->next = list->head;
    list->head = new_element;
  }
  else {
    if (element->next == NULL) {
      list->tail = new_element;
    }
    new_element->next = element->next;
    element->next = new_element;
  }
  list->size++;
  return 0;
}
int list_rem_next(List *list, Node *element, void** data) {
  Node *old_elem;
  if (list_size(list) == 0)
    return -1;

  if (element == NULL ) {
    if (list_size(list) == 1 )
      list->tail = NULL;

    *data = list->head->data;
    old_elem = list->head;
    list->head = list->head->next;
  }
  else {
    if (element->next == NULL )
      return -1;

    *data = element->next->data;
    old_elem = element->next;
    element->next = old_elem->next;
    if (element->next = NULL)
      list->tail = NULL;
  }


  free(old_elem);
  list->size--;
  return 0;
}

int match( char* in, char *out) {
  if ( *in == '(' && *out == ')'){
    return 1;
  }
  else if ( *in == '{' && *out == '}'){
    return 1;
  }
  else if ( *in == '[' && *out == ']'){
    return 1;  
  }
  return 0;
}

bool isValid(char *s) {
  int size = strlen(s);
  if (size % 2 == 1){
    return false;
  }
  int i;
  List* list;
  list = (List *)malloc(sizeof(List));
  list_init(list, NULL);
  char* paren;

  for(i = 0; i < size; i++) {
    if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
      list_ins_next(list, NULL, s[i]);
       
    }
    else {
      if (list_rem_next(list,NULL,(void **)&paren) == -1) {
        list_destroy(list);
        free(list);
        return false;  
      }
      if ( match(&paren, &s[i]) == 0 ) {
        list_destroy(list);
        free(list);
        return false;
      }
    }
  }
  if (list_size(list) == 0 ){
    list_destroy(list);
    free(list);
    return true;
  }
  else {
    list_destroy(list);
    free(list);
    return false;
  }
}
