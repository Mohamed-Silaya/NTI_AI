int arr[10];
int *ptr1 = arr;
int *ptr2 = arr + 5;
// This is invalid because the restrict type qualifier is used​
restrict int *ptr3 = ptr1;
// This code may not be safe because ptr1 and ptr3 may alias each other​
ptr3 = ptr2;





