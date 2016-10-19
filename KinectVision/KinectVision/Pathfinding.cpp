//Pathfinding algorithm

#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <ctime>
#include <math.h>

using namespace cv;
using namespace std;

vector<int> origin;
vector<int> goal;
const int MAP_WIDTH = 100;		//horizontal test map size
const int MAP_HEIGHT = 100;		//vertical test map size

enum DIRECTION {MOVE_FORWARD, MOVE_BACK, MOVE_LEFT, MOVE_RIGHT, TURN_LEFT, TURN_RIGHT, 
	WALK_STOP, WALK_READY, WALK_SPEED_SLOW, WALK_SPEED_MEDIUM, WALK_SPEED_FAST};



class SearchNode
{
public:
		int NodePosX;	
		int NodePosY;			// current position of node being searched

		float EstimateDistance(SearchNode &nodegoal);
		bool IsGoal(SearchNode &nodegoal);
		bool GetSuccessors(AStarSearch<SearchNode> *astarsearch, SearchNode *parent_node);
		float GetCost(SearchNode &successor);
		bool IsSameState(SearchNode &rhs);
		void PrintNodeInfo();
};

//simple display of node info
void SearchNode::PrintNodeInfo()
{
	char str[100];
	sprintf(str, "Node Position : (%d, %d)", NodePosX, NodePosY);
	cout << str;
}

bool SearchNode::IsSameState(SearchNode &rhs)
{
	//same state is when x,y are the same.  
	if ((NodePosX == rhs.NodePosX) && (NodePosY == rhs.NodePosY))
	{
		return true;
	}
	else
	{
		return false;
	}
}

float SearchNode::EstimateDistance(SearchNode &nodegoal)
{
	return fabsf(NodePosX - nodegoal.NodePosX) + fabsf(NodePosY - nodegoal.NodePosY);
}


//see if we have reached the end!
bool SearchNode::IsGoal(SearchNode &nodegoal)
{
	if ((NodePosX == nodegoal.NodePosX) && (NodePosY == nodegoal.NodePosY))
	{
		return true;
	}
	return false;
}



int main()
{
	unsigned int SearchCount = 0;
	unsigned int NumSearches = 1;

	while (SearchCount < NumSearches)
	{
		//placeholder
		SearchNode nodeStart;
		nodeStart.NodePosX = KINECT_DATAX;
		nodeStart.NodePosY = KINECT_DATAY;

		SearchNode nodeEnd;
		nodeEnd.NodePosX = KINECT_DATAX;
	}
	//program is done when robot reaches the goal point
}




