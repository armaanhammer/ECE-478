//Pathfinding algorithm

#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace cv;
using namespace std;

vector<int> origin;
vector<int> goal;


enum DIRECTION {MOVE_FORWARD, MOVE_BACK, MOVE_LEFT, MOVE_RIGHT, TURN_LEFT, TURN_RIGHT, 
	WALK_STOP, WALK_READY, WALK_SPEED_SLOW, WALK_SPEED_MEDIUM, WALK_SPEED_FAST};




int main()
{
	//start by situate

	//program is done when robot reaches the goal point
}


//print out a test grid, something to simulate obstacles and  goals.
//then remove it in final build

void situate(int origin, int goal)
{



}

