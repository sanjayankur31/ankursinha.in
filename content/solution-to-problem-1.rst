Solution to Problem 1
#####################
:date: 2009-02-20 12:34
:author: ankur
:category: Tech
:tags: Bitwise, C Programming
:slug: solution-to-problem-1

Well, I thought a lot about how to help Spidey, even peeked at the hint
( which, sadly, din't really help much :( )

The problem :
http://dodoincfedora.wordpress.com/2009/02/19/programming-skills/

***My solution :***

*If you want the .c file,( it'll be properly indented etc. ) I've put it
up here : http://ankursinha.fedorapeople.org/misc/problem1.c*

.. code-block:: c

    /\*
    \* My algo :
    \* The node with maximum number of links to the other nodes
    should be the result.
    \* In case all nodes have same number of links, Ill calculate the
    middle node.
    \* Although I dont think the above case will ever occur, I'm
    coding with its possibility.
    \* I'll give it more thought later.
    \*
    \*/

    #include
    #include#define MAX\_NODES 1000
    #define MAX\_CASES 10000

    int main(int argc, char \*argv[]){

    int graph[MAX\_NODES][MAX\_NODES];
    int number\_cases;
    int number\_nodes[MAX\_CASES];
    int i, j,k;
    int t1,t2;
    int node\_link\_count[MAX\_NODES];
    int max;
    /\* char temp; \*/

    if(argc > 1){
    fprintf(stderr,"Error : %s No arguments may be passed to this
    programn",argv[0]);
    exit (EXIT\_FAILURE);
    }

    printf("Enter the input cases: ");
    scanf("%d",&number\_cases);

    for(i = 0 ; i < number\_cases; i++){

    for(k = 0; k < MAX\_NODES; k++)
    for(j = 0; j < MAX\_NODES; j++)
    graph[k][j] = 0;

    for(k = 0; k < MAX\_NODES; k++)
    node\_link\_count[k] = 0;

    printf("Enter number of nodes in case %d: ",i+1);
    scanf("%d",&number\_nodes[i]);

    printf("Enter :n" );
    for(j = 0; j < (number\_nodes[i] - 1); j++){
    scanf("%d %d",&t1,&t2);graph[t1][t2] = graph[t2][t1] = 1;
    }

    for(j = 0; j < number\_nodes[i]; j++){
    for(k = 0; k < number\_nodes[i]; k++){
    if(graph[j][k] == 1)
    node\_link\_count[j]++;
    }
    }

    max = node\_link\_count[0];

    for(j = 1; j < number\_nodes[i]; j++)
    if(max < node\_link\_count[j])
    max = node\_link\_count[j];

    if(max == node\_link\_count[0] && node\_link\_count[0] ==
    node\_link\_count[1]){
    printf("Result(s) : %d",(number\_nodes[i]/2));
    }

    else {
    printf("Result(s) : ");
    for (j = 0; j < number\_nodes[i]; j++)
    if (node\_link\_count[j] == max)
    printf("%d ",j);

    printf("n");
    }
    }

    exit(EXIT\_SUCCESS);
    }

    It does give the result as per the trial input and output, but I'm
    still not completely convinced that this is a fool proof method.
