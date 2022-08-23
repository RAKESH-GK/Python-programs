#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int n;
void merge(int a[],int low,int mid,int high){
    int i=low,j=mid+1,k=low,b[n];
        while(i<=mid && j<=high){
            if(a[i]<=a[j]){
                b[k++]=a[i++];
            }
            else{
                b[k++]=a[j++];
            }
        }
            while(i<=mid){
                b[k++]=a[i++];
            }
            while(j<=high){
                b[k++]=a[j++];
            }
        for(int i=low;i<=high;i++){
            a[i]=b[i];
        } 
}
void mergesort(int a[],int low,int high){
    int mid;
    if(low<high){
        mid=(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,mid,high);
    }
}


void main(){
    int ch=1;
    while(ch){
        printf("enter the value for n:");
        scanf("%d",&n);
        double t=clock();
        int a[n];
        for(int i=0;i<n;i++){
            a[i]=rand()% 2000;
        }
        printf("values before sort:\n");
        for(int i=0;i<n;i++){
            printf("%d ",a[i]);
        }
        mergesort(a,0,n-1);
        t=clock()-t;  
        printf("\nvalues after sort:\n");
        for(int i=0;i<n;i++){
            printf("%d ",a[i]);
        }
        printf("\ntime taken is:%f",((double)t)/CLOCKS_PER_SEC);
        printf("\nwant to test again(1/0):");
        scanf("%d",&ch);
        if(ch==0){
        exit(0);
        }
    }
    
}
