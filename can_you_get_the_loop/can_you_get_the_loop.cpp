#include <iostream>
#include <unordered_map> // Add this line to include the unordered_map header

using namespace std; 

// define a simple class Node
class Node {
public:
    int data;
    Node* next;
};

int getLoopSize(Node* startNode)
{
    int counter = 0;
    unordered_map<Node*, int> nodeMap;
    
    while (nodeMap.find(startNode) == nodeMap.end())
    {

        nodeMap[startNode] = counter++;
        startNode = startNode->next;
    }

    return counter - nodeMap[startNode];
}

int main() {
    
    return 0;
}
